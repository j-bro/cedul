from django.contrib import admin

from cedul_app.models import Event, Attendee, EventTime


class AttendeeInline(admin.TabularInline):
	model = Attendee
	extra = 3

class EventTimeInline(admin.TabularInline):
	model = EventTime
	extra = 3

class EventAdmin(admin.ModelAdmin):
	inlines = [AttendeeInline, EventTimeInline]
	list_display = ('event_name', 'id', 'location', 'description')

# Register your models here.
admin.site.register(Event, EventAdmin)
admin.site.register(Attendee)
admin.site.register(EventTime)