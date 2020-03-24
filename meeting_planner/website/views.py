from django.http import HttpResponse
from django.shortcuts import render
from meetings.models import Meeting


def welcome(request):
    return render(request, "website/welcome.html", {
        "meetings": Meeting.objects.all(),
    })


def about(unused_request):
    return HttpResponse(f"<h1>About me</h1> \
                          <p>Hi, my name is Mariano. I'm a C# devolper trying to learn some python</p>")
