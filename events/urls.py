# events/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar_view, name='calendar_view'),
    path('add/', views.add_event, name='add_event'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('<int:event_id>/edit/', views.edit_event, name='edit_event'), 
    path('<int:event_id>/delete/', views.delete_event, name='delete_event'),
]
