from django.contrib import admin
from .models import Blog
from django.utils.html import format_html

class BlogAdmin(admin.ModelAdmin):
    #fields = ('title', 'image', 'content') #fields you want to show on admin form
    exclude = ('is_deleted', ) #fields you want to exclude from admin form
    list_display = ('title', 'blog_content', 'image', 'is_deleted', 'created_at', 'view_record') #fields you want to show on admin table
    #list_display_links = ('title', 'blog_content') #convert filelds into anchor link
    list_filter = ('is_deleted', 'created_at')

    def blog_content(self, obj):
        return obj.content[:39]

    def view_record(self, obj):
        return format_html(f'<a href ="/admin/admin_customisation/blog/{obj.id}/change/" class="default">View</a> ')



# Register your models here.
admin.site.register(Blog, BlogAdmin)