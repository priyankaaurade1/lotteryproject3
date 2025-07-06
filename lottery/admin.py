from django.contrib import admin
from .models import LotteryResult

# @admin.register(LotteryResult)
# class LotteryResultAdmin(admin.ModelAdmin):
#     list_display = ('date', 'time_slot', 'row', 'column', 'number',  'is_editable')
#     readonly_fields = ('date', 'time_slot', 'row', 'column')

#     def has_change_permission(self, request, obj=None):
#         if obj and not obj.is_editable():
#             return False
#         return super().has_change_permission(request, obj)
