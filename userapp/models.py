from django.db import models

# Create your models here.
class reg_tbl(models.Model):
    fname=models.CharField(max_length=25)
    mobile=models.IntegerField()
    email=models.EmailField()
    pssw=models.CharField(max_length=16)
    cpsww=models.CharField(max_length=16)

class Product_tbl(models.Model):
    mbname = models.CharField(max_length=25)
    mbim = models.ImageField(upload_to='pic')
    prc = models.IntegerField()
    dec = models.TextField()

class cart_tbl(models.Model):
    userobj = models.ForeignKey(reg_tbl,on_delete=models.CASCADE)
    prodobj=  models.ForeignKey(Product_tbl,on_delete=models.CASCADE)
    qty=models.PositiveIntegerField(default=1)
