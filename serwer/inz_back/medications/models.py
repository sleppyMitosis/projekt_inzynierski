import json
from django.db import models
from animal_profiles.models import Animal

class Medication(models.Model):
    id = models.AutoField(primary_key=True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='medications', null=True, blank=True)
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    dosage_count = models.IntegerField()
    dosage_states = models.TextField(default="[]")

    def set_dosage_states(self, states):
        states = (states or []) + [False] * (self.dosage_count - len(states))
        self.dosage_states = json.dumps(states)

    def get_dosage_states(self):
        states = json.loads(self.dosage_states)
        return [state if state is not None else False for state in states]

    def __str__(self):
        return self.name
