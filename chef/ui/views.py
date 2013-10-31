from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect

def home(request):
	return render_to_response('index.html')