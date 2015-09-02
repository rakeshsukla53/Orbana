from django.contrib import admin

# Register your models here.
from .models import Phone, Offender

admin.site.register(Phone)
admin.site.register(Offender)

