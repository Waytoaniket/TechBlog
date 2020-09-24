from django.db import models

# Create your models here.

class Product(models.Model):
    prod_id = models.AutoField
    prod_img = models.ImageField(upload_to="shop",default="")
    prod_name = models.CharField(max_length=50)
    prod_desc = models.CharField(max_length=500,null=True,blank=True)
    prod_color = models.CharField(max_length=10)
    prod_cost = models.IntegerField()

    def __str__(self):
        return self.prod_name

class Video(models.Model):
    vid_img = models.ImageField(upload_to="video",default="")
    Vid_title = models.CharField(max_length=100)
    vid_link = models.CharField(max_length=500)
    def __str__(self):
        return self.Vid_title

class GamingProduct(models.Model):
    gprod_img = models.ImageField(upload_to="gamingsetup",default="")
    gprod_name = models.CharField(max_length=50)
    gprod_cat = models.CharField(max_length=500,blank=True)
    gprod_link = models.CharField(max_length=500,default="",null=True,blank=True)
    gprod_store = models.CharField(max_length=100,default="",null=True,blank=True)
    def __str__(self):
        return self.gprod_name
