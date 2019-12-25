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
    for item in voting:
        options = getoptions(item)
        if options.count() == 0:
            item.delete()

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

        options = getoptions(item)

        if options.count() == 0:
            item.delete()


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


def getresult(voting_id):
    options=getoptions(voting_id)
    list=[]
    for i in options:
        list.append(i.id)

    #result = Result.objects.filter(resultvoting_id=option_id)
    return list


def getresultbyoption(option_id):
    result = Result.objects.filter(resultvoting_id=option_id)
    return result.count()


def getresultbyoptionage(option_id):
    result = Result.objects.filter(resultvoting_id=option_id)
    return result


def gettitleoptions(option_id):
    option = VotingOptions.objects.get(id=option_id)
    return option.title


def getcounter():
    voting = getrelevantvotings()
    list = []
    counter = 0
    for item in voting:
        options = getoptions(item)
        for j in options:
            counter+=getresultbyoption(j.id)

        list.append(counter)
        counter=0

    return list

def getcounterbyid(voting_id):
    voting = getvoting(voting_id)
    options = getoptions(voting_id)
    counter = 0
    for i in options:
        counter+=getresultbyoption(i.id)

    return counter






def getresultblock(voting_id):
    getcounterbyid(voting_id)


def getresult1(profile, option_id):
    result = Result.objects.get(resultprofile_id=profile, resultvoting_id=option_id)
    return result.created






# def getages(voting_id):
#     options=getresult(voting_id)
#     results = []
#     for i in options:
#         results.append(Result.objects.filter(resultvoting_id=i))
#
#     profs = {}
#     for i in results:
#         for j in i:
#             profs.append(j.resultprofile_id)
#     #result=getresultbyoptionage()
#     # for i in options:
#     #     list.append(i.resultprofile_id)
#     #
#     profs = profs.distinct()
#     ages = []
#     res=[]
#     for i in profs:
#         ages.append(Profile.objects.filter(id=i))
#
#     return ages
