from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone



class User(AbstractUser):
    pass


class Category(models.Model):
    
    class Meta:
        verbose_name_plural = "categories"

    id = models.AutoField(primary_key=True)
    categories=models.CharField(max_length=64, default="None")


    def __str__(self):
        return self.categories

class WatchList(models.Model):
    pass
    

class Product(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    author=models.CharField(max_length=100,default="unknow")
    title= models.CharField(max_length=64)
    description= models.TextField()
    startbid= models.PositiveIntegerField(null=True, blank=True)
    imgurl= models.CharField(max_length=200)
    category= models.ForeignKey(Category, on_delete=models.CASCADE, related_name="ctg", default="None")
    active = models.BooleanField()
    email= models.EmailField(max_length=128,null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    title = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='commenttext',null=True)
    comment_text = models.TextField(max_length=392)
    post_date= models.DateTimeField(default=timezone.now()) 

    class Meta:
        ordering = ["post_date"]

    def __str__(self):
        return "Comment \"{}\" of product \'{}'".format(self.comment_text, self.title)



