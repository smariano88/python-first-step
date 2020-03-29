from django.forms import modelform_factory
from django.shortcuts import get_object_or_404, render
from meetings.models import Meeting, Room


def meeting_detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/meeting_detail.html", {"meeting": meeting})


def room_list(request):
    rooms = Room.objects.all()
    return render(request, "meetings/room_list.html", {"rooms": rooms})


MeetingForm = modelform_factory(Meeting, exclude=[])


def new_meeting(request):
    form = MeetingForm()
    return render(request, "meetings/new_meeting.html", {"form": form})
