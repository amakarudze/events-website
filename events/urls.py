"""
Definition of urls for events.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
from app.views import AboutView, ContactView, HomeView, DetailsView, ListView, ThankYouView, OrderView, StartView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^about/', AboutView.as_view(), name='about'),
    url(r'^contact$', ContactView.as_view(), name='contact'),
    url(r'^start', StartView.as_view(), name='start'),
    url(r'^Category/(?P<category>\w+)', ListView.as_view(), name='list'),
    url(r'^Provider/(?P<slug>\w+)', DetailsView.as_view(), name='details'),
    url(r'order$', OrderView.as_view(), name='order'),
    url(r'thankyou$', ThankYouView.as_view(), name='thankyou'),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
