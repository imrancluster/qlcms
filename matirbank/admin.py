from django.contrib import admin

from matirbank.models import MatirBank


@admin.register(MatirBank)
class MatirBankAdmin(admin.ModelAdmin):
    search_fields = ['bank_code']
    list_filter = ['branch']
    list_display = ['bank_code', 'branch']
    list_display_links = ['bank_code']