from django.contrib import admin
from .models import FocusSession

@admin.register(FocusSession)
class FocusSessionAdmin(admin.ModelAdmin):
    list_display = ("user", "task", "start_time", "end_time", "duration", "completed")
    list_filter = ("completed", "start_time")
    search_fields = ("user__username", "task__title")

