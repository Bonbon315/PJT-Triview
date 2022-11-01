from random import choices
from django.db import models
from imagekit.models import ProcessedImageField
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

CATEGORY_CHOICES = (
    ("tour", "관광지"),
    ("restaurant", "음식점"),
    ("hotel", "숙소"),
)


class Location(models.Model):
    title = models.CharField(max_length=80)
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        format="JPEG",
        options={"quality": 80},
    )
    country = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    grade = models.IntegerField(
        default=3,
        validators=[MaxValueValidator(5), MinValueValidator(1)],
        verbose_name="평점",
    )
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default="관광지")
