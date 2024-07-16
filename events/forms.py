# events/forms.py

from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'start_time', 'end_time']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'start_time': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_time': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }