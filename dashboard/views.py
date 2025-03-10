from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now, timedelta
from task.models import Task
from focus.models import FocusSession
from habits.models import Habit
from reports.models import WeeklyReport

@login_required
def dashboard(request):
    """
    Displays an overview of the user's tasks, focus sessions, habits, and reports.
    """
    today = now().date()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    tasks = Task.objects.filter(user=request.user, status__in=["pending", "in_progress"]).order_by("due_date")[:5]
    focus_sessions = FocusSession.objects.filter(user=request.user).order_by("-start_time")[:5]
    habits = Habit.objects.filter(user=request.user).order_by("-id")[:5]

    report = WeeklyReport.objects.filter(
        user=request.user, start_date=start_of_week, end_date=end_of_week
    ).first()

    return render(request, "dashboard/index.html", {
        "tasks": tasks,
        "focus_sessions": focus_sessions,
        "habits": habits,
        "report": report,
    })
