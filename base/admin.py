from django.contrib import admin
from .models import sendMessage
from .models import Resume


# Register your models here.
admin.site.register(sendMessage)
admin.site.register(Resume)
