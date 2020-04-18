from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event
# Create your views here.


def event_list(request):
    context = {'events_list': Event.objects.all()}
    return render(request, "events/event_list.html", context)


def event_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EventForm()
        else:
            event = Event.objects.get(pk=id)
            form = EventForm(instance=event)
        return render(request, "events/event_form.html", {'form': form})
    else:
        if id == 0:
            form = EventForm(request.POST)
        else:
            event = Event.objects.get(pk=id)
            form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
        return redirect("/events/list")
    

def event_delete(request, id):
    event = Event.objects.get(pk=id)
    event.delete()
    return redirect("/events/list")
