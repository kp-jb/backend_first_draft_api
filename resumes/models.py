from django.contrib.auth import get_user_model
from django.db import models


class Resume(models.Model):
    name = models.CharField(max_length=50)
    # should this be called owner?
    user_id = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    content = models.TextField(blank=True)
    created_date = models.TimeField()
    modified_date = models.DateTimeField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        pass

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)