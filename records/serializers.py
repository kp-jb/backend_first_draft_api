from rest_framework import serializers
from .models import Record


class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Record
        fields = ("id", "name", "owner", "content","is_resume", "created_date", "modified_date")
