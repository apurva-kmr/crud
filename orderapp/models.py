from django.db import models

# Create your models here.
class Login(models.Model):
    Coustumer_id=models.IntegerField()
    Email_id=models.CharField(max_length=64)
    Pass=models.CharField(max_length=64)
    Attempts=models.IntegerField()
    Locked=models.IntegerField()


class Coustumer(models.Model):
    Transaction_ID=models.IntegerField()
    Customer_ID=models.IntegerField()
    Transdate=models.DateField()
    Cfname=models.CharField(max_length=64)
    Clname=models.CharField(max_length=64)
    Country=models.CharField(max_length=64)
    Ccity=models.CharField(max_length=64)
    Product=models.CharField(max_length=64)
    Qty=models.IntegerField()
    Amount=models.IntegerField()
