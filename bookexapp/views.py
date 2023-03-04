from django.shortcuts import render
from bookexapp.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
# from django.http import HttpResponse, HttpResponseRedirect

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
            
            # send_mail(
            #     'Welcome', # subject
            #     'Welcome to our website', # message
            #     'disyou2134@gmail.com',
            #     [user.email],
            #     fail_silently=False,
            # )

            subject = 'Welcome'
            html_content = render_to_string('bookexapp/welcomemail.html',{'name':user.username})
            from_email = 'disyou2134@gmail.com'
            to = user.email
            text_content = strip_tags(html_content)
            email = EmailMultiAlternatives(
                subject,
                text_content,
                from_email,
                [to],   
            )
            email.attach_alternative(html_content,"text/html")
            email.send()

            # return HttpResponseRedirect('/signup/')

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