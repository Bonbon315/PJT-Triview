from django.urls import path
from . import views

app_name = "location"

urlpatterns = [
    path("create/", views.create, name="create"),
    path("", views.index, name="index"),
]
