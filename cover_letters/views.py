from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .models import CoverLetter
from project.permissions import IsOwner
from .serializers import CoverLetterSerializer


class CoverLetterListCreateView(ListCreateAPIView):
    permission_classes = IsOwner
    queryset = CoverLetter.objects.all()
    serializer_class = CoverLetterSerializer


class CoverLetterRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = IsOwner
    queryset = CoverLetter.objects.all()
    serializer_class = CoverLetterSerializer
