from django.urls import path
from .views import CoverLetterListCreateView, CoverLetterRetrieveUpdateDestroyView

urlpatterns = [
    path("", CoverLetterListCreateView.as_view(), name="cover_letter_list"),
    path("<int:pk>/", CoverLetterRetrieveUpdateDestroyView.as_view(), name="cover_letter_detail"),
]