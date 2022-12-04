from django.shortcuts import render

# Create your views here.

# basic views only to check if it works
# changes will be made as per requirement in the future
def user_signup(request):
    return render(request, 'bookexapp/signup.html')

def landingpage(request):
    return render(request, 'bookexapp/landingPage.html')