# comments/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:event_id>/', views.add_comment, name='add_comment'),
]
