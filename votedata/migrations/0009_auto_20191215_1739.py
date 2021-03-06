# Generated by Django 2.2.7 on 2019-12-15 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votedata', '0008_auto_20191215_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='voting',
            name='finger',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='voting',
            name='need_password',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='voting',
            name='password',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='voting',
            name='type',
            field=models.CharField(choices=[('y', 'Yes'), ('n', 'No'), ('u', 'Unknown')], max_length=1),
        ),
    ]
