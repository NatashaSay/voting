from votedata.models import Voting, VotingOptions, Result, Profile
from django.db.models import Q
from datetime import datetime, timedelta, time
from django.utils import timezone
from django.db.models import Count

def getallvotings(date_sort=False, date_sort_reversed=False):
    votings = Voting.objects.all()
    return votings


def getuservotings(user_id):
    voting = Voting.objects.filter(userprofile_id=user_id)
    return voting


def getvoting(voting_id):
    voting = Voting.objects.get(id=voting_id)
    return voting


def getoptions(voting_id):
    options = VotingOptions.objects.filter(voting_id=voting_id)
    return options


#получает user-> возвращает profile
def getuserinfo(user_id):
    profile = Profile.objects.get(user_id=user_id)
    return profile


#получает id -> возвращает инфо
def getprofile(user_id):
    profile = Profile.objects.get(id=user_id)
    return profile


def getidprofile(user_id):
    profileid = getuserinfo(user_id).id
    return profileid


def getrelevantvotings(date_sort=False, date_sort_reversed=False):
    now = timezone.now()
    votings = Voting.objects.all()
    for item in votings:
        if now > item.finished:
            item.is_available=False
            item.save()

    return votings.exclude(is_available=False)


def getfinishedvotings(date_sort=False, date_sort_reversed=False):
    now = timezone.now()
    votings = Voting.objects.all()
    for item in votings:
        if now > item.finished:
            item.is_available=False
            item.save()

    return votings.exclude(is_available=True)


def getoptionid(voting_id, option):
    options = getoptions(voting_id)
    for i in options:
        if i.title == option:
            return i.id
    return None



def alreadyvoted(profile_id, voting_id):
    options=getoptions(voting_id)
    list=[]
    for i in options:
        list.append(i.id)
    for i in list:
        result = Result.objects.filter(resultprofile_id=profile_id, resultvoting_id=i)
        if result.count()>0:
            return True
    return False
