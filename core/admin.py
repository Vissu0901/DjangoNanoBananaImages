from django.contrib import admin
from .models import NanoBananaCard

@admin.register(NanoBananaCard)
class NanoBananaCardAdmin(admin.ModelAdmin):
    list_display = ('user', 'prompt', 'created_at')
    list_filter = ('user', 'created_at')
    search_fields = ('prompt',)
