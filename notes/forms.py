from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content", "goal", "task", "milestone"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "block w-full p-2.5 text-sm border border-gray-300 rounded-lg focus:ring-primary-600 focus:border-primary-600 dark:bg-gray-700 dark:border-gray-600 dark:text-white",
                "placeholder": "Enter note title"
            }),
            "content": forms.Textarea(attrs={
                "class": "block w-full p-2.5 text-sm border border-gray-300 rounded-lg focus:ring-primary-600 focus:border-primary-600 dark:bg-gray-700 dark:border-gray-600 dark:text-white",
                "placeholder": "Write your note..."
            }),
            "goal": forms.Select(attrs={
                "class": "block w-full p-2.5 text-sm border border-gray-300 rounded-lg focus:ring-primary-600 focus:border-primary-600 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
            }),
            "task": forms.Select(attrs={
                "class": "block w-full p-2.5 text-sm border border-gray-300 rounded-lg focus:ring-primary-600 focus:border-primary-600 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
            }),
            "milestone": forms.Select(attrs={
                "class": "block w-full p-2.5 text-sm border border-gray-300 rounded-lg focus:ring-primary-600 focus:border-primary-600 dark:bg-gray-700 dark:border-gray-600 dark:text-white"
            }),
        }
