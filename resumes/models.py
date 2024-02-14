from django.contrib.auth import get_user_model
from django.db import models


class Resume(models.Model):
    user_id = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    name = models.CharField(max_length=50)
    # should this be called owner?
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)