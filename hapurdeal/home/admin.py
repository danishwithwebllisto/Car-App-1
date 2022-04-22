from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(WebsiteInfo)
admin.site.register(ContactInfo)

admin.site.register(Profile)


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name','number','email','date','status')
    list_filter = ('name','number','email','date','status')

admin.site.register(ContactMessage, ContactMessageAdmin)

admin.site.register(Seller)
admin.site.register(Order)