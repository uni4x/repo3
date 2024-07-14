# users/models.py

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    color = models.CharField(max_length=7, default='#a8a8a8')

    def __str__(self):
        return self.user.username