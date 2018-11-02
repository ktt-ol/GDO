from django.db import models
from django.conf import settings
from django.utils import timezone


class key(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
    key_type = models.CharField(max_length=1)
    created_date = models.DateTimeField(
            default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    valid_from = models.DateTimeField(
            blank=True, null=True)
    valid_to = models.DateTimeField(
            blank=True, null=True)
    active = models.BooleanField()
    deleted = models.BooleanField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.id

