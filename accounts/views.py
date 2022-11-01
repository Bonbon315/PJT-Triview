from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserChangeForm, User
from django.http import Http404

# Create your views here.
# 회원가입
def signup(request):
    if request.method == "POST":
        form = User(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = User()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)


# 로그인
def log_in(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                login(request, form.get_user())
                return redirect(request.GET.get("next") or "index")
        else:
            form = AuthenticationForm()
        context = {"form": form}
        return render(request, "accounts/login.html", context)
    else:
        return redirect("index")


# 로그아웃
@login_required
def log_out(request):
    logout(request)
    return redirect("index")
