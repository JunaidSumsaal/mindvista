from django.db import models
from django.contrib.auth import get_user_model
from goals.models import Goal, Milestone
from task.models import Task

User = get_user_model()

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, null=True, blank=True, related_name="notes")
    milestone = models.ForeignKey(Milestone, on_delete=models.CASCADE, null=True, blank=True, related_name="notes")
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True, related_name="notes")

    def __str__(self):
        return self.title
