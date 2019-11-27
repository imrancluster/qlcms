from django.contrib import admin
from django.utils import timezone
from geography.models import Branch
from geography.models import *
from django.forms import Select
from qlcms.fields import BOOLEAN_SELECT_CHOICES

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.BooleanField: {'widget': Select(choices=BOOLEAN_SELECT_CHOICES)}
    }

    search_fields = ['name', 'branch_code']
    list_filter = ['created_on', 'branch_type', 'area']
    exclude = ['user', ]
    list_display = ['id', 'name', 'branch_code', 'branch_type', 'status', 'country_code', 'area']
    # readonly_fields = ['branch_code']
    list_display_links = ['name']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        else:
            obj.updated_on = timezone.now()

        super().save_model(request, obj, form, change)

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['district']
    list_display = ['name', 'district']
    list_display_links = ['name']

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['division']
    list_display = ['name', 'division']
    list_display_links = ['name']

@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']
    list_display_links = ['name']
