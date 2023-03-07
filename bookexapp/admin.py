from django.contrib import admin
# from bookexapp.models import UserProfileInfo
from .models import NewsletterUsersList,BestSellerBooks
# Register your models here.

admin.site.register(NewsletterUsersList)
admin.site.register(BestSellerBooks)