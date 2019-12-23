from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . import views
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from votedata.models import Voting, VotingOptions, Profile, User, Result
from django.contrib.auth.mixins import LoginRequiredMixin
from votingsystem.dbqueries import *
from votingmain.statistic import *
from django.http import JsonResponse
from django.contrib.auth.models import User
from .forms import ProfileForm, UserUpdateForm, ProfileUpdateForm, VotingCreateForm, OptionsCreateForm
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
    count = getcounter()
    context = {
        'voting': getrelevantvotings(),
        'count': count
    }

    return render(request, 'home.html', context)


@login_required
def mypolls(request):
    current_user = request.user
    profile = Profile.objects.get(user_id=current_user.id)
    voting = getuservotings(profile.id)

    context = {
        'voting': voting
    }
    return render(request, 'mypolls.html', context)


@login_required
def results(request):
    #current_user = request.user
    #profile = Profile.objects.get(user_id=current_user.id)
    voting = getfinishedvotings()
    context = {
        'voting': voting
    }
    return render(request, 'results.html', context)

# class HomeView(LoginRequiredMixin, ListView):
#     model = Voting
#     template_name = 'home.html'
#
#     def get_queryset(self):
#         #context = getallvotings()
#
#         #print (Voting.objects.all(), VotingOptions.objects.all())
#         #return Voting.objects.all()
#         return context


@login_required
def profile(request):
    current_user = request.user
    context = getuserinfo(current_user.id)
    info ={
        'count': getuservotings(context.id).count(),
        'date': current_user.date_joined,
        'email': current_user.email
    }
    print(getuservotings(context.id))
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


    return render(request, 'profile.html', {'context': context,'info':info})


class ProfileView(LoginRequiredMixin, ListView):
    model = Voting
    template_name = 'profile.html'

    def get_queryset(self):
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
    voting = getvoting(pk)
    voting = get_object_or_404(Voting, pk=pk)


class VotingDetailView(LoginRequiredMixin, DetailView):
    template_name = 'votings/votingdetails.html'
    model = Voting

    def get_queryset(request):
        voting = request.session['vote_id']
        print(voting)



@login_required
def votedetails(request, pk=0):
    # if(pk==0):
    #     return redirect('home')

    request.session['vote_id']=pk
    voting = getvoting(pk)
    username = getprofile(voting.userprofile_id)
    options = getoptions(pk)
    profile = getidprofile(request.user.id)
    creator = voting.userprofile_id
    view = 'guest'
    if (creator == profile):
        view = 'creator'

    if (alreadyvoted(profile, pk) is True):
        view = 'voted'

    context = {
        'username': username.firstname,
        #Add
        'title': voting.title,
        'info': voting.info,
        'theme': voting.theme,
        'created': voting.created,
        'finished': voting.finished,
        #options
        'options': options,
        'mode': voting.mode,
        'view': view
    }
    if request.method == 'POST':
        opt = request.POST.get('optradio')
        if opt is not None:
            option_id = getoptionid(pk, opt)
            Result.objects.create(resultprofile_id=profile, resultvoting_id=option_id)

        else:
            optcheck = request.POST.getlist('optcheck')
            for item in optcheck:
                option_id = getoptionid(pk, item)
                Result.objects.create(resultprofile_id=profile, resultvoting_id=option_id)

        return redirect('home')


    return render(request, 'votings/votingdetails.html', context)


@login_required
def createvoting(request):
    if request.method == 'POST':
        form = VotingCreateForm(request.POST)
        if form.is_valid():
            current_user = request.user
            profile = Profile.objects.get(user_id=current_user.id)
            form.instance.userprofile_id = profile.id
            form.save()
            request.session['vote_id'] = form.save().id
            return redirect( 'options-create')
        else:
            return HttpResponse('not valid')
    else:
        model = Voting
        form = VotingCreateForm(instance=request.user)
        return render(request, 'votings/votingcreate.html', {'form' : form})


@login_required
def createoptions(request):
    args = {}
    args.update(csrf(request))
    #form = OptionsCreateForm(instance=request.user)
    voting_id = request.session['vote_id']
    voting = getvoting(voting_id)
    print(voting_id)

    if request.method == 'POST':
        options = request.POST.get('min-2')
        option = options.split(',')
        for i in option:
            if i!="":
                request.session['title'] = i
                VotingOptions.objects.create(title=i, voting_id=request.session['vote_id'])

        return redirect('home')

    return render(request, 'votings/votingoptions.html', {'voting':voting})



@login_required
def viewstatistics(request, pk):
    voting = getvoting(pk)
    username = getprofile(voting.userprofile_id)
    options = getoptions(pk)
    result = getcounterbyid(pk)
    # print('-------')
    # print(result)
    # print('-------')
    # arg = {}
    # for i in result:
    #
    #     print(i)
    #     # arg.update({i.option:i.count})
    # print(arg)
    context = {
        'username': username.firstname,
        'title': voting.title,
        'info': voting.info,
        'theme': voting.theme,
        'created': voting.created,
        'finished': voting.finished,
        'result': result
    }
    dataset = createset(pk)
    #datasetage = createsetbyage(pk)

    return render(request, 'votings/statistic.html', {'dataset': dataset, 'context':context})



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
