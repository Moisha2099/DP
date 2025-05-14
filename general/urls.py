from django.contrib import admin
from django.urls import path, include
from general.views import index, logout_view, register, profile, admin_panel
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', index, name='index'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/admin_panel/', admin_panel, name='admin_panel'),
]
