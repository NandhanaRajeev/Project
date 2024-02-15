from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .models import contactus


# Create your views here.
def homeindex(request):
    return render(request, 'home/homeindex.html')

# def login_user(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username = username, password = password)
#         if user is not None and user.is_active:
#             if user.is_staff == True and user.is_superuser == False:
#                 login(request, user)
#                 return redirect('homeindex')
#             if user.is_staff == False and user.is_superuser == True:
#                 login(request, user)
#                 return redirect('homeindex')
#         else:
#             msg = "Wrong Credentials! Please try again!"
#             return render(request, 'home/login.html', {'msg':msg})
#     return render(request, 'home/login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            if user.is_superuser:
                return redirect('adminindex')
            elif user.is_staff:
                return redirect('adminstaff')
            else:
                msg = "You are not autherized for this login"
                return render(request, 'home/adminstudent.html', {'msg': msg})
        else:
            msg = "Invalid Credentials. Please try again!"
            return render(request, 'home/login.html', {'msg': msg})
    return render(request, 'home/login.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        ctct = contactus.objects.create(name=name, email=email,phone=phone, message=message)
        ctct.save()
        return redirect('contacts')
    return render(request, 'home/contacts.html')
    
def adminindex(request):
    ctct = contactus.objects.all()
    context = {
        'ctct' : ctct,
    }
    return render(request, 'admin/adminindex.html')

def adminstaff(request):
    return render(request, 'admin/adminstaff.html')

def adminstudent(request):
    return render(request, 'admin/adminstudent.html')

def logout(request):
    return redirect("login")





