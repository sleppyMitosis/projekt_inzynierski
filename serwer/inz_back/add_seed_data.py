import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "inz_back.settings")
django.setup()

from django.contrib.auth.models import User
from animal_profiles.models import Animal
from medications.models import Medication
from user_profiles.models import UserProfile
from appointments.models import Appointment
from datetime import datetime, timedelta

def add_seed_data():
    print("Creating or getting users...")
    user1, created = User.objects.get_or_create(
        username='user1',
        defaults={
            'email': 'user1@example.com',
            'password': 'testpassword',
            'first_name': 'John',
            'last_name': 'Doe'
        }
    )
    user2, created = User.objects.get_or_create(
        username='user2',
        defaults={
            'email': 'user2@example.com',
            'password': 'testpassword',
            'first_name': 'Jane',
            'last_name': 'Smith'
        }
    )
    print("Users ensured.")

    print("Creating animals...")
    Animal.objects.get_or_create(
        owner=user1,
        name="Max",
        defaults={'species': "Dog", 'date_of_birth': datetime(2018, 1, 1)}
    )
    Animal.objects.get_or_create(
        owner=user1,
        name="Buddy",
        defaults={'species': "Dog", 'date_of_birth': datetime(2019, 5, 20)}
    )
    Animal.objects.get_or_create(
        owner=user2,
        name="Bella",
        defaults={'species': "Cat", 'date_of_birth': datetime(2020, 3, 15)}
    )
    print("Animals ensured.")

    print("Creating medications...")
    Medication.objects.get_or_create(
        animal=Animal.objects.get(owner=user1, name="Max"),
        defaults={
            'name': "Medication1",
            'next_dosage_time': datetime.now() + timedelta(hours=6),
            'dosage_interval': timedelta(hours=12)
        }
    )
    Medication.objects.get_or_create(
        animal=Animal.objects.get(owner=user2, name="Bella"),
        defaults={
            'name': "Medication2",
            'next_dosage_time': datetime.now() + timedelta(hours=8),
            'dosage_interval': timedelta(hours=24)
        }
    )
    print("Medications ensured.")

    print("Seed data ensured.")

    print("Creating appointments...")
    Appointment.objects.get_or_create(
        animal=Animal.objects.get(name="Max"),
        defaults={
            'name': "Checkup for Max",
            'description': "Annual health checkup",
            'appointment_date': datetime.now().date() + timedelta(days=10),
            'appointment_time': datetime.now().time()
        }
    )
    Appointment.objects.get_or_create(
        animal=Animal.objects.get(name="Bella"),
        defaults={
            'name': "Vaccination for Bella",
            'description': "Routine vaccination",
            'appointment_date': datetime.now().date() + timedelta(days=20),
            'appointment_time': datetime.now().time()
        }
    )
    print("Appointments ensured.")

    print("Seed data ensured.")


if __name__ == "__main__":
    add_seed_data()


if __name__ == "__main__":
    add_seed_data()
