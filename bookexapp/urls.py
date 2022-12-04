from django.urls import path
from bookexapp import views

# app_name = "bookexapp"

url_patterns = [
    path('user_signup/', views.user_signup, name="user_signup"),
    path('landingpage/', views.landingpage, name="landingpage"),
]