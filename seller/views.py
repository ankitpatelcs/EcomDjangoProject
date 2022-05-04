
from django.shortcuts import redirect, render

from seller.models import Product, SellerUser


# Create your views here.
def seller_login(request):
    if request.method=='POST':
        #try:            
            obj = SellerUser.objects.get(email=request.POST['email'])
            if request.POST['password']==obj.password:
                request.session['seller'] = request.POST['email']
                return redirect('seller-index') # url name (3rd parameter)
            else:
                return render(request,'seller-login.html',{'msg':'Incorrect password'})
        #except:
            #return render(request,'seller-login.html',{'msg':'email not registered'})

    return render(request,'seller-login.html')

def seller_index(request):
    #request.session['seller'] = 'ankit.patel@tops-int.com'
    return render(request,'seller-index.html')

def add_product(request):
    if request.method=='POST':
        seller = SellerUser.objects.get(email=request.session['seller'])
        if 'pic' in request.FILES:           
            Product.objects.create(
                seller=seller,
                name=request.POST["pname"],
                des=request.POST["des"],
                price=request.POST["price"],
                quantity=request.POST["quantity"],
                pic = request.FILES['pic'],
                discount=request.POST["dis"]
            )
        else:
            Product.objects.create(
                 seller=seller,
                name=request.POST["pname"],
                des=request.POST["des"],
                price=request.POST["price"],
                quantity=request.POST["quantity"],
                #pic = request.FILES['pic'],
                discount=request.POST["dis"]
        )
    return render(request,'add-product.html')

def manage_products(request):
    uid=SellerUser.objects.get(email=request.session['seller'])
    product=Product.objects.filter(seller=uid) # returns list of objects
    return render(request,'manage-products.html',{'uid':uid,'productlist':product})

def edit_product(request,pid):
    product= Product.objects.get(id=pid) # returns 1 object
    return render(request,'edit-product.html',{'product':product})

def delete_product(request,pid):
    return render(request,'delete-product.html')
