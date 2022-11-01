from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from imagekit.models import ProcessedImageField
from django.conf import settings
# Create your models here.
Companion = (
    ('커플','커플'),
    ('가족', '가족'),
    ('친구','친구'),
    ('비즈니스','비즈니스'),
    ('솔로','솔로'),
)

class Review(models.Model):
  title = models.CharField(max_length=80)
  content = models.TextField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  grade = models.IntegerField(
        default=3,
        validators=[MaxValueValidator(5), MinValueValidator(1)],
        verbose_name="평점",
    )
  image = ProcessedImageField(
        blank=True,
        upload_to="images/",
        format="JPEG",
        options={"quality": 80},
    )
  traveled_at = models.DateTimeField(auto_now=True)
  companion = models.CharField(max_length=6, choices=Companion, default='커플')
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_reviews"
    )