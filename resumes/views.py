from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .models import Resume
from project.permissions import IsOwner
from .serializers import ResumeSerializer


class ResumeListCreateView(ListCreateAPIView):
    permission_classes = [IsOwner]
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

    def get_queryset(self):
        return Resume.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ResumeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwner]
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer