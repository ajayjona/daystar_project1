from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Categorystay(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
#
    def __str__(self):
        return self.name


class Baby(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    image = models.ImageField(max_length=255)
    broughtby = models.CharField(max_length=200)
    timein = models.DateTimeField(auto_now=True)
    timeout = models.DateTimeField(auto_now=True)
    fees= models.CharField(max_length=100 , null=True, blank=True)
    parent_name = models.CharField(max_length= 200)
    babynumber = models.IntegerField(null=True)
    message_left = models.TextField(max_length=1000)
    stay_duration = models.CharField(choices=(('fullday','fullday'),('halfday', 'halfday')), max_length=50, blank=True, null=True)
   
    
# class daily_operations(models.Model):
    # baby = models.ForeignKey(Baby, on_delete=models.CASCADE)
    # date = 
    # timein= 
    # timeout
    # brought _by
    # stay_duration
    # fees
    # sitter= sitter id

class Sitter(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    image = models.CharField(max_length=255)
    DOB = models.CharField(max_length=200)
    NxtoK = models.CharField(max_length=150)
    NIN = models.CharField(max_length=50, blank=True, null=True)
    recommender = models.CharField(max_length= 200)
    educationlevel = models.CharField(max_length=20)
    sitternumber = models.CharField(max_length=50)
    contact = models.CharField(max_length=20, default=1)
    status = models.CharField(max_length=10, default='Available', blank=True)
    # sit = models.ForeignKey(Baby, on_delete=models.SET_NULL, null=True, related_name='sitters')

class Item(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    current_stock =models.CharField(max_length=50)
    
    
#add sold items class


#how to be able to access some paricular items/objects/attributes from this class in my views and table
class Pay(models.Model):
    baby =  models.ForeignKey(Baby, on_delete=models.CASCADE, null=True, blank=True)
    pay_number = models.IntegerField(null=True, blank=True)
    amount = models.FloatField( null=True, blank=True)
    date = models.DateField( auto_now_add=True)
    # payee = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    stay_duration = models.CharField(max_length=15,default='Fullday', blank=True)
    # pay_status = models.BooleanField(default=0)
    
    def __str__(self):
        return f'payment of {self.amount} made by {self.baby.fname} on {self.date}'
    
    
class Doll_item(models.Model):
    item_name = models.CharField(max_length=100)
    item_description = models.CharField(max_length=100)
    item_quantity = models.IntegerField(default=0)
    date_added = models.DateField(default=timezone.now)
     
    def __str__(self):
        return self.item_name
    
class Doll_transction(models.Model):
    doll_name = models.ForeignKey(Doll_item, on_delete=models.SET_NULL, null=True, blank=True)
    transaction_type = models.CharField(max_length=100, choices=(('buy', 'buy'),('sell', 'sell')))
    transaction_quantity = models.IntegerField(default=0)
    transaction_date = models.DateField(auto_now_add=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.doll_name} {self.transaction_type} {self.transaction_quantity} on {self.transaction_date}'
    
    




