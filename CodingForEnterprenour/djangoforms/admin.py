from django.contrib import admin
from djangoforms.models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'company_name', 'release_date']


# Register your models here.
admin.site.register(Car, CarAdmin)