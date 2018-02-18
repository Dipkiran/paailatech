from django.shortcuts import render
from base.custom_forms import ContactForm
# Create your views here.

def index(request):
    form_base=ContactForm
    form=form_base()
    return render(request, 'dhara/automaticdhara.html', {'form':form})


def header(request):
    return render(request, 'dhara/header.html')

def footer(request):
    return render(request, 'dhara/footer.html')

