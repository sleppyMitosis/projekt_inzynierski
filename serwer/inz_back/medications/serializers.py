from rest_framework import serializers
from .models import Medication
from animal_profiles.models import Animal
from animal_profiles.serializers import AnimalSerializer


class MedicationSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer(read_only=True)
    animal_id = serializers.IntegerField(write_only=True, required=False)
    dosage_states = serializers.SerializerMethodField()

    class Meta:
        model = Medication
        fields = ['id', 'animal', 'animal_id', 'name', 'start_date', 'end_date', 'dosage_count', 'dosage_states']

    def get_dosage_states(self, obj):
        return obj.get_dosage_states()

    def create(self, validated_data):
        animal_id = validated_data.pop('animal_id', None)
        medication = Medication.objects.create(**validated_data)
        if animal_id:
            medication.animal = Animal.objects.get(id=animal_id)
            medication.save()
        return medication

    def update(self, instance, validated_data):
        animal_id = validated_data.pop('animal_id', None)
        if animal_id:
            instance.animal = Animal.objects.get(id=animal_id)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        dosage_states = validated_data.get('dosage_states')
        if dosage_states is not None:
            instance.set_dosage_states(dosage_states)

        instance.save()
        return instance
