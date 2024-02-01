from rest_framework import viewsets
from .models import Medication
from .serializers import MedicationSerializer
from rest_framework.permissions import IsAuthenticated

class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Medication.objects.filter(animal__owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save()
        dosage_states = self.request.data.get('dosage_states')
        if dosage_states:
            serializer.instance.set_dosage_states(dosage_states)
            serializer.instance.save()

    def perform_update(self, serializer):
        serializer.save()
        dosage_states = self.request.data.get('dosage_states')
        if dosage_states is not None:
            serializer.instance.set_dosage_states(dosage_states)
            serializer.instance.save()


