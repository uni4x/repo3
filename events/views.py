# events/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm
from comments.models import Comment
from users.models import UserProfile

@login_required
def calendar_view(request):
    events = Event.objects.all()
    event_list = []
    for event in events:
        color = event.created_by.userprofile.color  # ユーザーの色を取得
        event_list.append({
            'title': event.title,
            'start': event.start_time,
            'end': event.end_time,
            'color': color,
            'url': f"/events/{event.id}/"
        })
    return render(request, 'events/calendar.html', {'events': event_list})

@login_required
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('calendar_view')
    else:
        form = EventForm()
    return render(request, 'events/add_event.html', {'form': form})


@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    comments = Comment.objects.filter(event=event)
    return render(request, 'events/event_detail.html', {'event': event, 'comments': comments})


@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('calendar_view')
    return render(request, 'events/confirm_delete.html', {'event': event})