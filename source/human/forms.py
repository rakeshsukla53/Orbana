__author__ = 'rakesh'

#forms are actually your webform which your user will see

from django import forms

from .models import User


class UserForm(forms.ModelForm):

    class Meta:

        model = User
        #Explicity we can define here what all forms are required
        fields = ["location"]
        #exclude use springly

    def clean_location(self):  #clean_name_of_the_field  #validation technique

        #Address validator https://pypi.python.org/pypi/smartystreets.py

        print self.cleaned_data.get("location") #printing out the cleaned data  #add more validator here

        # if not "edu" in email:
        #     raise forms.ValidationError("Please use a valid college address")  #for raising validation error of any kind
        return "California"

class LocationForm(forms.Form):
    location = forms.CharField(max_length = 254)


