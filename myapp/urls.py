from django import views
from django.urls import include, path
from . import views

urlpatterns = [
    path('',views.index, name='index'),  #uses "from . import views"
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('products/',views.products, name='products'),
    path('single/<int:pid>',views.single, name='single'),
    path('add-to-cart/',views.add_to_cart, name='add-to-cart'),
    path('cart/',views.cart, name='cart'),
    path('delete-cart/<int:cid>',views.delete_cart,name='delete-cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('success/',views.success,name='success'),
]
