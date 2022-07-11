from django.contrib import admin
from blog.models import Post


class AdminPost(admin.ModelAdmin):
    list_display = ('title', 'active', 'content', 'publish_date', 'posted_since')

    def posted_since(self, instance, *args, **kwargs):
        return instance.get_age()

# Register your models here.
admin.site.register(Post, AdminPost)