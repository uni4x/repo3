# users/urls.py

from django.urls import path
from .views import signup, update_color

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('update_color/', update_color, name='update_color'),
]
