from django import forms
from django.forms import fields
from .models import *

class AddPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','tags','body']


class AddBlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ['title','category','image','body']


class AddPostComment(forms.ModelForm):

    class Meta:
        model = PostComment
        fields = ['comment']
        exclude = ['post', 'user']

class AddBlogComment(forms.ModelForm):

    class Meta:
        model = BlogComment
        fields = ['comment']
        