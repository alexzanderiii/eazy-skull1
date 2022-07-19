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
    
            
def work_single(request):
    return render(request,"work-single.html")

def pricing(request):
    return render(request,"pricing.html")    

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
