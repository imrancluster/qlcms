from django.contrib import admin

from django.forms import Select
from people.models import *
from qlcms.fields import BOOLEAN_SELECT_CHOICES


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.BooleanField: {'widget': Select(choices=BOOLEAN_SELECT_CHOICES)}
    }

    search_fields = ['name', 'registration_no', 'phone', 'email']
    list_filter = ['branch']
    # exclude = ['user', ]
    list_display = ['name', 'branch', 'registration_no', 'phone', 'email', 'status']
    # readonly_fields = ['branch_code']
    list_display_links = ['name']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass