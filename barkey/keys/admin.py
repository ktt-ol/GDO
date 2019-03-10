from django.contrib import admin
from .models import key
from .models import keyType

# Register your models here.
class key_admin(admin.ModelAdmin):
    list_display = ('description', 'parent', 'key_type', 'active', 'deleted', 'id')

admin.site.register(key, key_admin)
admin.site.register(keyType)
