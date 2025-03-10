from django.urls import path
from .views import disable_2fa, enable_email_otp, enforce_admin_2fa, profile_settings, register, user_login, user_logout, profile_update, verify_email_otp
from two_factor.views import SetupView, BackupTokensView
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("profile/", profile_settings, name="profile_settings"),
    path("profile/update/", profile_update, name="profile_update"),
    path("setup/", SetupView.as_view(), name="2fa_setup"),
    path("backup_tokens/", BackupTokensView.as_view(), name="2fa_backup_tokens"),
    path("email/", enable_email_otp, name="enable_email_otp"),
    path("email/verify/", verify_email_otp, name="verify_email_otp"),
    path("disable/", disable_2fa, name="disable_2fa"),
    path("admin/2fa-check/", enforce_admin_2fa, name="enforce_admin_2fa"),
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"), name="password_reset_complete"),
    path("password_change/", auth_views.PasswordChangeView.as_view(template_name="accounts/password_change.html"), name="password_change"),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(template_name="accounts/password_change_done.html"), name="password_change_done"),
]
