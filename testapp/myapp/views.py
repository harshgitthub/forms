from django.shortcuts import render  , HttpResponse
from myapp.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    # return HttpResponse("this is homepage")
    return render(request ,'index.html')

def contact(request):
    # return HttpResponse("this is contact")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = Contact(name=name , email=email)
        contact.save()    
    return render(request,'contact.html')


