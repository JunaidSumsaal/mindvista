from django import forms
from .models import MindMap, Node

class MindMapForm(forms.ModelForm):
    class Meta:
        model = MindMap
        fields = ["title"]

class NodeForm(forms.ModelForm):
    class Meta:
        model = Node
        fields = ["content", "parent"]
