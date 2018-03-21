from django.conf.urls import url
from views import account_detail

account_urls = [

		url(r'^$', account_detail, name = 'account_detail'),
	]