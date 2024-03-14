from django.db import models

# Create your models here.
class Customer(models.Model):
    Cid=models.IntegerField()
    P_Date=models.DateTimeField()
    Category=models.CharField(max_length=64)
    Price=models.FloatField()
    Quantity=models.IntegerField()
    TPAmt=models.FloatField()
    Payment=models.CharField(max_length=64)
    Returns=models.FloatField()
    Name=models.CharField(max_length=128)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=8)
    Churn=models.IntegerField()

    def __str__(self):
        return self.Name