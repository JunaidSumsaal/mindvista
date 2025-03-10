from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import MindMap, Node
from .utils import get_mindmap_structure, create_node
from .forms import MindMapForm, NodeForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@login_required
def mindmap_list(request):
    """
    Display all mind maps for the logged-in user.
    """
    mindmaps = MindMap.objects.filter(user=request.user)
    return render(request, "mindmaps/mindmap_list.html", {"mindmaps": mindmaps})


@login_required
def mindmap_detail(request, mindmap_id):
    """
    Display a single mind map with its nodes.
    """
    mindmap = get_object_or_404(MindMap, id=mindmap_id, user=request.user)
    nodes = get_mindmap_structure(mindmap)
    return render(request, "mindmaps/mindmap_detail.html", {"mindmap": mindmap, "nodes": nodes})


@login_required
def create_mindmap(request):
    """
    Create a new mind map.
    """
    if request.method == "POST":
        form = MindMapForm(request.POST)
        if form.is_valid():
            mindmap = form.save(commit=False)
            mindmap.user = request.user
            mindmap.save()
            return redirect("mindmaps:mindmap_list")
    else:
        form = MindMapForm()

    return render(request, "mindmaps/mindmap_form.html", {"form": form})


@login_required
def add_node(request, mindmap_id):
    """
    Add a new node to a mind map.
    """
    mindmap = get_object_or_404(MindMap, id=mindmap_id, user=request.user)

    if request.method == "POST":
        form = NodeForm(request.POST)
        if form.is_valid():
            parent = form.cleaned_data.get("parent")
            create_node(mindmap, form.cleaned_data["content"], parent)
            return redirect("mindmaps:mindmap_detail", mindmap_id=mindmap.id)
    else:
        form = NodeForm()

    return render(request, "mindmaps/node_form.html", {"form": form, "mindmap": mindmap})


@csrf_exempt
def update_node_position(request):
    """
    API to update node position via drag-and-drop.
    """
    if request.method == "POST":
        data = json.loads(request.body)
        node_id = data.get("node_id")
        new_x = data.get("position_x")
        new_y = data.get("position_y")

        node = Node.objects.filter(id=node_id).first()
        if node:
            node.position_x = new_x
            node.position_y = new_y
            node.save()
            return JsonResponse({"success": True})

    return JsonResponse({"success": False}, status=400)
