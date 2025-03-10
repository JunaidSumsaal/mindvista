from django.contrib import admin
from .models import MindMap, Node

@admin.register(MindMap)
class MindMapAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created_at")
    search_fields = ("title", "description")

@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ("title", "mindmap", "parent")
    search_fields = ("title", "content")
    list_filter = ("mindmap",)
