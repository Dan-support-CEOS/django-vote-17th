# Generated by Django 3.2.16 on 2023-06-24 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_candidate_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isCandiVoted',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='isDemoVoted',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
