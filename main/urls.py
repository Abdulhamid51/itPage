from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    # posts
    path("posts/", PostsView.as_view(), name="posts"),
    path("posts/<slug>", post_detail, name="post_detail"),
    path("posts/like/<slug>", plike, name="like"),
    path("post/add", AddPostView.as_view(), name="add_post"),
    path("update/post/<pk>", PostUpdateView.as_view(), name="update_post"),
    path("delete_post/", delete_post, name="delete_post"),
    # blogs
    path("blogs/", BlogsView.as_view(), name="blogs"),
    path("blogs/<slug>", blog_detail, name="blog_detail"),
    path("blogs/like/<slug>", blike, name="blike"),
    path("blog/add", AddBlogView.as_view(), name="add_blog"),
    path("update/blog/<pk>", BlogUpdateView.as_view(), name="update_blog"),
    path("delete_blog/", delete_blog, name="delete_blog"),
    path("search/", search, name="search"),
]
