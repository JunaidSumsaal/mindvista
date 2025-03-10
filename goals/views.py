from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Goal, Milestone
from .forms import GoalForm, MilestoneForm

@login_required
def goal_list(request):
    goals = Goal.objects.filter(user=request.user)
    return render(request, "goals/goal_list.html", {"goals": goals})

@login_required
def goal_detail(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    milestones = goal.milestones.all() 
    return render(request, "goals/goal_detail.html", {"goal": goal, "milestones": milestones})

@login_required
def goal_create(request):
    if request.method == "POST":
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect("goals:goal_list")
    else:
        form = GoalForm()
    return render(request, "goals/goal_form.html", {"form": form})

@login_required
def goal_update(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    if request.method == "POST":
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect("goals:goal_detail", pk=goal.pk)
    else:
        form = GoalForm(instance=goal)
    return render(request, "goals/goal_form.html", {"form": form})

@login_required
def goal_delete(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    if request.method == "POST":
        goal.delete()
        return redirect("goals:goal_list")
    return render(request, "goals/goal_confirm_delete.html", {"goal": goal})

@login_required
def milestone_create(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id, user=request.user)
    if request.method == "POST":
        form = MilestoneForm(request.POST)
        if form.is_valid():
            milestone = form.save(commit=False)
            milestone.goal = goal
            milestone.save()
            return redirect("goals:goal_detail", pk=goal.pk)
    else:
        form = MilestoneForm()
    return render(request, "goals/milestone_form.html", {"form": form, "goal": goal})

@login_required
def milestone_update(request, pk):
    milestone = get_object_or_404(Milestone, pk=pk, goal__user=request.user)
    if request.method == "POST":
        form = MilestoneForm(request.POST, instance=milestone)
        if form.is_valid():
            form.save()
            return redirect("goals:goal_detail", pk=milestone.goal.pk)
    else:
        form = MilestoneForm(instance=milestone)
    return render(request, "goals/milestone_form.html", {"form": form})

@login_required
def milestone_delete(request, pk):
    milestone = get_object_or_404(Milestone, pk=pk, goal__user=request.user)
    if request.method == "POST":
        milestone.delete()
        return redirect("goals:goal_detail", pk=milestone.goal.pk)
    return render(request, "goals/milestone_confirm_delete.html", {"milestone": milestone})
