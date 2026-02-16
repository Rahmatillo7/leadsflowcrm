from django.contrib import admin
from .models import Pipeline,PipenlineStage

# Register your models here.

@admin.register(Pipeline)
class PipelineAdmin(admin.ModelAdmin):
    list_display = ('name','company','is_default')

@admin.register(PipenlineStage)
class PipenlineStageAdmin(admin.ModelAdmin):
    list_display = ('name','order',  )
