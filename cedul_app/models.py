from django.db import models

# Create your models here.


class Event(models.Model):
	event_name = models.CharField(max_length=200, blank=False)
	location = models.CharField(max_length=200, blank=True)
	description = models.TextField(blank=True)
	recurring = models.BooleanField(blank=False)
	require_all = models.BooleanField(blank=False)

	def __str__(self):
		return self.event_name + 'at' + self.location


class Attendee(models.Model):
	event = models.ForeignKey(Event, blank=False)
	first_name = models.CharField(max_length=200, blank=False)
	last_name = models.CharField(max_length=200, blank=False)
	email = models.EmailField(blank=True)

class EventTime(models.Model):
	event = models.ForeignKey(Event, blank=False)
	time = models.DateTimeField(blank=False)