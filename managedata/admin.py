from django.contrib import admin

from .models import DataInfo

class DataInfoAdmin(admin.ModelAdmin):
    fields = ['data_file', 'upload_at']
    list_display = ('id', 'data_file', 'upload_at')
    
admin.site.register(DataInfo, DataInfoAdmin)
# Register your models here.
