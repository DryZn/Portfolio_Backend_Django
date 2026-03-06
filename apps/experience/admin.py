from django.contrib import admin
from .models import Experience


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['company', 'position', 'start_date', 'end_date', 'current', 'order']
    list_filter = ['current', 'start_date']
    search_fields = ['company', 'position', 'description']
    list_editable = ['order']
    readonly_fields = ['created_at']
