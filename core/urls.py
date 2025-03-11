from django.contrib import admin
from django.urls import include, path
from two_factor.urls import urlpatterns as tf_urls
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("accounts/", include("accounts.urls", namespace="accounts")),
    path("2fa/", include(tf_urls, namespace="two_factor")),
    path("", include("landing.urls", namespace="landing")),
    path("goals/", include("goals.urls", namespace="goals")),
    path("tasks/", include("task.urls", namespace="task")),
    path("focus/", include("focus.urls", namespace="focus")),
    path("notes/", include("notes.urls", namespace="notes")),
    path("mindmaps/", include("mindmaps.urls", namespace="mindmaps")),
    path("habits/", include("habits.urls", namespace="habits")),
    path("reports/", include("reports.urls", namespace="reports")),
    path("dashboard/", include("dashboard.urls", namespace="dashboard")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
