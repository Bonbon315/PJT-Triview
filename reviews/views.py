from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review
from location.models import Location
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

# 여행지-리뷰페이지
def index(request, location_pk):
    location = Location.objects.get(id=location_pk)
    reviews = Review.objects.all()
    grade = 0
    cnt = 0
    for review in reviews:
        if review.location == location:
            grade += review.grade
            cnt += 1
    if grade:
        grade /= cnt
    context = {
        "reviews": reviews,
        "location": location,
        "location_grade": grade,
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

# 여행자 리뷰 수정
@login_required
def update(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == "POST":
        # POST : input 값 가져와서, 검증하고, DB에 저장
        review_form = ReviewForm(request.POST, request.FILES, instance=review)
        if review_form.is_valid():
            # 유효성 검사 통과하면 저장하고, 여행리뷰 페이지로
            review_form.save()
            messages.success(request, "리뷰가 수정되었습니다.")
            return redirect("reviews:index", review.location.id)
        # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 review_form을 랜더링
    else:
        # GET : Form을 제공
        review_form = ReviewForm(instance=review)
    context = {"review_form": review_form}
    return render(request, "reviews/update.html", context)


# 여행자 리뷰 삭제
@login_required
def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)  # 어떤 글인지
    review.delete()
    return redirect('reviews:index', review.location.id)

