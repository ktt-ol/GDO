from django.contrib import admin
from .models import *

# Register your models here.
class key_user(admin.ModelAdmin):

    def get_list_display(self, request):
        if request.user.is_superuser:
            list_display = ('description', 'parent', 'key_type', 'active', 'deleted', 'id')
        else:
            list_display = ('description', 'parent', 'key_type', 'active')
        return list_display

    def get_queryset(self, request):
        qs = super(admin.ModelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(deleted=False)

    def delete_queryset(self, request, queryset):
        for model in queryset:
            model.delete()


admin.site.register(key, key_user)
admin.site.register(keyType)
admin.site.register(tenant)
