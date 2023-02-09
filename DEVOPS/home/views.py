from multiprocessing import context
from django.shortcuts import HttpResponse,render
from datetime import datetime
from home.models import Contact
from home.models import Product
from django.contrib import messages

# Create your views here.

'''def index(request):
    return HttpResponse("This is Homepage",request)'''
def home(request):
    return render(request,'index.html')
def pet(request):
    
    return render(request,'pet.html')
def men(request):
    return render(request,'men.html')
def women(request):
    return render(request,'women.html')
def kids(request):
    return render(request,'kids.html')
def appliances(request):
    return render(request,'appliances.html')
def electronics(request):
    return render(request,'electronics.html')
def con(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        ct=request.POST.get('ct')
        num=request.POST.get('num')
        #desc=request.POST.get('desc')
        contact=Contact( email= email, name= name,ct=ct,num=num)
        contact.save()
        messages.success(request, 'Your Message Has been sent')
    return render(request,'cont.html')
def padmin(request):
    if request.method=="POST":
        pid=request.POST.get('pid')
        name=request.POST.get('name')
        details=request.POST.get('details')
        price=request.POST.get('price')
        
        product=Product(pid= pid, name= name,details=details,price=price)
        product.save()
        messages.success(request, 'Your Message Has been sent')

    return render(request,'product.html')

def product(request,pid):
    return render(request,'cont.html')
