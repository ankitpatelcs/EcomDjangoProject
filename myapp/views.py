from django.http import JsonResponse
from django.shortcuts import redirect, render
from myapp.models import *
from seller.models import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        try:
            User.objects.get(email=request.POST['email']) # if return 1 record, then no exception
            return render(request,'register.html',{'msg':'Email already registered'})
        except:
            if request.POST['password']==request.POST['cnfpassword']:
                User.objects.create(
                    name=request.POST['name'],
                    email=request.POST['email'],
                    mobile=request.POST['mobile'],
                    address=request.POST['address'],
                    password=request.POST['password'],
                )
                return render(request,'register.html',{'msg':'User Registration Successful'})
            return render(request,'register.html',{'msg':'Passwords do not match'})
    return render(request,'register.html')


def login(request):
    if request.method=='POST':
        try:
            obj=User.objects.get(email=request.POST['email'])
            if request.POST['password']==obj.password:
                request.session['email']=obj.email
                return redirect('index')
            return render(request,'login.html',{'msg':'Incorrect password'})
        except:
            return render(request,'login.html',{'msg':'email is not registered'})
    return render(request,'login.html')

def products(request):    
    products = Product.objects.all()
    return render(request,'products.html',{'productlist':products})

def single(request,pid):
    productobj = Product.objects.get(id=pid)
    return render(request,'single.html',{'item':productobj})

def add_to_cart(request):
    productobj = Product.objects.get(id=request.GET['pid'])
    userobj=User.objects.get(email=request.session['email'])
    qty=request.GET['qty']
    Cart.objects.create(
        product=productobj,
        quantity=qty,
        user=userobj
    )
    return JsonResponse({'msg':'Addded into Cart'})

def cart(request):
    user = User.objects.get(email=request.session['email'])

    cart = Cart.objects.filter(user=user)
    return render(request,'cart.html',{'cart':cart})

def delete_cart(request,cid):
    #user = User.objects.get(email=request.session['email'])
    #product = Product.objects.get(id=cid)
    cart = Cart.objects.get(id=cid)
    cart.delete()
    return redirect('cart')

def checkout(request):
    userobj = User.objects.get(email=request.session['email'])

    cart = Cart.objects.filter(user=userobj)
    s = 0
    for i in cart:
        s +=  int(i.product.price)

    # print(s)
    order = Order.objects.create(
        user = userobj,
        amount = sgit 
    )
    for i in cart:
        OrderDetails.objects.create(
            product = i.product,
            quantity = 1,
            order = order
        )
    cart.delete()
    return render(request,'success.html')


def success(request):
    return render(request,'success.html')
