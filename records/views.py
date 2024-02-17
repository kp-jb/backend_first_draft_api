from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .models import Record
from project.permissions import IsOwner
from .serializers import RecordSerializer


class RecordListCreateView(ListCreateAPIView):
    permission_classes = [IsOwner]
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def get_queryset(self):
        return Record.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RecordRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    queryset = Record.objects.all()
    serializer_class = RecordSerializer