from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    is_normaluser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to='profilePic/',default='profilePic/default.jpg')
    date_joined = models.DateTimeField(auto_now = True)
    last_login = models.DateTimeField(default=timezone.now)

    



