from votedata.models import Voting, VotingOptions, Result, Profile
from django.db.models import Q
from datetime import datetime, timedelta, time
from django.utils import timezone

def getallvotings(date_sort=False, date_sort_reversed=False):
    votings = Voting.objects.all()
    return votings


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
