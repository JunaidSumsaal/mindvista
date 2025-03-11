from django import forms
from .models import Goal, Milestone

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['title', 'description', 'due_date', 'category', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'block border w-full mb-4 rounded-md py-1.5 pr-3 pl-1 text-base text-gray-900 placeholder:text-gray-400 focus:outline-none sm:text-sm/6',
                'placeholder': 'Create goal title',
            }),
            'description': forms.Textarea(attrs={
                'class': 'block border w-full mb-4 rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-[#65a30d] sm:text-sm/6',
                'rows': 4,
                'placeholder': 'Provide a description for your goal',
            }),
            'due_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'block w-full mb-4 border rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 focus:outline-2 focus:-outline-offset-2 focus:outline-[#65a30d] sm:text-sm/6',
            }),
            'category': forms.Select(attrs={
                'class': 'block w-full mb-4 border rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 focus:outline-2 focus:-outline-offset-2 focus:outline-[#65a30d] sm:text-sm/6',
            }),
        }

    status = forms.ChoiceField(
        choices=[
            ('pending', 'Pending'),
            ('in_progress', 'In Progress'),
            ('completed', 'Completed'),
        ],
        widget=forms.RadioSelect(attrs={'class': 'form-radio'}),
    )


class MilestoneForm(forms.ModelForm):
    class Meta:
        model = Milestone
        fields = ['goal', 'title', 'due_date', 'status']
        widgets = {
            'goal': forms.Select(attrs={
                'class': 'block w-full border rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 focus:outline-2 focus:-outline-offset-2 focus:outline-[#65a30d] sm:text-sm/6',
            }),
            'title': forms.TextInput(attrs={
                'class': 'block min-w-0 grow py-1.5 pr-3 pl-1 text-base text-gray-900 placeholder:text-gray-400 focus:outline-none sm:text-sm/6',
                'placeholder': 'Milestone title',
            }),
            'due_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'block w-full border rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 focus:outline-2 focus:-outline-offset-2 focus:outline-[#65a30d] sm:text-sm/6',
            }),
        }

    status = forms.ChoiceField(
        choices=[
            ('pending', 'Pending'),
            ('in_progress', 'In Progress'),
            ('completed', 'Completed'),
        ],
        widget=forms.RadioSelect(attrs={'class': 'form-radio'}),
    )
