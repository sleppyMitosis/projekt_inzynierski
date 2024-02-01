from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Animal
from .serializers import AnimalSerializer

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Animal.objects.filter(owner=user)

    def perform_create(self, serializer):
        user = self.request.user
        animal_name = serializer.validated_data.get('name')

        if Animal.objects.filter(owner=user, name=animal_name).exists():
            raise ValidationError({'name': 'An animal with this name already exists.'})

        serializer.save(owner=user)
