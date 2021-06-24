from django.shortcuts import render
from time import gmtime, strftime, localtime
    
def index(request):
    context = {
        "time_utc": strftime("%A, %b %d, %Y %H:%M %p", gmtime()),
    }
    return render(request,'index.html', context)