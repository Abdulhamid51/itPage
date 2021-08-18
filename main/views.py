from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import (
    View, UpdateView, DetailView, ListView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
from accounts.models import UserProfile
import rstr

slug_random = 'abdcfghijklmnopqrstuvwxyzABCDFGHIJKLMNOPQRSTUVWXYZ1234567890'

# Create your views here.

class HomeView(LoginRequiredMixin, View):
    
    def get(self, request):
        post = UserProfile.objects.all()
        recent = UserProfile.objects.all().order_by('?')[:8]
        context = {
            'post':post,
            'recent':recent}
        return render(request, 'index.html', context)


class PostsView(LoginRequiredMixin, ListView):
    model = Post
    ordering = '?'
    paginate_by = 9
    template_name = 'posts.html'


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title','tags','body']
    template_name = "update_post.html"


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title','category','image','body']
    template_name = "update_blog.html"


class BlogsView(LoginRequiredMixin, ListView):
    model = Blog
    ordering = '?'
    paginate_by = 6
    template_name = 'blogs.html'


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    form = AddPostComment(request.GET)
    if request.method == 'POST':
        form = AddPostComment(request.POST)
        comment = form.save()
        user = request.user
        com = PostComment.objects.create(
            user=user,
            comment=comment.comment,
        )
        com.post = post
        com.save()
    context = {
        'post':post,
        'form':form
    }
    return render(request, 'post_detail.html', context)

def blog_detail(request, slug):
    post = Blog.objects.get(slug=slug)
    context = {
        'post':post,
    }
    return render(request, 'blog_detail.html', context)


class AddPostView(LoginRequiredMixin, View):

    def get(self, request):
        form = AddPostForm(request.GET)
        context = {
            'form':form,
        }
        return render(request, 'add_post.html', context)

    def post(self, request):
        if request.method == 'POST':
            form = AddPostForm(request.POST)
            user = request.user
            slug = rstr.rstr(slug_random, 15)
            if form.is_valid():
                newpost = form.save(commit=False)
                newpost.user = user
                newpost.slug = slug
                newpost.save()
                return redirect('/posts/')
            else:
                form = AddPostForm()
        context = {
            'form':form,
        }
        return render(request, 'add_post.html', context)


class AddBlogView(LoginRequiredMixin, View):

    def get(self, request):
        form = AddBlogForm(request.GET)
        context = {
            'form':form,
        }
        return render(request, 'add_blog.html', context)

    def post(self, request):
        if request.method == 'POST':
            form = AddBlogForm(request.POST, request.FILES)
            user = request.user
            slug = rstr.rstr(slug_random, 15)
            if form.is_valid():
                newpost = form.save(commit=False)
                newpost.user = user
                newpost.slug = slug
                newpost.save()
                return redirect('/blogs/')
            else:
                form = AddBlogForm()
        context = {
            'form':form,
        }
        return render(request, 'add_blog.html', context)

def plike(request, slug):
    path = request.path
    post = Post.objects.get(slug=slug)

    if request.user.user_pro not in post.like.all():
        post.like.add(request.user.user_pro)
        post.save()
        return redirect(path.replace('like/',''))

    else:
        post.like.remove(request.user.user_pro)
        post.save()
        return redirect('/posts/')

def blike(request, slug):
    path = request.path
    post = Blog.objects.get(slug=slug)

    if request.user.user_pro not in post.like.all():
        post.like.add(request.user.user_pro)
        post.save()
        return redirect(path.replace('like/',''))

    else:
        post.like.remove(request.user.user_pro)
        post.save()
        return redirect('/blogs/')