# Generated by Django 4.2.2 on 2023-06-19 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_alter_file_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file_type',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
