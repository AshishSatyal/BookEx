"""bookex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from bookexapp import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.landingpage, name='landingpage'),
    path('signup/',views.signup, name='signup'),
    path('admin/', admin.site.urls),
    path('bookexapp/', include('bookexapp.urls')),
    path('signin/',views.signin, name='signin'),
    path('add_newsletter/',views.add_newsletter, name='add_newsletter'),
    path('categories/',views.categories, name="categories"),

     path('category-data/', views.categories, name='category-data'),

    # path('password_reset/', auth_views.PasswordResetView.as_view(template_name='bookexapp/password_reset.html')),
    # path('password_reset/', auth_views.PasswordResetCompleteView.as_view(template_name='bookexapp/password_reset.html'),name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='bookexapp/password_reset_done.html'),name='password_reset_done'),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='bookexapp/forgetPassword/password_reset.html',
             subject_template_name='bookexapp/forgetPassword/password_reset_subject.txt',
             email_template_name='bookexapp/forgetPassword/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='bookexapp/forgetPassword/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='bookexapp/forgetPassword/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='bookexapp/forgetPassword/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]