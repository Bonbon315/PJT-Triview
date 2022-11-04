from random import choices
from django.db import models
from imagekit.models import ProcessedImageField
from django.conf import settings

# Create your models here.

CATEGORY_CHOICES = (
    ("관광지", "관광지"),
    ("음식점", "음식점"),
    ("숙소", "숙소"),
)


class Location(models.Model):
    title = models.CharField(max_length=80, verbose_name="이름")
    image = ProcessedImageField(
        upload_to="images/",
        blank=False,
        format="JPEG",
        options={"quality": 80},
        verbose_name="대표이미지",
    )
    country = models.CharField(max_length=80, verbose_name="국가")
    city = models.CharField(max_length=80, verbose_name="도시")
    category = models.CharField(
        max_length=10, choices=CATEGORY_CHOICES, default="관광지", verbose_name="카테고리"
    )
    lat = models.CharField(max_length=80, verbose_name="위도")
    lng = models.CharField(max_length=80, verbose_name="경도")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    desc = models.TextField(max_length=300, blank=True, verbose_name="장소 설명문")
