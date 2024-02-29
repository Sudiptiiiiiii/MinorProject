from django.contrib import admin
from .models import Transaction, Item,Cards

# @admin.register(Transaction)
# class TransactionAdmin(admin.ModelAdmin):
#     list_display = ['Date_of_Transaction']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['Name', 'remaining_number', 'id']

@admin.register(Cards)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['card_number', 'active', 'id']



class TransactionAdmin(admin.ModelAdmin):
    list_display = ('card_Number', 'Item_Retrieved', 'Number_of_Items', 'Date_of_Transaction')
    search_fields = ('card_Number__card_number',)  # Add search functionality for card_number

admin.site.register(Transaction, TransactionAdmin)