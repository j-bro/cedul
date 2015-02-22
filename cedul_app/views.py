from django.shortcuts import render, redirect, get_object_or_404

from cedul_app.models import Event
from cedul_app.forms import EventForm


# Main home page view
def home(request):
	context = None
	return render(request, 'cedul_app/home.html', context)

# Create an event page
def create_event(request):
	if request.method == 'POST':
		### Do stuff here...
		form = EventForm(request.POST)
		if form.is_valid():
			pass
		public_key = None
		return redirect('event', public_key=public_key)
		pass
	else:
		public_key = request.GET.get('public_key')
		if public_key:
			form = EventForm(initial={'public_key': public_key})
		else:
			form = EventForm()
		context = {'public_key': public_key, 'create_event_form': form}
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
