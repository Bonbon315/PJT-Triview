from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
# 유저모델 생성
class User(AbstractUser):
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="follower"
    )
    profile_image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        format="JPEG",
        options={"quality": 80},
        processors=[ResizeToFill(150, 150)],
    )
