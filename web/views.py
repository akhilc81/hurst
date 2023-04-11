from django.shortcuts import render,redirect
from . models import Product,Contact

# Create your views here.

def index(request):
    context={}
    return render(request,'web/index.html')
def blog(request):
    context={}
    return render(request,'web/blog.html')

def products(request):
    context={
        'product':Product.objects.all()
    }
    return render(request,'web/shop.html', context)

def about(request):
    context={}
    return render(request,'web/about.html', context)

def contact(request):
    
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        message=request.POST.get("messege")
        
        form =Contact(name=name,email=email,message=message)
        form.save()
        
        return redirect('web:contact')
        

    return render(request,'web/contact.html')

def cart(request):
    context={}
    return render(request,'web/cart.html', context)

def checkout(request):
    context={}
    return render(request,'web/checkout.html', context)

def login(request):
    context={}
    return render(request,'web/login.html', context)