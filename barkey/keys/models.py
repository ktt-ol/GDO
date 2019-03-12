from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import datetime
from datetime import timedelta
import uuid


class key(models.Model):
    description = models.CharField(max_length=64, null=True)  # Beschreibung des Keys / der Gruppe
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, limit_choices_to={'key_type': 'G'})
    key_type = models.ForeignKey('keyType', on_delete=models.CASCADE) #S = Single-Use, G = Gruppe, M = Mieter, C = Standard-Code
    key_value = models.UUIDField(primary_key=True, editable=False)
    created_date = models.DateTimeField(
            default=timezone.now, editable=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, editable=False, null=True)
    created_for = models.ForeignKey('tenant', on_delete=models.CASCADE, editable=False, null=True) #gibt an, zu welchem Mieter ein Key gehört
    valid_from = models.DateTimeField(
            blank=True, null=True)
    valid_to = models.DateTimeField(
            blank=True, null=True)
    first_used = models.DateTimeField(
            blank=True, null=True, editable=False) #Wird gesetzt, wenn ein Single-Use Code das erste mal genutzt wird DEPRECATED
    valid_for = models.IntegerField(
            blank=True, null=True) #wird beim erstellen eines Single-Use Codes genutzt, duration, int
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False, editable=False)

    def save(self):

        self.key_value = uuid.uuid4()

        super(key, self).save()

    def delete(self):
        self.deleted = True
        self.save()

        children = key.objects.filter(parent=self)
        print(children)

        for child in key.objects.filter(parent=self):
            if child.parent is not None:
                child.delete()
        print("FCKU")

    def __str__(self):
        return self.description

    def is_valid(self):
        if not self._is_active() and not self._is_deleted() and not self._is_valid_to_date() and not self._is_valid_from_date() and self._is_valid_group():
            return False
        else:
            return True

    def _is_valid_group(self):
        if self.key_type.id == "S" or self.key_type.id == "C":
            print(keyType.id)
            return True
        else:
            return False

    def _is_valid_to_date(self):
        if self.valid_to > datetime.now or self.valid_to is None:
            if self.parent is not None and self.valid_to is None:
                return self.parent._is_valid_to_date()
            elif self.parent is None or self.valid_to > datetime.now:
                return True
        else:
            return False

    def _is_valid_from_date(self):
        if self.valid_from < datetime.now or self.valid_from is None:
            if self.parent is not None and self.valid_from is None:
                return self.parent._is_valid_from_date()
            elif self.parent is None or self.valid_from < datetime.now:
                return True
        else:
            return False

    def _is_active(self):
        if self.active:
            if self.parent is None:
                return True
            else:
                self.parent._is_active()
        else:
            return False

    def _is_deleted(self):
        if self.deleted:
            if self.parent is None:
                return True
            else:
                self.parent._is_deleted()
        else:
            return False

    def set_valid_to(self, value):
        if self.valid_to is None or self.valid_to > datetime.now + self._duration(value):
            self.valid_to = datetime.now + self._duration(value)
        #todo: Logeintrag bei _nicht_ gesetztem Wert, howto?


    def _duration(self, value):
        return timedelta(hours = value)

class keyType(models.Model):
    id = models.CharField(primary_key=True, max_length=1) #S = Single-Use, G = Gruppe, M = Mieter, C = Standard-Code
    description = models.CharField(max_length=64, null=True) #Beschreibung des Keys / der Gruppe

    def publish(self):
        self.save()

    def __str__(self):
        return self.description + "  (" + self.id + ")"


class tenant(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    tenant = models.CharField(max_length=64, null=True) #Beschreibung des Mieters

    def __str__(self):
        return self.tenant

class manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tenant = models.ForeignKey('tenant', on_delete=models.CASCADE, editable=True) #gibt an, zu welchem Mieter ein user gehört
