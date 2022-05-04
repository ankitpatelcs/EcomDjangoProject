from django.contrib import admin
from .models import *
# Register your models here.

#admin.site.register(User)
#admin.site.register(Order)
#admin.site.register(OrderDetails)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','name','mobile','address','email','password',]

@admin.register(Cart)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','product','quantity','user']

@admin.register(Order)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','user','amount','pay_id','order_status']

@admin.register(OrderDetails)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','product','quantity','order']