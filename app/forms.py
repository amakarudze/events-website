"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from app.models import Order, Contact


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


class OrderForm(forms.ModelForm):
    
     class Meta:
        model = Order
        fields = ('name', 'phone', 'email', 'servicerequired', 'serviceprovider', 'details', 'eventdate',)

        def __init__(self, *args, **kwargs):
            super(OrderForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper(self)
            self.helper.form_id = 'order_form'
            self.helper.form_tag = False
            self.helper.form_class = 'form-horizontal'
            
            self.helper.add_input(Submit('order', 'Order Now'))




class ContactForm(forms.ModelForm):
    
     class Meta:
        model = Contact
        fields = ('name', 'phone', 'email', 'subject', 'message',)

        def __init__(self, *args, **kwargs):
        	super(ContactForm, self).__init__(*args, **kwargs)
        	self.helper = FormHelper()
        	self.helper.form_id = 'id-Crispy_ContactForm'
        	self.helper.form_class = 'form-horizontal'
        	self.helper.label_class = 'col-lg-4'
        	self.helper.field_class = 'col-lg-8'
        	self.helper.add_input(Submit('send', 'Send Email'))

