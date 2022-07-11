from friends.models import FriendRequest


def get_friend_request_or_404(sender, receiver):
    try:
        friend_request = FriendRequest.objects.get(sender=sender, receiver=receiver, is_active=True)
        return friend_request
    except Exception as ex:
        print(f'''
            friend reqeust does not exist \n
            {ex}
        ''')
        return False