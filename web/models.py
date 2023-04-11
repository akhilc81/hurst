from django.db import models

# Create your models here.

class Product(models.Model):
    product_image=models.ImageField( upload_to='products')
    product_name=models.CharField(max_length=50)
    product_price=models.IntegerField()
    
    def __str__(self):
        return self.product_name
    
    
class Contact(models.Model):
    name=models.CharField( max_length=50)    
    email=models.EmailField( max_length=54)
    message=models.CharField( max_length=50)
    
    
    