from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.

class User(AbstractUser):
    ROLES=(('User', 0),('Admin', 1), ('Staff', 2))
    role = models.CharField(choices=ROLES, max_length=1)
    email = models.EmailField(max_length=50, unique=True, verbose_name='Your Email')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'password')


class Profile(models.Model):
    GENDER = (('male', 0), ('Female', 1), ('Other', 2))
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER, max_length=1)
    address = models.CharField(max_length=50)
    dob = models.DateField(null=True)