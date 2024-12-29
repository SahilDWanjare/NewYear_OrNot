from django.shortcuts import render
from django.http import HttpResponse
import datetime

recent = datetime.datetime.now()

# Create your views here.
def index(request):
    return render(request, "diwali/index.html",{
        "NewYear": recent.month == 1 and recent.day==1 ,# if this is true then title var will get a true value and wirtten on the screen 😉
        "year":recent.year,
        "month":recent.month,
        "day":recent.day,
        "hour":recent.hour,
        "minute":recent.minute,
        "second":recent.second,
        "msec":recent.microsecond
    })
