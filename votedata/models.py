from django.db import models
from datetime import datetime as dt
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from PIL import Image, ImageDraw
from django.urls import reverse



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30, blank=True)
    lastname = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    age = models.IntegerField(default=0,blank=True)
    bio = models.TextField(max_length=300, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    image = models.ImageField(default='def.png', upload_to='profile_pics')


    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    def save(self, *args, **kwargs):
        print('not wo')
        super().save()

        img = Image.open(self.image.path)

        if img.height > 200 or img.width > 200:
            output_size = (200,200)
            img.thumbnail(output_size)
            img.save(self.image.path)


            draw = ImageDraw.Draw(img)
            draw.ellipse((180, 200, 180, 200), fill=(255,0,0,0))


    # def getid(self, i):
    #     profile = Profile.objects.all().filter(user_id=i)
    #     print(profile.id, 'ID')
    #     return profile.id


    # def save(self, *args, **kw):
    #     super(Profile, self).save(*args, **kw)
    #     self.instance.user.firstname = self.cleaned_data.get('firstname')
    #     self.instance.user.lastname = self.cleaned_data.get('lastname')
    #     self.instance.user.city = self.cleaned_data.get('city')
    #     self.instance.user.save()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except ObjectDoesNotExist:
        Profile.objects.create(user=instance)


class Voting(models.Model):
    userprofile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    info = models.TextField(max_length=1000, default='Enter')
    created = models.DateTimeField(auto_now=True, blank=False)
    finished = models.DateTimeField(auto_now=False, blank=False)
    theme = models.CharField(max_length=200, blank=True)
    is_available = models.BooleanField(default=True)
    is_anon = models.BooleanField(default=False)
    finger = models.BooleanField(default=False)

    pa = models.CharField(max_length=200, blank=True)

    MODE = (
    ('o', 'One choice'),
    ('m', 'Multiple choice'),
    )

    TYPE = (
    ('y', 'Yes'),
    ('n', 'No'),
    ('u', 'Unknown'),
    )

    mode = models.CharField(max_length=50, choices=MODE, blank=False, default=0)
    type = models.CharField(max_length=1, choices=TYPE)

    def __str__(self):
        return f"{self.title} {self.info} {self.created}"

    # def save(self):
    #     print('it works')
    #     super.save()

    # def get_absolute_url(self):
    #     return reverse('votingdetails', kwargs={'pk': self.pk})


class VotingOptions(models.Model):
    voting = models.ForeignKey(Voting, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    type = models.TextField(max_length=50, default='Enter')

    def __str__(self):
        return f"{self.title} {self.voting} {self.type}"


class Result(models.Model):
    resultvoting = models.ForeignKey(VotingOptions, on_delete=models.CASCADE)
    resultprofile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True, blank=False)

    def __str__(self):
        return f"{self.resultvoting} {self.resultprofile} {self.created}"


class Comment(models.Model):
    votingpost = models.ForeignKey(VotingOptions, on_delete=models.CASCADE)
    userpost = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True, blank=False)
    info = models.TextField(max_length=1000, default='Enter')

    def __str__(self):
        return f"{self.votingpost} {self.userpost} {self.info} {self.created}"
