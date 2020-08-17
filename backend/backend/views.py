from django.http import JsonResponse


def index(request):
    return JsonResponse({ "status": "I'm here" })
def prueba(request):
    return JsonResponse({ "status": "I'm here2" })    