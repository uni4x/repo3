# mysite/comments/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
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


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    event = comment.event  # イベントを取得
    comments = Comment.objects.filter(event=event)  # コメントを取得
    if comment.created_by != request.user:
        return render(request, 'events/event_detail.html', {'event': event, 'comments': comments, 'error_message': '他の人の投稿は編集できません'})
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('event_detail', event_id=comment.event.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'comments/edit_comment.html', {'form': form, 'comment': comment})


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    event = comment.event  # イベントを取得
    comments = Comment.objects.filter(event=event)  # コメントを取得
    if comment.created_by != request.user:
        return render(request, 'events/event_detail.html', {'event': event, 'comments': comments, 'error_message': '他の人の投稿は削除できません'})
    if request.method == 'POST':
        event_id = comment.event.id
        comment.delete()
        return redirect('event_detail', event_id=event_id)
    return render(request, 'comments/confirm_delete_comment.html', {'comment': comment})