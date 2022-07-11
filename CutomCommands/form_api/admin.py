from django.contrib import admin
from .models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price')

# Register your models here.
admin.site.register(Car, CarAdmin)
