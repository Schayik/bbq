from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Event, Meat

# TODO proper error handling


@login_required
def dashboard(request):

    events = Event.objects.filter(user_id=request.user.id)
    user = request.user

    context = {
        'events': events,
        'user': user,
    }

    return render(request, 'dashboard.html', context)


@login_required
def event(request, event_id):
    event = Event.objects.get(pk=event_id)

    if event.user_id != request.user.id:
        messages.error(request, 'That event is not yours')
        return redirect('dashboard')

    meats = Meat.objects.filter(event_id=event_id)

    context = {
        'event': event,
        'meats': meats,
    }

    return render(request, 'event.html', context)


@login_required
def meat(request, event_id):
    if request.method == 'POST':
        type = request.POST['type']

        meat = Meat.objects.create(
            event_id=event_id,
            type=type
        )

    return redirect('/event/' + str(event_id))


def visitor(request):
    return render(request, 'visitor.html')
