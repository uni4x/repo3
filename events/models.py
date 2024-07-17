# events/models.py

from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateField()  # DateTimeField から DateField へ変更
    end_time = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.title
    def __str__(self):
        return f'Comment by {self.created_by} on {self.title}'