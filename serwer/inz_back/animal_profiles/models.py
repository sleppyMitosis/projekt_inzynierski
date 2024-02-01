from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True)
    chip_number = models.CharField(max_length=100, blank=True, null=True)
    pedigree_number = models.CharField(max_length=100, blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='animals', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.species}"
