from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import os


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="store/static/store/user_images",blank=True,null=True)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    category = models.CharField(max_length=50,unique=True,blank=False,null=False)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="products")
    product = models.CharField(max_length=100,null=False,blank=False)
    description = models.TextField(max_length=255)
    price = models.DecimalField(decimal_places=2,max_digits=8,blank=False)
    image = models.ImageField(upload_to="store/static/store/images",blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    in_stock = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

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


class Order(models.Model):
    class OrderStatus(models.TextChoices):
        CREATED = "CR","Created"
        DISPATCHED = "DP","Dispatched"
        DELIVERED = "DV","Delivered"
        CANCELED = "CN","Canceled"
        RETURNED = "RTV","Returned"

    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    buyer = models.ForeignKey(User,on_delete=models.CASCADE,related_name="orders")
    order_status = models.CharField(max_length=3,choices=OrderStatus.choices,default=OrderStatus.CREATED)
    payment_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    order_address = models.CharField(max_length=255,null=False,blank=False)
    receiver_name = models.CharField(max_length=100)
    contact_number = models.BigIntegerField(
        validators=[RegexValidator(
            regex=r'^(\+\d{1,3}[- ]?)?\d{10}$',
            message='Enter a valid phone number.',
            code='invalid_phone_number'
        )]
    )
    class Meta:
        ordering = ["-order_date"]

    @property 
    def seller(self):
        return self.product.owner

    @property 
    def total_price(self):
        return self.product.price*self.quantity

    def __str__(self):
        return self.product.product

class Review(models.Model):
    image = models.ImageField(upload_to="store/static/store/reviews",blank=False,null=False )
