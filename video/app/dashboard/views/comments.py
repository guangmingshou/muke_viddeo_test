# coding:utf-8

from django.views.generic import View
from django.shortcuts import redirect, reverse
from app.models import Comment


class Comments(View):

    def get(self, request, comment_id, video_id):
        comment = Comment.objects.get(pk=comment_id)

        comment.status = not comment.status
        comment.save()
        return redirect(reverse('video_sub', kwargs={'video_id': video_id}))


class CommentsDelete(View):

    def get(self, request, comment_id, video_id):

        Comment.objects.filter(id=comment_id).delete()
        return redirect(reverse('video_sub', kwargs={'video_id': video_id}))