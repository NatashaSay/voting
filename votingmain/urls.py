from django.urls import path
from .views import (
    VotingDetailView
)
from . import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name = 'home'),
    path('profile/', views.profile, name = 'profile'),
    path('editprofile/', views.editprofile, name = 'editprofile'),
    path('voting/<int:pk>/', views.votingdetails, name = 'votingdetails'),
    path('voting/<int:pk>/', views.vote_new, name = 'vote_new'),
    #path('voting/', views.votingdetails, name = 'voting'),
]
