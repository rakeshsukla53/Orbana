from django.db import models

# Create your models here.

class Problem(models.Model):

    problem_name = models.CharField(max_length = 254, null = True, blank = True)

    PRIORITY_CHOICES = (
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    )
    priority = models.CharField(max_length = 1, choices = PRIORITY_CHOICES)


class State(models.Model):
    state_name = models.CharField(max_length = 254, null = True)
    offender_count = models.IntegerField(default = 0, blank = True)

    def __unicode__(self):
        return '%s' % (self.state_name)

class Phone(models.Model):

    phone_number = models.IntegerField(null = True)
    area_code = models.IntegerField()
    frequency = models.IntegerField(default = 0)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    full_name = models.CharField(null = True, blank = True, max_length = 254)
    state = models.ForeignKey('State', blank = True)

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


