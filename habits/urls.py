from django.urls import path
from . import views

app_name = "habits"

urlpatterns = [
    path("", views.habit_list, name="habit_list"),
    path("<int:habit_id>/", views.habit_detail, name="habit_detail"),
    path("<int:habit_id>/log/", views.log_habit, name="log_habit"),
]
