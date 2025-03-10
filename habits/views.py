from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from .models import Habit, HabitLog

@login_required
def habit_list(request):
    habits = Habit.objects.filter(user=request.user)
    return render(request, "habits/habit_list.html", {"habits": habits})

@login_required
def habit_detail(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    logs = habit.logs.order_by("-date")[:7]
    return render(request, "habits/habit_detail.html", {"habit": habit, "logs": logs})

@login_required
def log_habit(request, habit_id):
    """
    Marks a habit as completed for today and updates streak.
    """
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    today = now().date()

    if not HabitLog.objects.filter(habit=habit, date=today).exists():
        HabitLog.objects.create(habit=habit, date=today)
        habit.update_streak()

    return redirect("habits:habit_list")
