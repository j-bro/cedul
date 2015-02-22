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
			# Valid form data, save to db
			new_event = form.save()
			public_key = new_event.public_key
			return redirect('event', public_key=public_key)
	# Invalid form, public_key or not
	else:
		public_key = request.GET.get('public_key')
		if public_key:
			if Event.objects.filter(public_key=public_key).exists():
				# Return home if event key already exists
				return redirect('home')
			else:
				form = EventForm(initial={'public_key': public_key})
		else:
			form = EventForm()
			## bug herrreee
	context = {'create_event_form': form}
	return render(request, 'cedul_app/create_event.html', context)

# Event search redirect
def event_redirect(request):
	public_key = request.GET.get('public_key', None)
	try:
	    Event.objects.get(public_key=public_key)
	except Event.DoesNotExist:
		return redirect('home')
	return redirect('event', public_key=public_key)

# Event display page
def event(request, public_key):
	e = get_object_or_404(Event, public_key=public_key)
	context = {'event': e}
	return render(request, 'cedul_app/event.html', context)
