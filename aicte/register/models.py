from django.db import models

from django.contrib.auth.models import AbstractUser
from .manager import ProfileManager
# Create your models here.
    
class Institute(models.Model):
    name=models.CharField(max_length=250,default=" ")
    verified=models.BooleanField(default=True)
    
    def __str__(self) :
        return self.name
    
    
class Developer(AbstractUser):
    email=models.EmailField(unique=True,default=" ")
    phone=models.CharField(max_length=100,unique=True)
    friends = models.ManyToManyField('self', symmetrical=True)
    institute=models.ForeignKey(Institute,on_delete=models.CASCADE,null=True)
    
    REQUIRED_FIELDS=['username','phone']
    USERNAME_FIELD="email"
    
    objects= ProfileManager()
    
    

    

    
    
    
    
 

