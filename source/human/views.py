from django.shortcuts import render
from .forms import UserForm

# Create your views here.
def human(request):

    #context is some sort of objects or variables that we want to bring into our project
    title = "Welcome"
    form = UserForm()  #creating instance of the form
    if request.user.is_authenticated():   #this is the user authentication method here

        title = "Human Trafficking" + " " + str(request.user)

    context = {'template_title': title, "form": form}

    return render(request, "home.html", context)

