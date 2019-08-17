from django.shortcuts import render

from .models import Event, Meat


def dashboard(request):
    events = Event.objects.filter(user_id=request.user.id)

    context = {
        'events': events
    }

    return render(request, 'dashboard.html', context)


def event(request, event_id):
    event = Event.objects.get(pk=event_id)
    meats = Meat.objects.filter(event_id=event_id)

    context = {
        'event': event,
        'meats': meats,
    }

    return render(request, 'event.html', context)


def visitor(request):
    return render(request, 'visitor.html')
