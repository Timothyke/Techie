from django.db import models

# Create your models here.
class Contact(models.Model):
    Name=models.CharField(max_length=50)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    def __str__(self):
        return self.Name
    
    
    