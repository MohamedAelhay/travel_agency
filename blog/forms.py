from django import forms
from django.http import request

from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_Text']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_Text']