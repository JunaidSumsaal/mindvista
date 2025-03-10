from django.db import models
from django.conf import settings
from django.utils import timezone
from habits.models import Habit
from focus.models import FocusSession
from task.models import Task

class WeeklyReport(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="weekly_reports")
    start_date = models.DateField()
    end_date = models.DateField()
    total_focus_time = models.PositiveIntegerField(default=0)
    completed_tasks = models.PositiveIntegerField(default=0)
    habit_completions = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Weekly Report ({self.start_date} - {self.end_date}) for {self.user}"

    def generate_report(self):
        """
        Aggregates data for the given week.
        """
        self.total_focus_time = FocusSession.objects.filter(
            user=self.user, start_time__date__range=[self.start_date, self.end_date]
        ).aggregate(models.Sum("duration"))["duration__sum"] or 0

        self.completed_tasks = Task.objects.filter(
            user=self.user, completed=True, completed_at__date__range=[self.start_date, self.end_date]
        ).count()

        self.habit_completions = Habit.objects.filter(
            user=self.user, logs__date__range=[self.start_date, self.end_date]
        ).count()

        self.save()
