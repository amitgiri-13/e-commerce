from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=50,unique=True,blank=False,null=False)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.CharField(max_length=100,null=False,blank=False)
    description = models.TextField(max_length=255)
    price = models.DecimalField(decimal_places=2,max_digits=8,blank=False)
    image = models.ImageField(upload_to="store/static/store/images",blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    in_stock = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
        

    def __str__(self):
        return self.product

class Cart(models.Model):
    customer = models.OneToOneField(User,on_delete=models.CASCADE)
  
    def __str__(self):
        return self.customer.username

class CartItems(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    products = models.ForeignKey(Product,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.products.product

    class Meta:
        verbose_name_plural = "Cart Items"


    