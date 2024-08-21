from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('profile/', views.profile, name='profile'),
    path('contact/', views.contact, name='contact'),
]