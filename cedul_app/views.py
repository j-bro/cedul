from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect

from cedul_app.models import Event


# Main home page view
def home(request):
	context = None
	return render(request, 'cedul_app/home.html', context)

# Create an event page
def create_event(request):
	public_key = request.GET.get('public_key')
	context = {'public_key': public_key}
	return render(request, 'cedul_app/create_event.html', context)

# Event search redirect
def event_redirect(request):
	public_key = request.GET.get('public_key')
	try:
	    Event.objects.get(public_key=public_key)
	except Event.DoesNotExist:
		## Fix this to stay on home page
		redirect('home')
	return redirect('event', public_key=public_key)

# Event display page
def event(request, public_key):
	e = get_object_or_404(Event, public_key=public_key)
	context = {'event': e}
	return render(request, 'cedul_app/event.html', context)
