from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.http import JsonResponse
from .forms import FocusSessionForm
from .models import FocusSession
from task.models import Task

@login_required
def start_focus_session(request, task_id):
    """Start a new focus session for a given task."""
    task = get_object_or_404(Task, id=task_id, user=request.user)
    
    active_session = FocusSession.objects.filter(user=request.user, task=task, completed=False).first()
    if active_session:
        return JsonResponse({"error": "You already have an active session for this task."}, status=400)
    
    focus_session = FocusSession.objects.create(user=request.user, task=task, start_time=now())
    return JsonResponse({"message": "Focus session started.", "session_id": focus_session.id})

@login_required
def end_focus_session(request, session_id):
    """End an active focus session and calculate duration."""
    session = get_object_or_404(FocusSession, id=session_id, user=request.user, completed=False)
    
    session.end_time = now()
    session.duration = int((session.end_time - session.start_time).total_seconds() / 60)
    session.completed = True
    session.save()
    
    return JsonResponse({"message": "Focus session ended.", "duration": session.duration})

@login_required
def focus_sessions_list(request):
    """View all completed focus sessions."""
    sessions = FocusSession.objects.filter(user=request.user).order_by("-start_time")
    return render(request, "focus/focus_sessions_list.html", {"sessions": sessions})

@login_required
def focus_detail(request, pk):
    focus_session = get_object_or_404(FocusSession, pk=pk, user=request.user)
    return render(request, "focus/focus_detail.html", {"focus_session": focus_session})

@login_required
def focus_create(request):
    if request.method == "POST":
        form = FocusSessionForm(request.POST)
        if form.is_valid():
            focus_session = form.save(commit=False)
            focus_session.user = request.user
            focus_session.save()
            return redirect("focus:focus_sessions_list")
    else:
        form = FocusSessionForm()

    return render(request, "focus/focus_form.html", {"form": form})

@login_required
def focus_update(request, pk):
    focus_session = get_object_or_404(FocusSession, pk=pk, user=request.user)

    if request.method == "POST":
        form = FocusSessionForm(request.POST, instance=focus_session)
        if form.is_valid():
            form.save()
            return redirect("focus:focus_detail", pk=focus_session.pk)
    else:
        form = FocusSessionForm(instance=focus_session)

    return render(request, "focus/focus_form.html", {"form": form})


@login_required
def focus_delete(request, pk):
    focus_session = get_object_or_404(FocusSession, pk=pk, user=request.user)

    if request.method == "POST":
        focus_session.delete()
        return redirect("focus:focus_sessions_list")

    return render(request, "focus/focus_confirm_delete.html", {"focus_session": focus_session})

