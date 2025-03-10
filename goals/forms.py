from django import forms
from .models import Goal, Milestone

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title', 'description', 'due_date', 'category', 'status']

class MilestoneForm(forms.ModelForm):
    class Meta:
        model = Milestone
        fields = ['goal', 'title', 'due_date', 'status']
