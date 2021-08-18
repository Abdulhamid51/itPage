from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

app_name = 'accounts'

urlpatterns = [
    #auth urls
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/login/", LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    #profile urls
    path("<slug>/", profile, name="profile"),
    path("craeteprofile/", createprofile, name="create_pro"),
    path("follow/<slug>", follow, name="follow"),
    path("update/profile/<pk>", ProfileUpdateView.as_view(), name="update_pro")
]
