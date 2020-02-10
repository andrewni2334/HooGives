from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('api/v1/users/', views.user_api),
    path('api/v1/users/create/', views.user_create_api),
    path('api/v1/users/delete/', views.user_delete_api),
    path('api/v1/events/', views.event_api),



]