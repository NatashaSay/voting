from votedata.models import Voting, VotingOptions, Result, Profile
from django.db.models import Q

def getallvotings(date_sort=False, date_sort_reversed=False):
    votings = Voting.objects.all()
    return votings


def getuserinfo(user_id):
    profile = Profile.objects.get(user_id=user_id)
    print('*******')
    print(profile)
    print('*******')
    return profile
