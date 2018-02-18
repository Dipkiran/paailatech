from django.db import models
from django.forms import ModelForm
from django import forms
from django.shortcuts import reverse
from django.views.generic import CreateView

class sendMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    usermessage = models.CharField(max_length=255)

    def __str__(self):
        return self.usermessage


class Resume(models.Model):
    name = models.CharField(max_length=100, default="",)
    email = models.EmailField(max_length=100, default="")
    doc = models.FileField(default="", verbose_name="Pdf of resume")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('base:resume-detail', kwargs={'pk': self.pk})
        return reverse('base:resume-detail', kwargs={'pk': self.pk})
        # return reverse('base:careers', kwargs={'pk': self.pk})
