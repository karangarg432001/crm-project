from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('dashboard', views.dashboard),
    path('detail', views.detail),
    path('customer', views.customer),
]
