from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import *

# Register your models here.

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class ManagerInline(admin.StackedInline):
    model = manager
    can_delete = False
    verbose_name_plural = 'manager'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ManagerInline,)

class key_user(admin.ModelAdmin):

    def get_list_display(self, request):
        if request.user.is_superuser:
            list_display = ('description', 'parent', 'key_type', 'active', 'deleted', 'key_value', 'created_for')
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

    def save_model(self, request, obj, form, change):

        if obj.created_for == None:
            obj.created_for = request.user.manager.tenant

        if obj.created_by == None:
            obj.created_by = request.user

        if obj.parent == None and not obj.key_type == keyType.objects.get(id='M'):
            parent = key.objects.get(key_type=keyType.objects.get(id='M'), created_for=request.user.manager.tenant)
            obj.parent = parent
            print(parent)

        super().save_model(request, obj, form, change)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "parent":
            print(db_field.name)
            kwargs["queryset"] = key.objects.filter(created_for=request.user.manager.tenant)
            print(kwargs["queryset"])
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(key, key_user)
admin.site.register(keyType)
admin.site.register(tenant)
