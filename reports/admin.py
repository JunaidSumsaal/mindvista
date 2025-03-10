from django.contrib import admin
from .models import WeeklyReport

@admin.register(WeeklyReport)
class WeeklyReportAdmin(admin.ModelAdmin):
    list_display = ("user", "start_date", "end_date", "total_focus_time", "completed_tasks", "habit_completions")
