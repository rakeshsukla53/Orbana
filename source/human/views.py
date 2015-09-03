from django.shortcuts import render
from .forms import UserForm
from django.shortcuts import render
from django.views.generic.edit import View
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import csv

# Create your views here.
class index(View):
	template_name = "home.html"

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {})

	def post(self, request, *args, **kwargs):

		'''
		numbers = {}

		whitespace = " "

		with open('output.txt', 'r') as file:
		    reader = csv.reader(file)
		    for row in reader:
		        for each in row:
		            number = int(each)

		            if number not in numbers:
		                numbers[number] = 1
		            else:
		                numbers[number] = numbers[number] + 1

		high = {}
		        
		for i in numbers:
		    if (numbers[i] >= 5):
		        high[i] = numbers[i]

		'''
		

		return render(request, "visualise_data.html", {})










