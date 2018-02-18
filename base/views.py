from django.shortcuts import render
from .models import sendMessage
from .models import Resume
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .custom_forms import ContactForm, ApplicationForm
from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage


def index(request):
    return render(request, 'base/index.html')

def base(request):
    return render(request, 'base/base.html')

def aboutus(request):
    form_base=ContactForm
    form=form_base()
    return render(request, 'base/about-us.html', {'form':form})

def ai(request):
    form_base=ContactForm
    form=form_base()
    return render(request, 'robotics/ai.html', {'form':form})


def media(request):
    return render(request, 'robotics/media.html')

def careers(request):
    return render(request, 'base/careers.html')

def contactus(request):
    return render(request, 'base/contact-us.html')

def send_message(request):
    form_base = ContactForm
    if request.method == "POST":
        form = form_base(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            user = sendMessage()
            user.usermessage = message
            user.email = email
            user.name = name
            user.save()

            template = get_template('base/contact_template.txt')
            context = Context({
                'sender_name': name,
                'sender_email': email,
                'message': message,
            })

            content = template.render(context)
            email = EmailMessage("Inquiry from paailatechnology.com",
                                 content,
                                 "dummypaaila@gmail.com",
                                 ['paailatechnology@gmail.com'],
                                 headers={'Reply-To': email})

            try:
                email.send()
                status = "Your message has been sent successfully"
            except:
                status = "There was a problem sending your message"

            return render(request, 'base/emailform.html',
                          {'form': form, 'status': status})

        else:
            return render(request, 'base/emailform.html',
                          {'form': form, 'status': "Please check your form for possible errors"})

    else:
        form = form_base()
        return render(request, 'base/contact-us.html', {'form': form})


# Detail view for resume
class ResumeDetailView(generic.DetailView):
    model = Resume
    context_object_name = 'resume'
    template_name = 'base/detailResume.html'


# Seeing all the resumes recieved
class ResumeIndex(generic.ListView):
    template_name = 'music/resume.html'
    context_object_name = 'all_resume'

    def get_queryset(self):
        return Resume.objects.all()


# Form for filling resume information
class ResumeCreate(CreateView):
    model = Resume
    fields = ['name', 'email', 'doc']
    template_name = 'base/careers.html'


def create_resume(request):
    form_base = ApplicationForm
    if request.method == "POST":
        form = form_base(request.POST, request.FILES)

        name = request.POST['name']
        email = request.POST['email']
        doc = request.FILES['doc']

        resume = Resume()
        resume.doc = doc
        resume.email = email
        resume.name = name
        resume.save()

        template = get_template('base/resume_template.txt')
        context = Context({
            'sender_name': name,
            'sender_email': email,

        })

        content = template.render(context)
        email = EmailMessage("Application from paailatechnology.com",
                             content,
                             "newsangamdummy@gmail.com",
                             ['paailatechnology@gmail.com'],
                             headers={'Reply-To': email})

        try:
            email.send()
            status = "Your application has been sent successfully"
        except:
            status = "There was a problem sending your application"

        return render(request, 'base/resumeform.html',
                      {'form': form, 'status': status})

#        else:
#            return render(request, 'base/resumeform.html',
#                          {'form': form, 'status': "Please check your form for possible errors"})

    else:
        form = form_base()
        return render(request, 'base/careers.html', {'form': form})
