from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserChangeForm, User

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = User(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("templats/index.html")
    else:
        form = User()
    context = {"form": form}
    return render(request, "accounts/signup.html", context)
