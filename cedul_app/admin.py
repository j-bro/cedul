from django.contrib import admin

from cedul_app.models import Event, Attendee, AvailableSlot


class AttendeeInline(admin.TabularInline):
	model = Attendee
	extra = 3

class AvailableSlotInline(admin.TabularInline):
	model = AvailableSlot
	extra = 3

class EventAdmin(admin.ModelAdmin):
	inlines = [AttendeeInline]
	list_display = ('event_name', 'public_key', 'location', 'description')

class AttendeeAdmin(admin.ModelAdmin):
	inlines = [AvailableSlotInline]
	list_display = ('name', 'email', 'event')

# Register your models here.
admin.site.register(Event, EventAdmin)
admin.site.register(Attendee, AttendeeAdmin)
