from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Product(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    title= models.CharField(max_length=64)
    description= models.TextField()
    startbid= models.PositiveIntegerField(null=True, blank=True)
    imgurl= models.CharField(max_length=200)
    category= models.CharField(max_length=32)
    active = models.BooleanField()
    email= models.EmailField(max_length=128,null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment_autor = models.CharField(max_length=64)
    comment_text = models.TextField()
    post_date= models.DateTimeField() 
     
    def __str__(self):
        return self.comment_autor 

class Bids(models.Model):
    current_bid= models.ForeignKey(Product, on_delete=models.CASCADE, related_name="currentbid")

    def __str__(self):
        return self.current_bid