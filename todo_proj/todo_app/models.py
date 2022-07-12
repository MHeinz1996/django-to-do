from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class AppUser(AbstractUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    owner = models.ForeignKey(AppUser, on_delete=models.CASCADE)