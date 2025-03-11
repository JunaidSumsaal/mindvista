from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "goal", "milestone", "due_date", "priority", "status"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-primary-600 focus:border-primary-600 text-gray-900",
                "placeholder": "Enter task title"
            }),
            "description": forms.Textarea(attrs={
                "class": "block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-primary-600 focus:border-primary-600 text-gray-900",
                "placeholder": "Task description",
                "rows": 4
            }),
            "goal": forms.Select(attrs={
                "class": "block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-primary-600 focus:border-primary-600 text-gray-900",
            }),
            "milestone": forms.Select(attrs={
                "class": "block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-primary-600 focus:border-primary-600 text-gray-900",
            }),
            "due_date": forms.DateInput(attrs={
                "type": "date",
                "class": "block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-primary-600 focus:border-primary-600 text-gray-900",
            }),
            "priority": forms.Select(attrs={
                "class": "block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-primary-600 focus:border-primary-600 text-gray-900",
            }),
            "status": forms.Select(attrs={
                "class": "block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-primary-600 focus:border-primary-600 text-gray-900",
            }),
        }
