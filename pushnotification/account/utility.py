from .models import WebServer

def login(name, password):
    try:
        web = WebServer.objects.get(name=name, password=password)
        return web
    except WebServer.DoesNotExist:
        return None