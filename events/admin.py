from django.contrib import admin

from .models import (
    Event,
    Meat,
    Visitor,
    Quantity,
)


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'date')
    list_display_links = ('id', 'title')


class MeatAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'event')
    list_display_links = ('id', 'type')


class VisitorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'event', 'number_of_extra_guests')
    list_display_links = ('id', 'name')


class QuantityAdmin(admin.ModelAdmin):
    list_display = ('id', 'visitor', 'meat', 'quantity')
    list_display_links = ('id', 'visitor', 'meat')


admin.site.register(Event, EventAdmin)
admin.site.register(Meat, MeatAdmin)
admin.site.register(Visitor, VisitorAdmin)
admin.site.register(Quantity, QuantityAdmin)
