from random import choices
from django.db import models
from imagekit.models import ProcessedImageField
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

CATEGORY_CHOICES = (
    ("관광지", "관광지"),
    ("음식점", "음식점"),
    ("숙소", "숙소"),
)


class Location(models.Model):
    title = models.CharField(max_length=80)
    image = ProcessedImageField(
        upload_to="images/",
        blank=False,
        format="JPEG",
        options={"quality": 80},
    )
    country = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default="관광지")
