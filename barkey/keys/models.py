from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import datetime
import uuid


class key(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    key_type = models.ForeignKey('keyType', on_delete=models.CASCADE) #S = Single-Use, G = Gruppe, M = Mieter, C = Standard-Code
    description = models.CharField(max_length=64, null=True) #Beschreibung des Keys / der Gruppe
    created_date = models.DateTimeField(
            default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    created_for = models.ForeignKey('tenant', on_delete=models.CASCADE, editable=False) #gibt an, zu welchem Mieter ein Key gehört
    valid_from = models.DateTimeField(
            blank=True, null=True)
    valid_to = models.DateTimeField(
            blank=True, null=True)
    first_used = models.DateTimeField(
            blank=True, null=True, editable=False) #Wird gesetzt, wenn ein Single-Use Code das erste mal genutzt wird
    valid_for = models.DateTimeField(
            blank=True, null=True) #wird beim erstellen eines Single-Use Codes genutzt
    active = models.BooleanField()
    deleted = models.BooleanField()


    def save(self):
        if str(self.valid_to) == "None":
            self.valid_to = datetime(2999, 12, 31, 23, 59)
        super(key, self).save()


    def __str__(self):
        if not str(self.parent) == "None":
            return self.description + ", Parent: " + str(self.parent)
        else:
            return self.description


class keyType(models.Model):
    id = models.CharField(primary_key=True, max_length=1) #S = Single-Use, G = Gruppe, M = Mieter, C = Standard-Code
    description = models.CharField(max_length=64, null=True) #Beschreibung des Keys / der Gruppe

    def publish(self):
        self.save()

    def __str__(self):
        return self.description + "  (" + self.id + ")"