from django.contrib import admin
from django.urls import include, path
from two_factor.urls import urlpatterns as tf_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("accounts/", include("accounts.urls")),
    path("2fa/", include(tf_urls, namespace="two_factor")),
    path("", include("landing.urls")),
]
