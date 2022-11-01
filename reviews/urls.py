from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
  path("<int:location_pk>/", views.index, name='index'),
  path("<int:location_pk>/create/", views.create, name="create"),
  path("update/<int:pk>", views.update, name="update"),
]
