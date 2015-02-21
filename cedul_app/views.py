from django.shortcuts import render
from django.http import HttpResponse

from cedul_app.models import Event

# Create your views here.

# Main home page view
def home(request):
	return HttpResponse('Welcome to Cedul\'s home page')

def event(request, event_key):
	e = Event.objects.get(pk=event_key)
	return HttpResponse('Page for event %s' % e.event_name)
