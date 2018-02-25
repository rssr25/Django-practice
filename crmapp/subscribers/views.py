# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# This imports the render utility, which takes a template and context dictionary and returns a web response object. It's a shortcut that makes it easy to return the proper content after the view is done processing.
from django.shortcuts import render

#This imports the User model which will be used later in the view to create the user record.
from django.contrib.auth.models import User

#This imports the HttpReseponseRedirect utility. This utility can be used to redirect users to any URL.
from django.http import HttpResponseRedirect

#This imports the SubscriberForm that was created in the previous lesson.
from .forms import SubscriberForm

from .models import Subscriber

# Create your views here.

#This defines the view function that will be used to process requests made to the /signup/ URL. 
#These functions must take in the request object at the very least. Our application defines another object that 
#this function can take; template. If we wanted to use this function to process forms in different templates, 
#we could easily do so by passing in a different template name.

def subscriber_new(request, template='subscribers/subscriber_new.html'):
	if request.method == 'POST':
		#This creates a form object. That's done by passing in request.POST to the SubscriberForm class. Whenever a form is submitted, it's data (i.e. its HTML inputs) can be accessed at request.POST.
		form = SubscriberForm(request.POST)

		if form.is_valid():
			#Unpack form values
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			email = form.cleaned_data['email']
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']

			#create the user record
			user = User(username=username, email = email,
						first_name=first_name, last_name=last_name)
			user.set_password(password)
			user.save()

			#create subscriber record
			address_one = form.cleaned_data['address_one']
			address_two = form.cleaned_data['address_two']
			city = form.cleaned_data['city']
			state = form.cleaned_data['state']
			sub = Subscriber(address_one=address_one, address_two=address_two,
							 city=city, state=state, user_rec=user)

			sub.save()
			#process payment (via Stripe)
			#Auto login the user
			return HttpResponseRedirect('/success/')
	else:
		form = SubscriberForm()

	#This uses the render shortcut to return the request, template, and form to the user. This marks the end of the view processing and is what provides the blank form to the end user.
	return render(request, template, {'form':form})