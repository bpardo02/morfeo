from django.contrib import admin
from .models import Sueno

@admin.register(Sueno)
class SuenoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "iniciales", "fecha", "estado")
    list_filter = ("estado", "fecha")
    search_fields = ("titulo", "mensaje", "iniciales")