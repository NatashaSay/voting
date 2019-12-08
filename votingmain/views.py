from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import ListView
from votedata.models import Voting, VotingOptions, Profile
from django.contrib.auth.mixins import LoginRequiredMixin
from votingsystem.dbqueries import getallvotings, getuserinfo
from .forms import UploadDocumentForm
from django.http import JsonResponse

@login_required
def home(request):
    return render(request, 'home.html')



class HomeView(LoginRequiredMixin, ListView):
    model = Voting
    template_name = 'home.html'

    def get_queryset(self):
        context = getallvotings()
        print('--------')
        print(context)
        print('--------')
        #print (Voting.objects.all(), VotingOptions.objects.all())
        #return Voting.objects.all()
        return context


@login_required
def profile(request):
    current_user = request.user
    context = getuserinfo(current_user.id)


    # if request.POST.get('action') == 'post':
    #     title = request.POST.get('title')
    #     description = request.POST.get('description')
    #
    #     response_data['title'] = title
    #     response_data['description'] = description
    # 
    #     Post.objects.create(
    #         title = title,
    #         description = description,
    #         )
    #     return JsonResponse(response_data)


    return render(request, 'profile.html', {'context': context})


class ProfileView(LoginRequiredMixin, ListView):
    model = Voting
    template_name = 'profile.html'

    def get_queryset(self):

        #context = getallvotings()
        print('--------')
        print(context)
        print('--------')
        #print (Voting.objects.all(), VotingOptions.objects.all())
        #return Voting.objects.all()
        return context
