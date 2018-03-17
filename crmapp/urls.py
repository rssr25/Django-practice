"""crmapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
#admin.autodiscover()
from marketing.views import HomePage
from subscribers.views import subscriber_new
from django.contrib.auth.views import login, logout
from accounts.views import AccountList

urlpatterns = [

		#Marketing pages
		url(r'^$', HomePage.as_view(), name="home"),

		#Subscriber related URLs
		url(r'^signup/$', subscriber_new, name='sub_new'),


		#Admin URL
		url(r'^admin/', admin.site.urls),


		#Login/Logout URLs
		url(r'^login/$', login, {'template_name': 'login.html'}, name="login"), 
		url(r'^logout/$', logout, {'next_page': '/logout/'}, name="logout"),


		#Account related URLs
		url(r'^account/list/$', AccountList.as_view(), name = 'account_list'),


		#Contact related URLs



		#Communication related URLs
	]
