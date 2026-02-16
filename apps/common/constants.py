# Roles
ROLE_SUPER_ADMIN = "SUPER_ADMIN"
ROLE_COMPANY_ADMIN = "COMPANY_ADMIN"
ROLE_MANAGER = "MANAGER"
ROLE_OPERATOR = "OPERATOR"

USER_ROLES = [
    (ROLE_SUPER_ADMIN, "Super Admin"),
    (ROLE_COMPANY_ADMIN, "Company Admin"),
    (ROLE_MANAGER, "Manager"),
    (ROLE_OPERATOR, "Operator"),
]

# Lead sources
LEAD_WEBSITE = "WEBSITE"
LEAD_TELEGRAM = "TELEGRAM"
LEAD_FACEBOOK = "FACEBOOK"
LEAD_API = "API"

LEAD_SOURCES = [
    (LEAD_WEBSITE, "Website"),
    (LEAD_TELEGRAM, "Telegram"),
    (LEAD_FACEBOOK, "Facebook"),
    (LEAD_API, "API"),
]

# Task status
TASK_PENDING = "PENDING"
TASK_DONE = "DONE"
TASK_OVERDUE = "OVERDUE"

TASK_STATUS_CHOICES = [
    (TASK_PENDING, "Pending"),
    (TASK_DONE, "Done"),
    (TASK_OVERDUE, "Overdue"),
]
