from django.shortcuts import render,HttpResponse
from .models import Product,Contact
from math import ceil
# Create your views here.

def index(request):
    # product_details=Product.objects.all()
    # print(product_details)
    # n=len(product_details)
    allprods = []
    catproduct = Product.objects.values('category','id')
    cats = {item['category'] for item in catproduct}
    for cat  in cats:
        print(cat)
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n//4 + ceil((n/4)-(n//4))
        print("allprods",nslides)
        allprods.append([prod,range(1,nslides),nslides])
        params = {'allProds':allprods}
    # print(nslides)
    # param = {'no of slides':nslides,'product':product_details,'range':range(1,nslides)}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name',default="")
        email=request.POST.get('email',default="")
        phone=request.POST.get('phone',default="")
        desc=request.POST.get('desc',default="")
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request,myid):
    product=Product.objects.filter(id=myid)
    print("-------------->",product)
    return render(request, 'shop/prodView.html',{'product':product[0]})

def checkout(request):
    return render(request, 'shop/checkout.html')