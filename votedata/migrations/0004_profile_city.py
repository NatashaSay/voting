# Generated by Django 2.2.7 on 2019-12-08 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votedata', '0003_voting_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
