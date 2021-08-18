from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.urls import reverse

# Create your models here.
# Tag and Category
class Category(models.Model):
    name = models.CharField("name", max_length=150)
    color = models.CharField("color", max_length=150)
    slug = models.SlugField("*", max_length=150)

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField("name", max_length=150)
    color = models.CharField("color", max_length=150)
    slug = models.SlugField("*", max_length=150)

    def __str__(self):
        return self.name

# Post and its comment
class Post(models.Model):
    user = models.ForeignKey(User, verbose_name="posts", on_delete=models.CASCADE)
    title = models.CharField("title", max_length=550)
    slug = models.SlugField("*")
    tags = models.ManyToManyField(Tags, verbose_name="tags")
    like = models.ManyToManyField(UserProfile, verbose_name="like", blank=True)
    span = models.IntegerField("span", default=0)
    body = RichTextField('body')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:post_detail', kwargs={'slug': self.slug})

class PostComment(models.Model):
    post = models.ForeignKey(Post, related_name="post", on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="p_comment", on_delete=models.CASCADE)
    comment = RichTextField('comment')

    def __str__(self):
        return self.user.username

# Blog and its comment
class Blog(models.Model):
    user = models.ForeignKey(User, verbose_name="blogs", on_delete=models.CASCADE)
    title = models.CharField("title", max_length=350)
    slug = models.SlugField("*")
    image = models.ImageField("image", upload_to='blog_images/')
    category = models.ForeignKey(Category, verbose_name="category", on_delete=models.PROTECT)
    like = models.ManyToManyField(UserProfile, verbose_name="like", blank=True)
    span = models.IntegerField("span", default=0)
    body = RichTextField('body')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('main:blog_detail', kwargs={'slug': self.slug})

class BlogComment(models.Model):
    post = models.ForeignKey(Blog, related_name="blog", on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey(User, verbose_name="b_comment", on_delete=models.CASCADE, blank=True)
    comment = RichTextField('comment')

    def __str__(self):
        return self.user.username
