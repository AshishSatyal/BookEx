from django.db import models

# Create your models here.
class NewsletterUsersList(models.Model):
    email = models.EmailField(max_length = 200)
    
    def __str__(self):
        return self.email
    
class BestSellerBooks(models.Model):
       img = models.ImageField(upload_to = "static/images/")
       title = models.CharField(max_length=100)
       author = models.CharField(max_length=50)

       def __str__(self):
            return self.title