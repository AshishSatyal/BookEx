from django.urls import path
from bookexapp import views

# app_name = "bookexapp"

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('landingpage/', views.landingpage, name="landingpage"),
]