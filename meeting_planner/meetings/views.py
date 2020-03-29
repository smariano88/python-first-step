#from django.forms import modelform_factory
from django.shortcuts import get_object_or_404, redirect, render

from meetings.models import Meeting, Room
from .forms import MeetingForm


def meeting_detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/meeting_detail.html", {"meeting": meeting})


def room_list(request):
    rooms = Room.objects.all()
    return render(request, "meetings/room_list.html", {"rooms": rooms})


# MeetingForm = modelform_factory(Meeting, exclude=[])


def new_meeting(request):
    if request.method == "POST":
        meeting_form = MeetingForm(request.POST)
        if meeting_form.is_valid():
            meeting_form.save()
            return redirect("home")
    else:
        meeting_form = MeetingForm()

    return render(request, "meetings/new_meeting.html", {"form": meeting_form})
