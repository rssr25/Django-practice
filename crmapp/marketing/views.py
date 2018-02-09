# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic.base import TemplateView

# Create your views here.

class HomePage(TemplateView):
	""" Because our needs are so simple, all we have to do is assign one value; template_name.
	The home.html file we will create as a response to this request"""

	template_name = 'marketing/home.html'