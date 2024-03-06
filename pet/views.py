from django.shortcuts import render

from pet.models import student
def index(request):
    return render(request,"index.html")
def admin(request):
    return render(request,"adminmenubar.html")
def petowner(request):
    return render(request,"petownermenubar.html")   
def user(request):
    return render(request,"usermenubar.html")    
def shop(request):
    return render(request,"shopmenubar.html")    
def expert(request):
    return render(request,"expertmenubar.html") 
def boarding(request):
    return render(request,"boardingmenubar.html") 
def public(request):
    return render(request,"publicmenubar.html") 
def addshop(request):
    return render(request,"addshop.html") 
def register(request):
    return render(request,"register.html")
