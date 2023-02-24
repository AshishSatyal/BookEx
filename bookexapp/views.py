from django.shortcuts import render
from bookexapp.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings 
# Create your views here.

# basic views only to check if it works
# changes will be made as per requirement in the future
def signup(request):
    signed = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password) # hashing the password
            user.save()

            signed = True

            
            send_mail(
                'Welcome', # subject
                'Welcome to our website', # message
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )


        else:
            print(user_form.errors)

    else:
        user_form = UserForm()
    return render(request, 'bookexapp/signup.html',
                            {'user_form':user_form,
                             'signed':signed,
                             })

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse('Logged in')
        
        else:
            # messages.error(request,"Incorrect Credentials")
            return HttpResponse('Incorrect Credentials')

    return render(request, 'bookexapp/login.html')

def landingpage(request):
    return render(request, 'bookexapp/landingPage.html')