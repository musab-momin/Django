from pyexpat import model
from django.contrib import admin
from django.core.paginator import Paginator
from django.core.cache import cache
from django.db import models
from public_chat.models import PublicChatRoom, PublicChatRoomMessage


class PublicChatRoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']
    list_display_links = ['id', 'title']
    
    
    class Meta:
        model = PublicChatRoom
    
admin.site.register(PublicChatRoom, PublicChatRoomAdmin)


#Resource: http://masnun.rocks/2017/03/20/django-admin-expensive-count-all-queries/
#It will cache the message record bcoz quering all the mesages is pretty time taking operation.
class CachingPaginator(Paginator):
    def _get_count(self):
        if not hasattr(self, "_count"):
            self._count = None
        
        if self._count is None:
            try: 
                key  = "adm:{0}:count".format(hash(self.object_list.query.__str__()))
                self._count = cache.get(key, -1)
                if self._count == -1:
                    self._count = super().count
                    cache.set(key, self._count, 3600)
            except:
                self._count = len(self.object_list)
        return self._count

    count = property(_get_count)
    
    
class PublicChatRoomMessageAdmin(admin.ModelAdmin):
    list_display = ['room', 'user', 'timestamp', 'content']
    list_filter = ['room', 'user', 'timestamp']
    search_fields = ['room__title', 'user']
    readonly_fields = ['id', 'room', 'user', 'timestamp']
    
    show_full_result_count = False
    paginator = CachingPaginator
    
    class Meta:
        model = PublicChatRoomMessage

admin.site.register(PublicChatRoomMessage, PublicChatRoomMessageAdmin)