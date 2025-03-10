from django.db import models
from django.conf import settings
from django.utils.timezone import now
from goals.models import Goal
from task.models import Task


class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="habits")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    goal = models.ForeignKey(Goal, on_delete=models.SET_NULL, null=True, blank=True, related_name="habits")
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, blank=True, related_name="habits")
    frequency = models.CharField(
        max_length=20,
        choices=[("daily", "Daily"), ("weekly", "Weekly"), ("custom", "Custom")],
        default="daily"
    )
    streak = models.PositiveIntegerField(default=0)
    last_completed = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    def update_streak(self):
        today = now().date()
        if self.last_completed == today:
            return
        if self.last_completed and (today - self.last_completed).days == 1:
            self.streak += 1
        else:
            self.streak = 1
        self.last_completed = today
        self.save()


class HabitLog(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name="logs")
    date = models.DateField(default=now)

    class Meta:
        unique_together = ("habit", "date")

    def __str__(self):
        return f"{self.habit.name} - {self.date}"
