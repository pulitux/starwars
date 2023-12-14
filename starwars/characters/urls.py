from django.urls import path
from characters import views

urlpatterns = [
    path('all', views.all, name='all'),
]