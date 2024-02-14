from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .models import Resume
from project.permissions import IsOwner
from .serializers import ResumeSerializer


class ResumeListCreateView(ListCreateAPIView):
    permission_classes = IsOwner
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer


class ResumeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = IsOwner
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer