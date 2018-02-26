# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

import stripe

# Create your models here.
class Subscriber(models.Model):
	user_rec = models.ForeignKey(User)
	address_one = models.CharField(max_length=100)
	address_two = models.CharField(max_length=100, blank=True)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=2)
	stripe_id = models.CharField(max_length=30, blank=True)

	class Meta:
		verbose_name_plural='subscribers'

	def __unicode__(self):
		return u"%s's Subscription Info" % self.user_rec

	def charge(self, request, email, fee):
		stripe.api_key = settings.STRIPE_SECRET_KEY

		#get the credit card details submitted by the form
		token = request.POST['stripeToken']

		#create a customer
		stripe_customer = stripe.Customer.create(
				card=token,
				description=email
			)

		#sve the stripe ID to the customer's profile
		self.stripe_id = stripe_customer.id
		self.save()

		stripe.charge.create(
				amount=fee, #in cents
				currency="usd",
				customer=stripe_customer.id
			)

		return stripe_customer