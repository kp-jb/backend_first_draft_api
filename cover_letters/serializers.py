from rest_framework import serializers
from .models import CoverLetter


class CoverLetterSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoverLetter
        fields = ("name", "user_id", "content", "created_date", "modified_date")
