from django.urls import path
from . import views

app_name = "reports"

urlpatterns = [
    path("weekly/", views.weekly_report, name="weekly_report"),
]
