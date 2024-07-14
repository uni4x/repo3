# comments/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Comment
from .forms import CommentForm
from events.models import Event

@login_required
def add_comment(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.event = event
            comment.created_by = request.user
            comment.save()
            return redirect('calendar_view')
    else:
        form = CommentForm()
    return render(request, 'comments/add_comment.html', {'form': form, 'event': event})