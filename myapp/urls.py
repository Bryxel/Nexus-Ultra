from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('snippets/', views.snippets, name='snippets'),
    path('snippets/<int:pk>/edit/', views.edit_snippet, name='edit_snippet'),
    path('snippets/<int:pk>/delete/', views.delete_snippet, name='delete_snippet'),
    path('snippets/<int:pk>/detail/', views.snippet_detail, name='snippet_detail'),
]