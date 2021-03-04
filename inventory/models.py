from django.db import models

# Create your models here.

class Device(models.Model): # Device is the table
    type = models.CharField(max_length=100, blank=False) # Name of the column
    price = models.IntegerField()

    # choices is provided by django char field
    choices = (
        ('AVAILABLE', 'Item ready to be purchased'),
        ('SOLD', 'Item Sold'),
        ('RESTOCKING', 'Item restocking in few days')
    )
    status = models.CharField(max_length=10, choices=choices, default="SOLD") # Available, Sold, Restocking
    issues = models.CharField(max_length=100, default="No issues")

    class Meta: 
        abstract = True # Device class will be called out as an abstract class, i.e. wont be migrated to the database

    def __str__(self): # used by the django admin, this string is returned using __str__ method
        return 'Type: {0} Price: {1}'.format(self.type, self.price)

class Laptop(Device):
    pass

class Desktop(Device):
    pass

class Mobile(Device):
    pass

    