from django.contrib import admin

from events.models import ProgramType, Program


@admin.register(ProgramType)
class ProgramTypeAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['branch']
    list_display = ['name', 'branch']
    list_display_links = ['name']

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    pass