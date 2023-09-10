from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import register
# Create your views here.
def registration(request):
    print("come till here")
    if request.method == "POST":
        checkbox = request.POST.get('on')
        if checkbox == 'on':
            FirstName=request.POST.get('fname')
            print("===>",type(FirstName))
            LastName=request.POST.get('lname')
            uname = FirstName + LastName
            Email=request.POST.get('email')
            Password=request.POST.get('password')
            con_pass = request.POST.get('con_password')
            print(uname,Email,Password,con_pass)
            x=User.objects.all()
            print(x)
            try:
                user = User.objects.create_user(username=uname, email=Email, password=Password)
            except:
                print("GIve errpr")
            user.save()
            # registered=User(Firstname=FirstName,Lastname=LastName,email=Email,password=Password)
            # registered.save()
            messages.info(request,"go and login")
            return render(request,'regis/login.html')
        else:
            return HttpResponse("Please check the box")
    return render(request,'regis/registrations.html')

def login_view(request):
    print("comes here")
    if request.method=="POST" :
        fname=request.POST.get('fname')
        pwd=request.POST.get('password')
        print(fname,pwd)
        User = authenticate(username=fname,password=pwd)
        print("------------------------------------->1",User)
        if User is not None:
            print("------------------------------------->2",User)
            # login(request, User)
            request.session['userid'] = User.username
            print("user is secure",request.session['userid'])
            messages.success(request,"congratuation")
            try:
                return render(request,"regis/home.html")
            except Exception as e:
                print("Error is ",e)
    return render(request,"regis/login.html")

def home(request):
    return render(request,'regis/home.html')

