from django.contrib import admin
from .models import Computer


class ComputerAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price')

# Register your models here.
admin.site.register(Computer, ComputerAdmin)