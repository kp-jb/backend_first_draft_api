from django.urls import path
from .views import RecordListCreateView, RecordRetrieveUpdateDestroyView

urlpatterns = [
    path("", RecordListCreateView.as_view(), name="record_list"),
    path("<int:pk>/", RecordRetrieveUpdateDestroyView.as_view(), name="record_detail"),
]