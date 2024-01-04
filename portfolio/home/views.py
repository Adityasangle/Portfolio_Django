import email
from django.shortcuts import render, HttpResponse
from home import models


# Create your views here.

def home(request):
    return render(request, 'home.html')


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        ins = models.Contact(name=name, email=email, phone=phone, message=message)
        ins.save()
        print("Data has been saved to DB")
    context = {'name': 'Aditya', 'contact': 8378057460}
    return render(request, 'contact.html', context)


def projects(request):
    return render(request, 'project.html')


def about(request):
    return render(request, 'about.html')
