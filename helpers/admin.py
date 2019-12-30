from django.contrib import admin

from helpers.models import Identification


@admin.register(Identification)
class IdentificationAdmin(admin.ModelAdmin):
    pass

