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







