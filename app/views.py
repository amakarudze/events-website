"""
Definition of views.
"""


from __future__ import absolute_import
from django.views.generic import TemplateView
from django.shortcuts import render, render_to_response
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy
from django.template.loader import render_to_string
from datetime import datetime
from app.models import Category, Provider, Order, ServiceProvider
from app.forms import ContactForm, OrderForm



class HomeView(TemplateView):
    template_name = "app/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = 'Home Page'
        context['year'] = datetime.now().year
        context['categories'] =  Category.objects.all()
        return context


class ContactView(TemplateView):
    template_name = "app/contact.html"
    contact_form = ContactForm()

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        contact_form = ContactForm()
        context['contact_form'] = contact_form
        context['title'] = 'Contact Us'
        context['message'] = 'Our Contact Details'
        context['year'] = datetime.now().year
        return context

    def post(self, request):
        contact_form = ContactForm(request.POST)
        contact_form.save()
        
        to = ['user@example.com']          
        subject = request.POST.get('subject', '')
        details = request.POST.get('message', '')
        email = request.POST.get('email', '')
        phone =  request.POST.get('phone')
        name = request.POST.get('name')

        ctx = {'name': name,
               'phone': phone,
               'email': email,
               'details': details,
               }

        if subject and details and email:
            try:
                message = render_to_string('emails/webenquiry.txt', ctx)
                EmailMessage(subject, message, to=to).send()
                return HttpResponseRedirect('thankyou')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            

    
class AboutView(TemplateView):
    template_name = "app/about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['title'] = 'About Us'
        context['message'] = 'Your application description page.'
        context['year'] = datetime.now().year
        return context

               

"""def home(request):
      assert isinstance(request, HttpRequest)
    
    context = dict()
    context['categories'] =  Category.objects.all()
   
    return render(request,
        'app/index.html', context, 
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year
        })
    )
    
         

def contact(request):
      assert isinstance(request, HttpRequest)
    
    if request.method == "GET":
        contact_form = ContactForm()
        return render(
            request,
            'app/contact.html', {'contact_form': contact_form},
            context_instance = RequestContext(request,
            {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
             })
             )
    elif request.method == "POST":
        form = ContactForm(request.POST);
        form.save()


def about(request):
        assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )"""



class StartView(TemplateView):
    template_name = "app/start.html"

    def get_context_data(self, **kwargs):
        context = super(StartView, self).get_context_data(**kwargs)
        context['title'] = 'Home Page'
        context['year'] = datetime.now().year
        return context


class OrderView(TemplateView):
    template_name = "app/order.html"
    
    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        order_form = OrderForm
        context['order_form'] = order_form
        context['title'] = 'Order Now'
        context['message'] = 'Please fill in the form below.'
        context['year'] = datetime.now().year
        return context

    def post(self, request):
        order_form = OrderForm(request.POST)
        order_form.save()
        
        to = ['anna@anntele.com']          
        subject = request.POST.get('subject', '')
        details = request.POST.get('message', '')
        email = request.POST.get('email', '')
        phone =  request.POST.get('phone')
        name = request.POST.get('name')

        ctx = {'name': name,
               'phone': phone,
               'email': email,
               'details': details,
               }

        if subject and details and email:
            try:
                message = render_to_string('emails/webenquiry.txt', ctx)
                EmailMessage(subject, message, to=to).send()
                return HttpResponseRedirect('thankyou')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            

    
class ThankYouView(TemplateView):
    template_name = "app/thankyou.html"

    def get_context_data(self, **kwargs):
        context = super(ThankYouView, self).get_context_data(**kwargs)
        context['title'] = 'About Us'
        context['message'] = 'Your application description page.'
        context['year'] = datetime.now().year
        return context


class ListView(TemplateView):
    template_name = "app/list.html"

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['title'] = 'Service Provider List'
        context['year'] = datetime.now().year
        context['providers'] =  ServiceProvider.objects.all()
        return context


class DetailsView(TemplateView):
    template_name = "app/details.html"
    
    def get_context_data(self, slug, **kwargs):
        context = super(DetailsView, self).get_context_data(**kwargs)
        context['provider'] = ServiceProvider.objects.filter(slug=slug)
        context['title'] = 'Service Provider Details'
        context['message'] = 'Service Provider Details'
        context['year'] = datetime.now().year
        return context

    
"""    
def start(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/start.html',
        context_instance = RequestContext(request,
        {
            'title':'Start Planning',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )


def list(request, category):
    assert isinstance(request, HttpRequest)
    
    context = dict()
    
    context['providers'] = ServiceProvider.objects.filter(category__category=category)
    

     
    return render(request,
        'app/list.html', context,
        context_instance = RequestContext(request,
        {
            'title':'In this category',
            'year':datetime.now().year
        })
    )


def details(request, slug):
    assert isinstance(request, HttpRequest)

    context = dict()
      
    context['provider'] = ServiceProvider.objects.filter(slug=slug)


    return render(
        request,
        'app/details.html', context,
        context_instance = RequestContext(request,
        {
            'title':'Service Provider Details',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )


def order(request):
    assert isinstance(request, HttpRequest)
    order_form = OrderForm()
        
    return render(
        request,
        'app/order.html', {'order_form': order_form},
        context_instance = RequestContext(request,
        {
            'title':'Order Now',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )  """