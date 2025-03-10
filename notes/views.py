from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Note
from goals.models import Goal, Milestone
from task.models import Task
from .forms import NoteForm

@login_required
def notes_list(request):
    """List all notes for the user."""
    notes = Note.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "notes/notes_list.html", {"notes": notes})

@login_required
def add_note(request):
    """Create a new note."""
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect("notes:notes_list")
    else:
        form = NoteForm()
    
    return render(request, "notes/note_form.html", {"form": form})

@login_required
def edit_note(request, note_id):
    """Edit an existing note."""
    note = get_object_or_404(Note, id=note_id, user=request.user)
    
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("notes:notes_list")
    else:
        form = NoteForm(instance=note)
    
    return render(request, "notes/note_form.html", {"form": form})

@login_required
def delete_note(request, note_id):
    """Delete a note."""
    note = get_object_or_404(Note, id=note_id, user=request.user)
    if request.method == "POST":
        note.delete()
        return redirect("notes:notes_list")
    
    return render(request, "notes/note_confirm_delete.html", {"note": note})
