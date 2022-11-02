from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
  path("<int:location_pk>/", views.index, name='index'),
  path("<int:location_pk>/create/", views.create, name="create"),
  path("update/<int:review_pk>/", views.update, name="update"),
  path("delete/<int:review_pk>/", views.delete, name="delete"),
  path('like/<int:review_pk>/', views.like, name='like'),
]
