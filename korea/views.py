from django.http.response import HttpResponse
from django.shortcuts import render
import datetime
from .models import Bob
from datetime import date, datetime
import crawl

# Create your views here.
def bab(request):
    bab = Bob.objects.order_by('-end').first()

    if not (bab and bab.end.date() >= date.today()):
        image = crawl.get_bob_image()
        start, end = crawl.get_bob_period()
        if not (bab and bab.end.date() != end.date()):
            Bob(start=start, end=end, image=image).save()

    bab = Bob.objects.order_by('-end').first()
    data = {
        'image': bab.image,
        'start': bab.start.date(),
        'end': bab.end.date(),
    }
    return render(request, 'korea/bab.html', data)