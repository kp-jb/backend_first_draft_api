from django.urls import path
from .views import CreateCustomUserView

urlpatterns = [
    path("", CreateCustomUserView.as_view(), name="registration"),
]