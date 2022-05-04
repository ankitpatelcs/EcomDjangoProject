from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.seller_login,name='seller-login'),
    path('seller-login/',views.seller_login,name='seller-login'),
    path('seller-index/',views.seller_index,name='seller-index'),
    path('add-product/',views.add_product,name='add-product'),    
    path('manage-products/',views.manage_products,name='manage-products'),
    path('edit-product/<int:pid>',views.edit_product,name='edit-product'),
    path('delete-product/<int:pid>',views.delete_product,name='delete-product'),
]