from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserChangeForm, User
from django.views.decorators.http import require_POST
from django.http import Http404

# Create your views here.
# 회원가입
def signup(request):
    if request.method == "POST":
        form = User(request.POST, request.FILES)
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


# 프로필 확인
def detail(request, pk):
    context = {
        "user": get_user_model().objects.get(pk=pk),
        "reviews": get_user_model().objects.get(pk=pk).review_set.all(),
    }
    return render(request, "accounts/detail.html", context)


# 유저 정보 변경
@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:detail", request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {"form": form}
    return render(request, "accounts/update.html", context)


# 팔로우 기능
@login_required
def follow(request, pk):
    if request.user != get_user_model().objects.get(pk=pk):
        if request.user not in get_user_model().objects.get(pk=pk).follower.all():
            request.user.followings.add(get_user_model().objects.get(pk=pk))
        else:
            request.user.followings.remove(get_user_model().objects.get(pk=pk))

    return redirect("accounts:detail", pk)


# 탈퇴
@login_required
def dropout(request):
    if request.method == "POST":
        request.user.delete()
        logout(request)
        return redirect("location:index")
    else:
        return render(request, "accounts/dropout.html")


# 비번 변경
