"""Paaila URL Configuration

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

from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # Google verification
    url(r'^google438d2efd8acd56ff.html', TemplateView.as_view(template_name='base/google438d2efd8acd56ff.html')),


    # Admin App
    url(r'^admin/', admin.site.urls),

    # Automatic Dhara
    url(r'^automaticdhara/', include('dhara.urls')),

    # Robotics App
    url(r'^robotics/', include('robotics.urls')),

    # VFD App
    url(r'^vfd/', include('vfd.urls')),

    # Pages that have no apps
    url(r'^', include('base.urls')),

    # Paailablog App
    # url(r'^blog/', include('blog.urls')),
    url(r'^blog/', include("blog.urls", namespace='blog')),

]


# if the DEBUG is on in settings, then append the urlpatterns as below
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

