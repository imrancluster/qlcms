from django.contrib import admin

from matirbank.models import MatirBank, BankHistory


@admin.register(MatirBank)
class MatirBankAdmin(admin.ModelAdmin):
    search_fields = ['bank_code']
    list_filter = ['branch']
    list_display = ['bank_code', 'branch']
    list_display_links = ['bank_code']

@admin.register(BankHistory)
class BankHistoryAdmin(admin.ModelAdmin):
    search_fields = ['status']
    list_filter = ['created_on']
    list_display = ['status', 'bank']
    list_display_links = ['bank']