from django.shortcuts import render
from bookexapp.forms import UserForm
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

        else:
            print(user_form.errors)

    else:
        user_form = UserForm()
    return render(request, 'bookexapp/signup.html',
                            {'user_form':user_form,
                             'signed':signed,
                             })

def signin(request):
    return render(request, 'bookexapp/login.html')

def landingpage(request):
    return render(request, 'bookexapp/landingPage.html')