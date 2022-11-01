from django.shortcuts import render, redirect
from .forms import LocationForm
from .models import Location

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
