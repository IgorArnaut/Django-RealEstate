from django.contrib import admin

from .models import Ad, Address, Agency, Apartment, Condition, Content, Landlord

# Register your models here.
admin.site.register(Apartment)
admin.site.register(Condition)
admin.site.register(Content)


class AdAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ()})
    )


admin.site.register(Ad)


class LandlordAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'phone',)}),
    )


class AgencyAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'name', 'website', 'registration_date', 'address', 'phone',)}),
    )


admin.site.register(Address)
admin.site.register(Landlord, LandlordAdmin)
admin.site.register(Agency, AgencyAdmin)