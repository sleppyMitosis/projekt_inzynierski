# Generated by Django 4.2.7 on 2023-12-15 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='age',
        ),
        migrations.AddField(
            model_name='animal',
            name='chip_number',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='animal',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]
