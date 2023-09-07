from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(ConfigGolpe)

@admin.register(ContadorGolpes)
class ContadorGolpesAdmin(admin.ModelAdmin):
    list_display = ['id', 'combate', 'numero_asalto', 'golpe', 'esquina']