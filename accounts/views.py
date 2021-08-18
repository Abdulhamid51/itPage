from main.models import Post
from accounts.forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.views.generic import (
    View, UpdateView, DetailView,
)
from .models import *
from main.models import *
from .forms import *

# Create your views here.

class RegisterView(View):

    def get(self, request):
        form = RegisterForm(request.GET)
        context = {'form':form}
        return render(request, 'accounts/register.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            print('@'*50)
            u = form.save()
            try:
                user = UserProfile.objects.create(
                    user=u,
                    slug=u.username,
                    name=u.first_name,
                    surname=u.last_name)
                user.save()
            except:
                user = None
            return redirect('/accounts/auth/login')

        else:
            print('#'*50)
            form = RegisterForm()

        context = {'form':form}
        return render(request, 'accounts/register.html', context)


def profile(request, slug):
    user = UserProfile.objects.get(slug=slug)
    posts = Post.objects.filter(user=user.user).order_by('-id')
    blogs = Blog.objects.filter(user=user.user).order_by('-id')
    context = {
        'user':user,
        'posts':posts,
        'blogs':blogs
    }
    return render(request, 'accounts/profile.html',context)

def createprofile(request):
    user = UserProfile.objects.create(
        user=request.user,
        name=request.user.first_name,
        surname=request.user.last_name,
        slug=request.user.username,
    )
    user.save()
    return redirect('/')

def follow(request, slug):
    path = request.path
    user = UserProfile.objects.get(slug=slug)

    if request.user not in user.follows.all():
        user.follows.add(request.user)
        user.save()
        return redirect(path.replace('follow/',''))

    else:
        user.follows.remove(request.user)
        user.save()
        return redirect('/')



class ProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = UpdateProfileForm
    success_url = '/'
    template_name = "accounts/update_pro.html"
