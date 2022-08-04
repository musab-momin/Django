from django.contrib import admin
from classbasedviews.models import author, Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    


# Register your models here.
admin.site.register(author)
admin.site.register(Book, BookAdmin)