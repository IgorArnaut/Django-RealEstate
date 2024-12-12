from django.contrib import admin

from .models import Agency, Apartment, Condition, Content, Landlord

# Register your models here.
admin.site.register(Apartment)
admin.site.register(Condition)
admin.site.register(Content)
admin.site.register(Agency)
admin.site.register(Landlord)