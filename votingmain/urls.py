from django.urls import path
from .views import (
    VotingDetailView,
    #CreateVoting
)
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('profile/', views.profile, name = 'profile'),
    path('editprofile/', views.editprofile, name = 'editprofile'),
    #path('voting/<int:pk>/', views.votingdetails, name = 'votingdetails'),
    #path('voting/<int:pk>/', views.vote_new, name = 'vote_new'),
    #path('voting/', views.votingdetails, name = 'voting'),
    path('voting/<int:pk>/', VotingDetailView.as_view(), name='vote-detail'),
    path('create/', views.createvoting, name='vote-create'),
    path('createoptions/', views.createoptions, name='options-create'),
]
