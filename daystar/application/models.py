from django.db import models

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
    stay_duration = models.ForeignKey(Categorystay, on_delete=models.CASCADE, null=True, blank=True)


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

#i cant connect my model items to my views 
# class Item(models.Model):
#     dolls = models.CharField(max_length=50)
#     toys = models.CharField(max_length=50)
#     milk = models.CharField(max_length=50)
#     daipers = models.CharField(max_length=50)
#     babyfood = models.CharField(max_length=50)
#     fruits = models.CharField(max_length=50)
#     date_recieved = models.DateField()


class Item(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    current_stock =models.CharField(max_length=50)
#add sold items class
#how to be able to access some paricular items/objects/attributes from this class in my views and table
class Pay(models.Model):
    payee =  models.ForeignKey(Baby, on_delete=models.CASCADE, null=True, blank=True)
    # payment_sitter = models.ForeignKey(Sitter, on_delete=models.CASCADE, null=True, blank=True)
    payment_cat= models.ForeignKey(Categorystay, on_delete=models.CASCADE, null=True, blank=True)
    pay_number = models.IntegerField(null=True, blank=True)
    amount = models.FloatField( null=True, blank=True)
    date = models.DateTimeField( auto_now_add=True)
    description = models.TextField()





