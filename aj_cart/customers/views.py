from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from customers.models import Customer
# Create your views here.
def account_show(request):
    try:
        if request.POST and 'register' in request.POST:
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            address=request.POST.get('address')
            phone=request.POST.get('phone')

            # create user account
            user=User.objects.create(
                username=username,
                password=password,
                email=email
            )

            # create customer account
            Customer.objects.create(
                user=user,
                phone=phone,
                email=email
            )
        return redirect('home')

    except Exception as e:
        error_message="Invaid user name"
        messages.error(request,error_message)

    return render(request,'account.html')