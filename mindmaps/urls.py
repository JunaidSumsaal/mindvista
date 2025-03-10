from django.urls import path
from . import views

app_name = "mindmaps"

urlpatterns = [
    path("", views.mindmap_list, name="mindmap_list"),
    path("<int:mindmap_id>/", views.mindmap_detail, name="mindmap_detail"),
    path("create/", views.create_mindmap, name="create_mindmap"),
    path("<int:mindmap_id>/add_node/", views.add_node, name="add_node"),
    path("update_node_position/", views.update_node_position, name="update_node_position"),
]
