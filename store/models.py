from django.db import models


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()
    

#i created this class collection before the product so that i can refrece it in prodcut class for one to many relation
class Collection(models.Model):
    collection_title = models.CharField(max_length=255)
    freatured_product = models.ForeignKey('Product',on_delete=models.SET_NULL,null=True,related_name='+')
    
    
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    one_unit_price = models.DecimalField(max_digits=6,decimal_places=2)
    inventory = models.IntegerField()
    last_update= models.DateTimeField(auto_now=True)
    Collection = models.ForeignKey(Collection,on_delete=models.PROTECT)
    promotion = models.ManyToManyField(Promotion)
    
    
    
class Customer(models.Model):
    MEMBERSHIP_BRONZE ='B'
    MEMBERSHIP_SILVER ='S'
    MEMBERSHIP_GOLD ='G'
    
    MEMBERSHIP_CHIOCES = [
  
         (MEMBERSHIP_BRONZE ,'BRONZE'),
         (MEMBERSHIP_SILVER ,'SILVER'),
         (MEMBERSHIP_GOLD ,'GOLD')
        
         
    ]
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField( max_length=50,choices=MEMBERSHIP_CHIOCES,default = MEMBERSHIP_BRONZE)
    

    
    
class Order(models.Model):
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETE = 'C'
    PAYMENT_FAILED = 'F'
    PAYMENT_CHOICES = [
        (PAYMENT_PENDING,'PENDING'),
        (PAYMENT_COMPLETE,'COMPLETED'),
        (PAYMENT_FAILED,'FAILED')
    ]
    placed_at = models.DateTimeField(auto_now=True)
    payment_status = models.CharField(max_length=50,choices=PAYMENT_CHOICES,default=PAYMENT_PENDING)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)
    
    
    
class Adress(models.Model):
    street = models.CharField( max_length=255)
    city = models.CharField(max_length=255)
    customer = models.OneToOneField(Customer,on_delete=models.CASCADE,primary_key=True)
    zip = models.PositiveIntegerField()


    
class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    Product = models.ForeignKey(Product,on_delete=models.PROTECT)
    quantity = models.PositiveBigIntegerField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)
    

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    