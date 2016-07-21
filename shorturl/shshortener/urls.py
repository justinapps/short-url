from django.conf.urls import url, include
from .views import index

urlpatterns = [
    		url(r'^$', 'index', name='home'),
    		url(r'^(?P<shorter>\w{4})$', 'go_to_original', name='gotoorig'),
    		url(r'^makeshort/$', 'shorten', name='shorten'),
]