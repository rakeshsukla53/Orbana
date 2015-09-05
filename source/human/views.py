from django.shortcuts import render
from .forms import UserForm, LocationForm
from django.shortcuts import render
from django.views.generic.edit import View
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from human.models import Phone, State
import csv

# Create your views here.
class index(View):
	template_name = "home.html"
	form = LocationForm

	def get(self, request, *args, **kwargs):
		form = self.form
		return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		
		state_name = request.POST.get('location')
		state = State.objects.get(state_name = state_name)
		count = state.offender_count
		
		return render(request, "visualise_data.html", {'state_name': state_name, 'count': count})

class action(View):

	def get(self, request, *args, **kwargs):
		form = self.form
		return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		
		state_name = request.POST.get('location')
		state = State.objects.get(state_name = state_name)
		problem = state.problem.problem_name
		count = state.offender_count
		
		return render(request, "visualise_data.html", {'state_name': state_name, 'problem': problem, 'count': count})







