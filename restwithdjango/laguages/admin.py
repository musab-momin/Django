from django.contrib import admin
from .models import Language, LanguageInventor, Programmer

# Register your models here.
admin.site.register(Language)
admin.site.register(LanguageInventor)
admin.site.register(Programmer)