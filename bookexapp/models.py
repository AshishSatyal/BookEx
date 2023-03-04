from django.db import models

# Create your models here.
class NewsletterUsersList(models.Model):
    email = models.EmailField(max_length = 200)
    
    def __str__(self):
        return self.email