from django.db import models
from task.models import Task
from django.conf import settings

class FocusSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="focus_sessions")
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="focus_sessions")
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    duration = models.PositiveIntegerField(help_text="Duration in minutes", default=0)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Focus Session for {self.task.title} by {self.user.username}"

    class Meta:
        ordering = ["-start_time"]
