from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
# 유저모델 생성
class User(AbstractUser):
    followings = models.ManyToManyField(
        "self", symmetrical=False, related_name="follower"
    )
