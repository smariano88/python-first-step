# from django.shortcuts import render
from django.http import HttpResponse
from website.time_class import TimeClass

def welcome(unused_request):
    time = TimeClass()
    return HttpResponse(f"Welcome to the show! \
                        <br/><br/> \
                        <b>Current time is:</b> {time.now()}")
