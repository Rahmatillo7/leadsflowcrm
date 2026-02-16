from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from apps.tasks.models import Task
from apps.notifications.models import Notification



@shared_task
def check_overdue_tasks():
    now = timezone.now()

    overdue_tasks = Task.objects.filter(
        deadline__lt=now,
        status="PENDING"
    )

    count = 0

    for task in overdue_tasks:
        task.status = "OVERDUE"
        task.save()

        Notification.objects.create(
            user=task.assigned_to,
            title="Task Overdue",
            message=f"{task.title} deadline o'tib ketdi!"
        )

        count += 1
        print(f"⚠️ OVERDUE: {task.title}")

    return f"{count} ta task overdue qilindi"


@shared_task
def reminder_before_deadline():
    now = timezone.now()
    next_day = now + timedelta(hours=24)

    tasks = Task.objects.filter(
        deadline__range=(now, next_day),
        status="PENDING"
    )

    count = 0

    for task in tasks:
        Notification.objects.create(
            user=task.assigned_to,
            title="Task Reminder",
            message=f"{task.title} 24 soatdan keyin tugaydi."
        )

        count += 1
        print(f"⏰ Reminder: {task.title}")

    return f"{count} ta reminder yuborildi"


@shared_task
def notify_task_created(task_id):
    try:
        task = Task.objects.get(id=task_id)

        Notification.objects.create(
            user=task.assigned_to,
            title="New Task Assigned",
            message=f"Sizga yangi task biriktirildi: {task.title}"
        )

        print(f"🆕 Task notification: {task.title}")

        return "Notification sent"

    except Task.DoesNotExist:
        return "Task topilmadi"


@shared_task
def update_task_status(task_id, new_status):
    try:
        task = Task.objects.get(id=task_id)
        task.status = new_status
        task.save()

        print(f"🔄 Status yangilandi: {task.title} → {new_status}")

        return "Status updated"

    except Task.DoesNotExist:
        return "Task topilmadi"


@shared_task
def task_statistics():
    total = Task.objects.count()
    pending = Task.objects.filter(status="PENDING").count()
    done = Task.objects.filter(status="DONE").count()
    overdue = Task.objects.filter(status="OVERDUE").count()

    stats = {
        "total": total,
        "pending": pending,
        "done": done,
        "overdue": overdue,
    }

    print(f"📊 Task Stats: {stats}")

    return stats
