from django.contrib import admin
from app.models import Provider, Category, Contact, ServiceProvider

admin.site.register(Contact)
admin.site.register(Provider)
admin.site.register(ServiceProvider)
admin.site.register(Category)
