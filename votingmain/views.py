from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from votedata.models import Voting, VotingOptions, Profile, User
from django.contrib.auth.mixins import LoginRequiredMixin
from votingsystem.dbqueries import getallvotings, getuserinfo
from django.http import JsonResponse
from django.contrib.auth.models import User
from .forms import ProfileForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


@login_required
def home(request):
    voting = Voting.objects.all()
    context = {'voting' : voting}
    print('-----------------------')
    print(context)
    print('-----------------------')
    return render(request, 'home.html', context)



class HomeView(LoginRequiredMixin, ListView):
    model = Voting
    template_name = 'home.html'

    def get_queryset(self):
        #context = getallvotings()
        #voting = Voting.objects.get()
        voting = getallvotings()
        context = {'voting' : voting}

        print('--------')
        print(context)
        print(voting)
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




@login_required
def editprofile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'editprofile.html', context)


@login_required
def votingdetails(request, pk):
    voting = get_object_or_404(Voting, pk=pk)
    print(voting)
    #context = {}
    #context['voting'] = voting
    return render(request, 'votings/votingdetails.html', {'context':voting})


class VotingDetailView(DetailView):
    template_name = 'votings/votingdetails.html'
    model = Voting


def vote_new(request, pk):
    print(pk)

# @login_required
# def editprofile(request):
#     current_user = request.user
#     username = current_user.username
#     context = getuserinfo(current_user.id)
#
#     #if request.method == "POST":
#         #form = ProfileForm(request.POST, instance=request.user,  prefix='form')
#
#         #form = ProfileForm(request.POST, instance=request.user)
#         # if form.is_valid():
#         #     form.save()
#         #     q = Profile() #import your own User model here.
#         #     q.username = request.user.username
#         #     q.save()
#         #     return redirect('home')
#
#         if form.is_valid():
#             prof = form.save(commit=False)
#             prof.save()
#             messages.success(request, f'Your account has been updated!')
#             print('hello')
#             print(prof.profile.age)
#             return redirect('home')
#
#     else:
#         form = ProfileForm(instance=context, prefix='form')
#         print('not hello')
#
#     return render(request, 'editprofile.html', {'context': context,'username': username, 'form': form})
