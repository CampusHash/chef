from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext

from django.contrib.auth.models import User
from core.models import Profile

def home(request):
	# If a Chef installation does not exist, redirect to '/register'
	if not Profile.objects.all():
		return redirect('/register/')
	else:
		return render_to_response('index.html')

def chef(request):
	"""
	Chef admin panel.
	"""
	pass

def register(request):
	"""
	Renders the Chef registration page for installation.
	"""

	# Render the registration page template for a GET request
	if request.method == "GET":
		c = RequestContext(request, {})
		return render_to_response('register.html', context_instance=c)

	# Perform new registration for a POST request
	elif request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		# Create a Django super-user first
		chef_superuser = User.objects.create_superuser(username = username,
														password = password, email = "")
		chef_profile = Profile(user = chef_superuser,
								user_type = "ADM")

		chef_profile.save()

		if chef_profile.id:
			print chef_profile.id
			return redirect('/')