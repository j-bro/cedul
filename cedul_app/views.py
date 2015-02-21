from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from cedul_app.models import Event

# Create your views here.

# Main home page view
def home(request):
	context = None
	return render(request, 'cedul_app/home.html', context)

# event display page
def event(request, event_key):
	e = get_object_or_404(Event, pk=event_key)
	attendees = e.attendee_set.all()
	context = {'event': e, 'attendees': attendees}
	return render(request, 'cedul_app/event.html', context)
