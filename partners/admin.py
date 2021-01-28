from django.contrib import admin
from .models import Partner


# Register your models here.
@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name',
                    'api_key',
                    'api_url',
                    )

    search_fields = ('name',)
    ordering = ('name',)