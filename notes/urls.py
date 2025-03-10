from django.urls import path
from .views import notes_list, add_note, edit_note, delete_note

app_name = "notes"

urlpatterns = [
    path("", notes_list, name="notes_list"),
    path("add/", add_note, name="add_note"),
    path("edit/<int:note_id>/", edit_note, name="edit_note"),
    path("delete/<int:note_id>/", delete_note, name="delete_note"),
]
