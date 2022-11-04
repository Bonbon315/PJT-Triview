from django.shortcuts import render, redirect, get_object_or_404
from .forms import LocationForm
from .models import Location
from django.contrib.auth.decorators import login_required

# Create your views here.
def create(request):
    if request.method == "POST":
        location_form = LocationForm(request.POST, request.FILES)
        if location_form.is_valid():
            location = location_form.save(commit=False)
            location.save()
            return redirect("location:index")
    else:
        location_form = LocationForm()
    context = {"location_form": location_form}
    return render(request, "location/create.html", context=context)


def index(request):
    locations = Location.objects.all()
    context = {"locations": locations}
    return render(request, "location/index.html", context)


# 장소 수정
@login_required
def update(request, location_pk):
    location = Location.objects.get(pk=location_pk)
    if request.method == "POST":
        location_form = LocationForm(request.POST, request.FILES, instance=location)
        if location_form.is_valid():
            location_form.save()
            return redirect("reviews:index", location.id)
    else:
        location_form = LocationForm(instance=location)
    context = {"location_form": location_form}
    return render(request, "location/update.html", context)


# 장소 삭제
@login_required
def delete(request, location_pk):
    location = Location.objects.get(pk=location_pk)
    location.delete()
    return redirect("location:index")
