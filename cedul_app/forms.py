from django.forms import ModelForm

from cedul_app.models import Event

class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ['public_key', 'event_name', 'location', 'description',
			'recurring', 'unanimity', 'duration_hours']