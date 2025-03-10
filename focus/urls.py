from django.urls import path
from .views import focus_create, focus_delete, focus_detail, focus_update, start_focus_session, end_focus_session, focus_sessions_list

app_name = "focus"

urlpatterns = [
    path("start/<int:task_id>/", start_focus_session, name="start_focus"),
    path("end/<int:session_id>/", end_focus_session, name="end_focus"),
    path("sessions/", focus_sessions_list, name="focus_sessions_list"),
    path("<int:pk>/", focus_detail, name="focus_detail"),
    path("new/", focus_create, name="focus_create"),
    path("<int:pk>/edit/", focus_update, name="focus_update"),
    path("<int:pk>/delete/", focus_delete, name="focus_delete"),
]
