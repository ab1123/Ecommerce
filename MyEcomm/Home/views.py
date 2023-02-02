from django.shortcuts import render,HttpResponse

def index(request):
    return render(request,"index.html")
def men(request):
    return render(request,"men.html")
def women(request):
    return render(request,"women.html")
def kids(request):
    return render(request,"kids.html")
def pets(request):
    return render(request,"pets.html")
def others(request):
    return render(request,"others.html")
def electronics(request):
    return render(request,"electronics.html")
