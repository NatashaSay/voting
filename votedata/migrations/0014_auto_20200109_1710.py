# Generated by Django 2.2.7 on 2020-01-09 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votedata', '0013_remove_voting_need_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voting',
            name='pa',
        ),
        migrations.RemoveField(
            model_name='voting',
            name='type',
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='def.png', upload_to='profile_pics'),
        ),
    ]
