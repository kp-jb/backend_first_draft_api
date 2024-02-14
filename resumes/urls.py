from django.urls import path
from .views import ResumeListCreateView, ResumeRetrieveUpdateDestroyView

urlpatterns = [
    path("", ResumeListCreateView.as_view(), name="resume_list"),
    path("<int:pk>/", ResumeRetrieveUpdateDestroyView.as_view(), name="resume_detail"),
]