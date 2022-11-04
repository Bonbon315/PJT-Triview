from django.urls import path
from . import views

app_name = "location"

urlpatterns = [
    path("create/", views.create, name="create"),
    path("", views.index, name="index"),
    path("update/<location_pk>", views.update, name="update"),
    path("delete/<location_pk>", views.delete, name="delete"),
]
