from django.db import models

# Create your models here.
class Phone(models.Model):

    phone_number = models.IntegerField()
    area_code = models.IntegerField()
    latitude = models.FloatField(max_length=20, null=True)
    longitude = models.FloatField(max_length=20, null=True)
    location = models.CharField(max_length=30, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.phone_number

class Offender(models.Model):

    phone_number = models.IntegerField()
    name = models.CharField(max_length=30, null=True)  #blank and null are different
    location = models.CharField(max_length=30, null=True)
    person_image = models.ImageField(max_length=300, null=True)

    def __unicode__(self):

        return self.phone_number

