from django.urls import path
from .views import openai_request_view

urlpatterns = [
    path("", openai_request_view, name="openai_request"),
]