from django.contrib import admin
from friends.models import FriendList, FriendRequest


class FriendListAdmin(admin.ModelAdmin):
    list_display = ('user', )
    search_fields = ('user__username', )
    readonly_fields = ('user', )
    
    class Meta:
        modal = FriendList 

admin.site.register(FriendList, FriendListAdmin)


class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'is_active', 'timestamp')
    search_fields = ('sender__username', 'receiver__username')
    readonly_fields = ('sender', 'receiver', 'is_active', 'timestamp')
    
    class Meta:
        modal = FriendRequest

admin.site.register(FriendRequest, FriendRequestAdmin)