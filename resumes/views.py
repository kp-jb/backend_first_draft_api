from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .models import Resume
from project.permissions import IsOwnerOrReadOnly
from .serializers import ResumeSerializer


class ResumeListCreateView(ListCreateAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


class ResumeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = IsOwnerOrReadOnly
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
