from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime
from django.utils.dateparse import parse_date, parse_time

from .models import Event, Meat, Visitor, Quantity

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

    visitors = Visitor.objects.filter(event_id=event_id)
    visitor_count = visitors.count()
    guest_count = sum(visitors.values_list(
        'number_of_extra_guests', flat=True))

    for meat in meats:
        meat.count = sum(meat.quantities.all(
        ).values_list('quantity', flat=True))

    context = {
        'event': event,
        'meats': meats,
        'visitors': visitors,
        'visitor_link': 'localhost:8000/visitor/' + str(event_id),
        'visitor_count': visitor_count,
        'guest_count': guest_count,
        'total_count': visitor_count + guest_count,
    }

    return render(request, 'event.html', context)


@login_required
def create_event(request):
    if request.method == 'POST':
        title = request.POST['title']
        date = request.POST['date']
        time = request.POST['time']

        print(parse_date(date))
        # print(combine(date, time))

        event = Event.objects.create(
            user_id=request.user.id,
            title=title,
            date_time=datetime.combine(parse_date(date), parse_time(time)),
        )

        return redirect('/event/' + str(event.id))


@login_required
def create_meat(request, event_id):
    if request.method == 'POST':
        type = request.POST['type']

        meat = Meat.objects.create(
            event_id=event_id,
            type=type
        )

    return redirect('/event/' + str(event_id))


def visitor(request, event_id):
    event = Event.objects.get(pk=event_id)
    meats = Meat.objects.filter(event_id=event_id)

    context = {
        'event': event,
        'meats': meats,
    }

    return render(request, 'visitor.html', context)


def create_visitor(request, event_id):
    if request.method == 'POST':
        name = request.POST['name']
        number_of_extra_guests = request.POST['guests']

        visitor = Visitor.objects.create(
            event_id=event_id,
            name=name,
            number_of_extra_guests=number_of_extra_guests,
        )

        for key in request.POST.keys():
            list = key.split('_')
            if list[0] == 'meat':
                Quantity.objects.create(
                    meat_id=list[1],
                    visitor_id=visitor.id,
                    quantity=request.POST[key]
                )

    return redirect('index')
