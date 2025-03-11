from django import forms
from .models import MindMap, Node

class MindMapForm(forms.ModelForm):
    class Meta:
        model = MindMap
        fields = ["title"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "block min-w-0 grow py-1.5 pr-3 pl-1 text-base text-gray-900 placeholder:text-gray-400 focus:outline-none sm:text-sm/6",
                "placeholder": "Enter mind map title",
            }),
        }


class NodeForm(forms.ModelForm):
    class Meta:
        model = Node
        fields = ["content", "parent"]
        widgets = {
            "content": forms.Textarea(attrs={
                "class": "block border w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-primary-600 sm:text-sm/6",
                "rows": 3,
                "placeholder": "Enter node content",
            }),
            "parent": forms.Select(attrs={
                "class": "block w-full border rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 focus:outline-2 focus:-outline-offset-2 focus:outline-primary-600 sm:text-sm/6",
            }),
        }
