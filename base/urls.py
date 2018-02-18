"""
Paaila URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from . import views

app_name = "base"
urlpatterns = [

    # Pages that have no apps
    url(r'^media-and-press/', views.media, name="media"),
    url(r'^ai', views.ai, name="ai"),
    url(r'^$', views.index, name="index"),
    url(r'^about-us', views.aboutus, name="about-us"),
    url(r'^contact-us', views.send_message, name="contact-us"),
    url(r'^base', views.base, name='base'),
    url(r'^message', views.send_message, name='message'),
    # url(r'^djga/', include('google_analytics.urls')),
    # Resumes
    url(r'^careers/$', views.create_resume, name='resume-add'),

]

