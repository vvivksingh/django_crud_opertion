from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('userapi/', views.UserApi.as_view()),
    path('userapi/<int:pk>/', views.UserApi.as_view()),
]