from django.contrib import admin

from cedul_app.models import Event, Attendee, EventTime

# Register your models here.
admin.site.register(Event)
admin.site.register(Attendee)
admin.site.register(EventTime)