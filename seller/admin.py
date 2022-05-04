from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(SellerUser)
#admin.site.register(Product)

@admin.register(Product)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','des','price','quantity','pic','discount','seller']