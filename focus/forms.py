from django import forms
from .models import FocusSession

class FocusSessionForm(forms.ModelForm):
    class Meta:
        model = FocusSession
        fields = ["task", "end_time", "duration", "completed"]
        widgets = {
            "end_time": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "duration": forms.NumberInput(attrs={"min": 1}),
        }
