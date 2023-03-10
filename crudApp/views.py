from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
import os


def home(request):
    return render(request, 'travel.html')


def createProfile(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        gander = request.POST.get('gander')
        address = request.POST.get('address')
        facebook = request.POST.get('facebook')
        image = request.FILES.get('image')
        if image == None:
            customer = Customer(name=name, email=email, phone_num=phonenumber,
                                gander=gander, address=address, facebook=facebook)
            customer.save()
        else:
            customer = Customer(name=name, email=email, phone_num=phonenumber,
                                gander=gander, address=address, facebook=facebook, image=image)

            customer.save()
    obj = Customer.objects.all()
    context = {
        'profile': obj
    }
    return render(request, 'create_profile.html', context)


def Profile(request, id):
    profile = Customer.objects.get(id=id)
    return render(request, 'profile.html', locals())


def Signin(request):
    return render(request, 'index.html')


def Signup(request):
    return render(request, 'registration.html')


def Delete(request, id):
    pk = id
    obj = Customer.objects.get(id=pk)
    obj.delete()
    # remove old picture -----------
    if obj.image != "default/default.png":
        os.remove(obj.image.path)
    # end----------------------------
    return redirect('createProfile')


def Update(request, id):
    pk = id
    profile = Customer.objects.get(id=pk)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        gander = request.POST.get('gander')
        address = request.POST.get('address')
        facebook = request.POST.get('facebook')
        image = request.FILES.get('image')
        if image == None:
            customer = Customer(id=pk, name=name, email=email, phone_num=phonenumber,
                                gander=gander, address=address, facebook=facebook, image=profile.image)

            customer.save()
            return redirect('createProfile')
        else:
            # remove old picture -----------
            os.remove(profile.image.path)
            # end----------------------------
            customer = Customer(id=pk, name=name, email=email, phone_num=phonenumber,
                                gander=gander, address=address, facebook=facebook, image=image)

            customer.save()
            return redirect('createProfile')
    context = {
        'profile': profile
    }
    return render(request, 'update_profile.html', context)
