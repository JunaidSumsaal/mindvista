from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class MindMap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mindmaps")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Node(models.Model):
    mindmap = models.ForeignKey(MindMap, on_delete=models.CASCADE, related_name="nodes")
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    position_x = models.FloatField(default=0.0)
    position_y = models.FloatField(default=0.0)

    def __str__(self):
        return self.title
