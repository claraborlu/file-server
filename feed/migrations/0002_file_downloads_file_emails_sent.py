# Generated by Django 4.2.2 on 2023-06-18 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='downloads',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='file',
            name='emails_sent',
            field=models.PositiveIntegerField(default=0),
        ),
    ]