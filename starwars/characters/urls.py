from django.urls import path
from characters import views

urlpatterns = [
    path('all', views.all, name='all'),
    path('inplanet/', views.inplanet, name='inplanet')
]