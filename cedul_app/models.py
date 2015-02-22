from django.db import models

# Create your models here.


class Event(models.Model):
	event_name = models.CharField(max_length=200, blank=False)
	public_key = models.CharField(max_length=40)
	location = models.CharField(max_length=200, blank=True)
	description = models.TextField(blank=True)
	recurring = models.BooleanField(default=False)
	unanimity = models.BooleanField(default=False)
	duration_hours = models.IntegerField(blank=False)

	def __str__(self):
		return self.event_name


# Person who is invited to the event
class Attendee(models.Model):
	event = models.ForeignKey(Event, blank=False)
	name = models.CharField(max_length=200, blank=False)
	email = models.EmailField(blank=True)

	def __str__(self):
		return self.name


# Available time slot
# Linked to a single attendee
# Start and end times determine the beginning and end of an available time slot
# Is maybe determines the level of availablility. If true, it works for the attendee but is not an ideal time
class AvailableSlot(models.Model):
	attendee = models.ForeignKey(Attendee, blank=False)
	start_time = models.DateTimeField(blank=False)
	end_time = models.DateTimeField(blank=False)
	is_maybe = models.BooleanField(default=False)

	def __str__(self):
		return str(self.start_time) + ' to ' + str(self.aend_time)
