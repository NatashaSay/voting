from django.contrib import admin
from .models import Profile, Voting, VotingOptions, Result, Comment
# Register your models here.


admin.site.register(Profile)
admin.site.register(Voting)
admin.site.register(VotingOptions)
admin.site.register(Result)
admin.site.register(Comment)
