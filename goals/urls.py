from django.urls import path
from .views import (
    goal_list, goal_detail, goal_create, goal_update, goal_delete,
    milestone_create, milestone_update, milestone_delete
)

app_name = "goals"

urlpatterns = [
    path("", goal_list, name="goal_list"),
    path("<int:pk>/", goal_detail, name="goal_detail"),
    path("create/", goal_create, name="goal_create"),
    path("<int:pk>/update/", goal_update, name="goal_update"),
    path("<int:pk>/delete/", goal_delete, name="goal_delete"),
    path("<int:goal_id>/milestone/create/", milestone_create, name="milestone_create"),
    path("milestone/<int:pk>/update/", milestone_update, name="milestone_update"),
    path("milestone/<int:pk>/delete/", milestone_delete, name="milestone_delete"),
]
