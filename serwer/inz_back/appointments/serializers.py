from rest_framework import serializers
from .models import Appointment
from animal_profiles.models import Animal
from animal_profiles.serializers import AnimalSerializer
from datetime import datetime


class AppointmentSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer(read_only=True)
    animal_id = serializers.IntegerField(write_only=True, required=False)
    formatted_appointment_datetime = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = ['id', 'animal', 'animal_id', 'name', 'description', 'appointment_date', 'appointment_time', 'formatted_appointment_datetime']

    def get_formatted_appointment_datetime(self, obj):
        combined_datetime = datetime.combine(obj.appointment_date, obj.appointment_time)
        return combined_datetime.strftime("%Y-%m-%d %H:%M")

    def create(self, validated_data):
        animal_id = validated_data.pop('animal_id', None)
        appointment = Appointment.objects.create(**validated_data)
        if animal_id:
            appointment.animal = Animal.objects.get(id=animal_id)
            appointment.save()
        return appointment

    def update(self, instance, validated_data):
        animal_id = validated_data.pop('animal_id', None)
        if animal_id:
            instance.animal = Animal.objects.get(id=animal_id)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
