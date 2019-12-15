from django import forms
from django.contrib.auth.models import User
from votedata.models import Profile, User, Voting, VotingOptions
from django.contrib.auth.forms import UserChangeForm


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('image', 'firstname', 'lastname', 'city', 'age', 'bio', 'birthdate')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image', 'firstname', 'lastname', 'city', 'age', 'bio', 'birthdate']


class VotingCreateForm(forms.ModelForm):

    class Meta:
        model = Voting
        fields = ['title', 'info', 'finished', 'is_available', 'is_anon', 'mode', 'type', 'finger', 'need_password', 'pa']


class OptionsCreateForm(forms.ModelForm):

    class Meta:
        model = VotingOptions
        fields = ['title']
