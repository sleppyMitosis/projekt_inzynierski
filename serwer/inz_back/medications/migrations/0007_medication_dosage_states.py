# Generated by Django 4.2.7 on 2024-01-13 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0006_alter_medication_animal_alter_medication_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='medication',
            name='dosage_states',
            field=models.TextField(default='[]'),
        ),
    ]