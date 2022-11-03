from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from imagekit.models import ProcessedImageField
from django.conf import settings
from location import models as location_models
# Create your models here.
# 여행유형 목록
Companion = (
    ('커플','커플'),
    ('가족', '가족'),
    ('친구','친구'),
    ('비즈니스','비즈니스'),
    ('솔로','솔로'),
)

# 여행일자 목록
Month_choices = (
    ('2022-11','2022년 11월'),
    ('2022-10','2022년 10월'),
    ('2022-09','2022년 09월'),
    ('2022-08','2022년 08월'),
    ('2022-07','2022년 07월'),
    ('2022-06','2022년 06월'),
    ('2022-05','2022년 05월'),
    ('2022-04','2022년 04월'),
    ('2022-03','2022년 03월'),
    ('2022-02','2022년 02월'),
    ('2022-01','2022년 01월'),
    ('2021-12','2021년 12월'),
)

# 리뷰 model class
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
  traveled_at = models.CharField(max_length=12, choices=Month_choices, default='2022년 11월')
  companion = models.CharField(max_length=6, choices=Companion, default='가족')
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_reviews"
    )
  location = models.ForeignKey(location_models.Location, on_delete=models.CASCADE)