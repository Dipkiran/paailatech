from django.shortcuts import render
from django.http import HttpResponse
from base.custom_forms import ContactForm


# Create your views here.
def index(request):
    form_base = ContactForm
    form = form_base()
    return render(request, 'robotics/robotics.html', {'form':form})

def gallery(request):
    return render(request, 'robotics/galleryModern.html')


def pari(request):
    return render(request, 'robotics/pari.html')


def waiter(request):
    return render(request, 'robotics/waiter.html')


def roomservice(request):
    return render(request, 'robotics/room-service.html')


