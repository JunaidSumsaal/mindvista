from django.shortcuts import redirect
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.plugins.otp_email.models import EmailDevice

class EnforceAdmin2FAMiddleware:
    """Middleware to enforce 2FA for admin users."""
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.user.is_staff:
            has_totp = TOTPDevice.objects.filter(user=request.user, confirmed=True).exists()
            has_email_otp = EmailDevice.objects.filter(user=request.user, confirmed=True).exists()

            if (
                not has_totp
                and not has_email_otp
                and request.path.startswith("/admin/")
            ):
                return redirect("2fa_setup")

        return self.get_response(request)
