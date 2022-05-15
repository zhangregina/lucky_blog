from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from main import settings


class User(AbstractUser):
    is_bloger = models.BooleanField(default=False)
    is_reader = models.BooleanField(default=False)

    def __str__(self):
        return self.username


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Bloger(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='bloger')
    phone = models.CharField(max_length=15, null=True, blank=True)
    skills = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    portfolio = models.CharField(max_length=200, null=True, blank=True)
    blog_name = models.CharField(max_length=80)

    def __str__(self):
        return self.user.username


class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='reader')
    phone = models.CharField(max_length=15, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.user.username
