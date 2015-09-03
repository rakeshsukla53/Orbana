from django.db import models

# Create your models here.
class Phone(models.Model):

    phone_number = models.IntegerField()
    area_code = models.IntegerField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return '%s' % (self.phone_number)

class Offender(models.Model):

    phone_number = models.IntegerField()
    name = models.CharField(max_length=30, blank=True, default=None)  #blank and null are different
    location = models.CharField(max_length=30, blank=True, default=None)
    person_image = models.ImageField(max_length=300, blank=True, default=None)

    def __unicode__(self):

        return '%s' % (self.phone_number)

class User(models.Model):

    location = models.CharField(max_length=30, blank=True, default=None)

    def __unicode__(self):

        return '%s' % (self.location)

