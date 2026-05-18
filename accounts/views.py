from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes


def login_view(request):
    error_message = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("profile")
        else:
            error_message = "Username ou password inválidos."

    return render(request, "accounts/login.html", {
        "error_message": error_message
    })


def logout_view(request):
    logout(request)
    return redirect("profile")


def register_view(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save()

        group, created = Group.objects.get_or_create(name="autores")
        user.groups.add(group)

        login(request, user)
        return redirect("profile")

    return render(request, "accounts/register.html", {
        "form": form
    })

def magic_link_request(request):
    message = None

    if request.method == "POST":
        email = request.POST.get("email")
        user = User.objects.filter(email=email).first()

        if user:
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)

            link = request.build_absolute_uri(
                f"/accounts/magic-login/{uid}/{token}/"
            )

            send_mail(
                "Magic Login Link",
                f"Clique neste link para entrar: {link}",
                "noreply@example.com",
                [email],
            )

        message = "Se o email existir, foi enviado um link mágico."

    return render(request, "accounts/magic_link_request.html", {
        "message": message
    })


def magic_login(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except Exception:
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        login(request, user)
        return redirect("profile")

    return render(request, "accounts/magic_link_invalid.html")