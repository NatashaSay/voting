from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name = 'home'),
    path('profile/', views.profile, name = 'profile'),
    path('editprofile/', views.editprofile, name = 'editprofile'),
]