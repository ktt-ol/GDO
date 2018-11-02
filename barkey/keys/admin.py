from django.contrib import admin
from .models import key
from .models import keyType

# Register your models here.
admin.site.register(key)
admin.site.register(keyType)
