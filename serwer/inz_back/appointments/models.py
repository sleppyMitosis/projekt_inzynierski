from django.db import models
from animal_profiles.models import Animal

class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='appointments', null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    def __str__(self):
        return self.name
