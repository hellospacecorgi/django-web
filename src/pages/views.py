from django.http import HttpResponse
from django.shortcuts import render

# Handling web pages views as functions
def home_view(*args, **kwargs):
	# *args and **kwards are python specific - look it up
	return HttpResponse("<h1>Hello Django!</h1>")

def contact_view(*args, **kwargs):
	return HttpResponse("<h1>Contact Page</h1>")
