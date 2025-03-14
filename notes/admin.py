from django.contrib import admin
from .models import Note

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created_at", "goal", "milestone", "task")
    search_fields = ("title", "content")
    list_filter = ("goal", "milestone", "task")
