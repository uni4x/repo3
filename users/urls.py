# users/urls.py

from django.urls import path
from .views import signup, update_color, CustomLoginView

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('update_color/', update_color, name='update_color'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
