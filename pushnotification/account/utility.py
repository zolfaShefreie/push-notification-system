from .models import WebServer

def login(name, password):
    try:
        web = WebServer.objects.get(name=name)
        if web.check_password(password):
            return web
    except WebServer.DoesNotExist:
        pass
    return None