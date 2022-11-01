from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.log_in, name="login"),
    path("logout/", views.log_out, name="logout"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("update/", views.update, name="update"),
    path("<int:pk>/follow/", views.follow, name="follow"),
]
