from django.shortcuts import render
from .forms import UserForm, LocationForm
from django.shortcuts import render
from django.views.generic.edit import View
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from human.models import Phone, State, Organization
from django.core.mail import send_mail
import csv
from django.conf import settings
from django.contrib import messages	
import json

# Create your views here.

def index(request):
	return render(request, "home.html", {})

class form(View):
	template_name = "form.html"
	form = LocationForm

	def get(self, request, *args, **kwargs):
		form = self.form
		return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		
		state_name = request.POST.get('location')
		state = State.objects.get(state_name = state_name)
		count = state.offender_count
		#send_mail('Subject here', 'Here is the message.', 'rishabhranawat12345@gmail.com', ['rdr324@nyu.edu'], fail_silently = False)
		return render(request, "index.html", {'state_name': state_name, 'count': count})

class action(View):

	def get(self, request, *args, **kwargs):
		form = self.form
		return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		
		state_name = request.POST.get('location')
		state = State.objects.get(state_name = state_name)
		problem = state.problem.problem_name
		count = state.offender_count
		
		return render(request, "index.html", {'state': state, 'state_name': state_name, 'problem': problem, 'count': count})


class orgAction(View):

	def get(self, request, state_name,  *args, **kwargs):
		print state_name
		all_objects = Organization.objects.all()
		return render(request, "org_action.html", {})

	def post(self, request, *args, **kwargs):
		return HttpResponse("Okay")


#Map Data Cache
def mapData(request):
	data = {}
	numbers = Phone.objects.all()

	for num in numbers:
		pos = str(num.latitude)+" "+ str(num.longitude)

		if pos not in data:
			data[pos] = [1]
			data[pos]
			data[pos].append([num.phone_number, num.frequency])
		else:
			data[pos][0] = data[pos][0] + 1
			data[pos].append([num.phone_number, num.frequency])

	return HttpResponse(json.dumps(data), content_type = "application/json")

#All Statistics
def economics(request):
	template = "economics.html"
	return render(request, template, {})

def social(request):
	template = "social.html"
	return render(request, template, {})


def organizations(request):
	template = "org.html"
	return render(request, template, {})

def health(request):
	template = "health.html"
	return render(request, template, {})

