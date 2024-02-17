
from django.core.validators import MaxLengthValidator
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Record(models.Model):
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    name = models.CharField(max_length=50)

    content = models.TextField(blank=True, validators=[MaxLengthValidator(limit_value=10000)])
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_resume = models.BooleanField(blank=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('record_detail', args=[str(self.id)])

