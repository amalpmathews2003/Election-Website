# Generated by Django 3.2.7 on 2021-09-26 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_candidatemodel_is_validated'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatemodel',
            name='symbol',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
