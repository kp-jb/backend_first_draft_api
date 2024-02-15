from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Resume(models.Model):
    user_id = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    name = models.CharField(max_length=50)

    content = models.TextField(blank=True, max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('resume_detail', args=[str(self.id)])

