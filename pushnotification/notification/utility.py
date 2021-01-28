from account.models import User
from .models import NotificationType


def is_owner_user(web, user_id):
    try:
        user = User.objects.get(pk=user_id)
    except:
        return False
    if user.webserver == web.id:
        return True
    return False


def is_owner_notif_type(web, type_id):
    try:
        notif_type = NotificationType.objects.get(pk=type_id)
    except:
        return False
    if notif_type.webserver == web.id:
        return True
    return False
