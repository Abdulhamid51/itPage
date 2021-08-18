from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="user_pro", on_delete=models.CASCADE, blank=True)
    slug = models.SlugField("username", blank=True)
    name = models.CharField("ismi", max_length=150, blank=True)
    avatar = models.ImageField("avatar", upload_to='avatars/', blank=True)
    surname = models.CharField("familyasi", max_length=150, blank=True)
    follows = models.ManyToManyField(User, related_name="follows", blank=True)
    git = models.CharField("github link", max_length=350, blank=True)
    telegram = models.CharField("telegram link", max_length=350, blank=True)

    def __str__(self):
        return self.slug
    
