from django.db import models

# Create your models here.


class Event(models.Model):
	event_name = models.CharField(max_length=200, blank=False)
	location = models.CharField(max_length=200, blank=True)
	description = models.TextField(blank=True)
	recurring = models.BooleanField(default=False, blank=False)
	require_all = models.BooleanField(default=False, blank=False)

	def __str__(self):
		return self.event_name


class Attendee(models.Model):
	event = models.ForeignKey(Event, blank=False)
	first_name = models.CharField(max_length=200, blank=False)
	last_name = models.CharField(max_length=200, blank=False)
	email = models.EmailField(blank=True)

	def __str__(self):
		return self.first_name + ' ' + self.last_name

class EventTime(models.Model):
	event = models.ForeignKey(Event, blank=False)
	time = models.DateTimeField(blank=False)

	def __str__(self):
		return str(self.time)