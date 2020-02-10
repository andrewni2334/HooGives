from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('api/v1/users/', views.user_api),
    path('api/v1/events/', views.event_api),
    path('api/v1/events/create/', views.event_create_api),
    path('api/v1/events/delete/', views.event_delete_api)
]