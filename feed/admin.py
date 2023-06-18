from django.contrib import admin
from .models import File

class FileAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','downloads', 'emails_sent', 'uploaded_at',)
    list_filter = ('uploaded_at', 'downloads', 'emails_sent')
    search_fields = ('title', 'description')
    ordering = ('-uploaded_at',)

admin.site.register(File, FileAdmin)
