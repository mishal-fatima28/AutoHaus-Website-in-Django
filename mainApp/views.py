from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import *
# Create your views here.

def index(request):
    allCars = AddCar.objects.all()
    return render(request, 'mainApp/index.html', {'allCars': allCars})


def aboutus(request):
    return render(request, 'mainApp/aboutus.html')

def contactus(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        message = request.POST['message']

        ContactUs.objects.create(name=name,email=email,phone=phone,subject=subject,message=message)
        messages.info(request,'Your Message Has Been Submitted. You Will Hear From Us Soon.')
        return redirect('mainApp-contact')
    else:
        return render(request, 'mainApp/contactus.html')

def sellcar(request):
    
    if request.method == 'POST':
        image = request.POST['img']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        cartype = request.POST['cartype']
        carname = request.POST['carname']
        company = request.POST['company']
        model = request.POST['model']
        mileage = request.POST['mileage']
        kmDriven = request.POST['kmdriven']
        color = request.POST['color']
        price = request.POST['price']

        SellCar.objects.create(image='sellcars/'+image,name=name,email=email,phone=phone,address=address,carType=cartype,carCompany=company,carName=carname,carModel=model,
                               mileage=mileage,color=color,kmDriven=kmDriven,price=price)
        messages.info(request,'Your Car Submitted For Review. It will be posted soon. Thank You for Choosing Buckingham Autohaus.')
        return redirect('mainApp-sellcar')
    else:
        return render(request, 'mainApp/sellcar.html')


def adminmanage(request):
    if request.method == 'POST':
        image = request.POST['img']
        cartype = request.POST['cartype']
        carname = request.POST['carname']
        company = request.POST['company']
        model = request.POST['model']
        mileage = request.POST['mileage']
        kmDriven = request.POST['kmdriven']
        color = request.POST['color']
        price = request.POST['price']
        description = request.POST['description']

        ob = AddCar.objects.create(image='addcars/'+image,carType=cartype,carCompany=company,carName=carname,carModel=model,
                               mileage=mileage,color=color,kmDriven=kmDriven,price=price,description=description)

        messages.info(request,'Your Car Has Been Added To The Stock.')
        return redirect('mainApp-adminmanagepage')

    else:
        return render(request, 'mainApp/adminManagePage.html')


def adminviewmessages(request):
    allmessages = ContactUs.objects.all()

    if allmessages is None:
        messages.info(request,'No Messages to Show.')
        return redirect('mainApp-adminviewmessages')
    else:
        return render(request, 'mainApp/adminViewMessages.html',{'allmessages': allmessages})

def adminviewcars(request):
    sellerCars = SellCar.objects.all()

    if sellerCars is None:
        messages.info(request,'No Cars To Show.')
        return redirect('mainApp-adminviewcars')
    else:
        return render(request, 'mainApp/adminViewCars.html',{'sellerCars': sellerCars})


def cardetails(request,id):
    specCar = AddCar.objects.get(id=id)
    return render(request, 'mainApp/carDetails.html',{'specCar':specCar})

def deletecar(request,id):
    AddCar.objects.filter(id=id).delete()
    return redirect('/')

def deletecustcar(request,id):
    SellCar.objects.filter(id=id).delete()
    return redirect('mainApp-adminviewcars')

def adminlogin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('mainApp-adminmanagepage')
        else:
            messages.info(request,'invalid credentials')
            return redirect('mainApp-adminlogin')
    else:
        if request.user.is_authenticated:
            return render(request, 'mainApp/adminManagePage.html')
        else:
            return render(request, 'mainApp/adminlogin.html')



def adminlogout(request):
    auth.logout(request)
    return redirect('mainApp-adminlogin')