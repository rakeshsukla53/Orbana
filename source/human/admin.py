from django.contrib import admin

# Register your models here.
from .models import Phone, Offender


class PhoneAdmin(admin.ModelAdmin):

    class Meta:

        model = Phone


class OffenderAdmin(admin.ModelAdmin):

    class Meta:

        model = Offender

admin.site.register(Phone, PhoneAdmin)
admin.site.register(Offender, OffenderAdmin)




