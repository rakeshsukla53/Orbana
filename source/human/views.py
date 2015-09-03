from django.shortcuts import render
from .forms import UserForm

# Create your views here.
def human(request):

    #context is some sort of objects or variables that we want to bring into our project
    title = "Welcome"
    form = UserForm()  #creating instance of the form

    if form.is_valid():   #checking if the form is valid
        instance = form.save(commit=False)
        if not instance.location:
            instance.location = "New York"  #here you can modify your data and decided you want to save it in databbase
        instance.save()  #it will save your data
        print instance.location

    # if request.method == 'POST':
    #     print request.POST #if you want to see the data  #if you want to view the DATA
    if request.user.is_authenticated():   #this is the user authentication method here

        title = "Human Trafficking" + " " + str(request.user)

    context = {'template_title': title, "form": form}

    return render(request, "home.html", context)

