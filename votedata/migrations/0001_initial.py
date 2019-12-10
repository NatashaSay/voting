# Generated by Django 2.2.7 on 2019-12-07 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=30)),
                ('lastname', models.CharField(blank=True, max_length=30)),
                ('age', models.IntegerField(blank=True)),
                ('bio', models.TextField(blank=True, max_length=300)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Voting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('info', models.TextField(default='Enter', max_length=1000)),
                ('created', models.DateTimeField(auto_now=True)),
                ('finished', models.DateTimeField()),
                ('is_available', models.BooleanField(default=True)),
                ('is_anon', models.BooleanField(default=False)),
                ('mode', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VotingOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('type', models.TextField(default='Enter', max_length=50)),
                ('voting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votedata.Voting')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('resultprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votedata.Profile')),
                ('resultvoting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votedata.VotingOptions')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True)),
                ('info', models.TextField(default='Enter', max_length=1000)),
                ('userpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votedata.Profile')),
                ('votingpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votedata.VotingOptions')),
            ],
        ),
    ]