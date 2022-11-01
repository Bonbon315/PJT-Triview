from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review
from location.models import Location
from django.contrib.auth.decorators import login_required

# Create your views here.

# 여행지-리뷰페이지
def index(request, location_pk):
    location = Location.objects.get(id=location_pk)
    reviews = Review.objects.all()
    context = {
        "reviews": reviews,
        "location": location,
    }
    return render(request, "reviews/index.html", context)


# 여행지-리뷰작성
@login_required
def create(request, location_pk):
    location = Location.objects.get(id=location_pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.location = location
            review.user = request.user
            review.save()
            return redirect("reviews:index", location.pk)
    else:
        review_form = ReviewForm()
    context = {
        "review_form": review_form,
    }

    return render(request, "reviews/create.html", context)


@login_required
def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect("reviews:detail", pk)
    else:
        review_form = ReviewForm(instance=review)
    context = {
        "review_form": review_form,
        "review": review,
    }
    return render(request, "reviews/update.html", context)
