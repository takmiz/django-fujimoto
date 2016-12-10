from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    return HttpResponse('index page')

def health(request):
    return HttpResponse(json.dumps({'status': 'ok'}), content_type="application/json")
