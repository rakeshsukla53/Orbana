from django.shortcuts import render

# Create your views here.
def human(request):

    return render(request, "home.html", {})

