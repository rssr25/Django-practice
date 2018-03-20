from django.conf.urls import patters, url

accounts_urls = patterns('', 

		url(r'^$', 'crmapp.accounts.views.account_detail',
				name = 'account_detail'
			),
	)