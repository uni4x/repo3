# comments/models.py

from django.db import models
from django.contrib.auth.models import User
from events.models import Event

class Comment(models.Model):
    event = models.ForeignKey(Event, related_name='comments', on_delete=models.CASCADE)
    comment_text = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment by {self.created_by.username} on {self.event.title}'