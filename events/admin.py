from django.contrib import admin

from .models import (
    Event,
    Meat,
    Visitor,
    Quantity,
)


class EventAdmin(admin.ModelAdmin):
    pass


class MeatAdmin(admin.ModelAdmin):
    pass


class VisitorAdmin(admin.ModelAdmin):
    pass


class QuantityAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
admin.site.register(Meat, MeatAdmin)
admin.site.register(Visitor, VisitorAdmin)
admin.site.register(Quantity, QuantityAdmin)
