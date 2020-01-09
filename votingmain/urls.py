from django.urls import path
from .views import SearchResultsView
from .views import (
    VotingDetailView,
    #CreateVoting
)
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),

    path('home/', views.home, name = 'home'),
    path('profile/', views.profile, name = 'profile'),
    path('editprofile/', views.editprofile, name = 'editprofile'),
    #path('voting/<int:pk>/', views.votingdetails, name = 'votingdetails'),
    #path('voting/<int:pk>/', views.vote_new, name = 'vote_new'),
    #path('voting/', views.votingdetails, name = 'voting'),

    #path('voting/<int:pk>/', VotingDetailView.as_view(), name='vote-detail'),
    path('voting/<int:pk>/', views.votedetails, name='vote-detail'),
    path('delete/<int:pk>/', views.delete, name='delete'),

    path('create/', views.createvoting, name='vote-create'),
    path('createoptions/', views.createoptions, name='options-create'),

    path('mypolls/', views.mypolls, name='mypolls'),
    path('results/', views.results, name='results'),

    path('statistic/<int:pk>/', views.viewstatistics, name='viewstatistics'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('order/', views.orderresult, name='title'),
]
