from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_profile, name='my_profile'),
    path('about/', views.about_business, name='my_business'),
]