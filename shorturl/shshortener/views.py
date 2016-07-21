from django.shortcuts import render
from django.core.context_processors import csrf
from django.conf import settings
from django.shortcuts import render_to_response
from shshortener.models import Links
import random, string, json
from django.http import HttpResponseRedirect, HttpResponse
 
def index(request):
    con = {}
    con.update(csrf(request))
    return render_to_response('shshortener/index.html', con)
 
def go_to_original(request, shorter):
    url = Links.objects.get(pk=shorter)
    return HttpResponseRedirect(url.original)

def short():
    length = 4
    i = string.ascii_uppercase + string.digits + string.ascii_lowercase
    while True:
        shorter = ''.join(random.choice(i) for x in range(length))
        try:
            var = Links.objects.get(pk=shorter)
        except:
            return shorter
 
def shorten(request):
    url = request.POST.get("url", '')
    if not (url == ''):
        shorter = short()
        link = Links(original=url, shorter=shorter)
        link.save()
 
        response_data = {}
        response_data['url'] = settings.SITE_URL + "/" + shorter
        return HttpResponse(json.dumps(response_data),  content_type="application/json")
    return HttpResponse(json.dumps({"error": "error occurs"}), content_type="application/json")
