# Generated by Django 3.2.7 on 2021-09-26 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatemodel',
            name='is_validated',
            field=models.BooleanField(default=0),
        ),
    ]