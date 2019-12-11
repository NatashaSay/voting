from django import forms

from votedata.models import Profile

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('image', 'firstname', 'lastname', 'city', 'age', 'bio')
