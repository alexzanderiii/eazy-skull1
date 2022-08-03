from django.shortcuts import render
from django.http import HttpResponse  

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")
        
def work(request):
    return render(request,"work.html")
    
            
def clearance(request):
    return render(request,"clearance.html")

def registration(request):
    return render(request,"registration.html")    

def exam(request):
    return render(request,"exam.html") 

def project(request):
    return render(request,"project.html")    

def form_group(request):
    return render(request,"form_group.html")    

def form_individual(request):
    return render(request,"form_individual.html") 

def orientation(request):
    return render(request,"orientation.html")              

def howto(request):
    return render(request,"howto.html")    

def profile(request):
    return render(request,"profile.html")        

def signup(request):
    return render(request,"signup.html")

def signin(request):
    return render(request,"signin.html")    

def OT_search(request):
    return render(request,"OT_search.html")

def account_settings(request):
    return render(request,"account_settings.html")

def account(request):
    return render(request,"account.html")                    
