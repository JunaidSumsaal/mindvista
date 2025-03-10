from django.contrib.auth.decorators import login_required
from django_otp.plugins.otp_email.models import EmailDevice
from django.core.mail import send_mail
from django.conf import settings
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegistrationForm, LoginForm, UserProfileUpdateForm

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard:dashboard")
    else:
        form = UserRegistrationForm()
    return render(request, "accounts/register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard:dashboard")
    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect("landing:landing")

def profile_update(request):
    if request.method == "POST":
        form = UserProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:profile_settings")
    else:
        form = UserProfileUpdateForm(instance=request.user)
    return render(request, "accounts/profile_update.html", {"form": form})
  

@login_required
def profile_settings(request):
    user = request.user
    totp_device = TOTPDevice.objects.filter(user=user, confirmed=True).exists()
    email_device = EmailDevice.objects.filter(user=user, confirmed=True).exists()
    
    context = {
        "user": user,
        "totp_enabled": totp_device,
        "email_otp_enabled": email_device,
    }
    
    return render(request, "accounts/profile.html", context)


@login_required
def enable_email_otp(request):
    if request.method == "POST":
        device, created = EmailDevice.objects.get_or_create(user=request.user, name="Email OTP")
        if created or not device.confirmed:
            device.generate_challenge()
            return redirect("accounts:verify_email_otp")
    return render(request, "accounts/enable_email_otp.html")

@login_required
def verify_email_otp(request):
    if request.method == "POST":
        token = request.POST.get("token")
        device = EmailDevice.objects.filter(user=request.user).first()
        if device and device.verify_token(token):
            device.confirmed = True
            device.save()
            return redirect("accounts:profile")
    return render(request, "accounts/verify_email_otp.html")

@login_required
def disable_2fa(request):
    """Disable both TOTP and Email OTP for the logged-in user."""
    TOTPDevice.objects.filter(user=request.user).delete()
    EmailDevice.objects.filter(user=request.user).delete()
    return redirect("profile")

@login_required
def enforce_admin_2fa(request):
    """Check if admin user has 2FA enabled, if not redirect to 2FA setup."""
    if request.user.is_staff:
        has_totp = TOTPDevice.objects.filter(user=request.user, confirmed=True).exists()
        has_email_otp = EmailDevice.objects.filter(user=request.user, confirmed=True).exists()
        
        if not (has_totp or has_email_otp):
            return redirect("accounts:2fa_setup")
    
    return redirect("profile")
