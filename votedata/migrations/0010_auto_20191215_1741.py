# Generated by Django 2.2.7 on 2019-12-15 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votedata', '0009_auto_20191215_1739'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voting',
            old_name='password',
            new_name='pa',
        ),
    ]
