from django.db import models

from django.contrib.auth.models import AbstractUser
from .manager import ProfileManager
# Create your models here.
    
class Institute(models.Model):
    name=models.CharField(max_length=250)
    verified=models.BooleanField(default=True)
    
    def __str__(self) :
        return self.name
    
    
class customuser(AbstractUser):
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=100,unique=True)
    is_authenticated=models.BooleanField(default=False)
    token=models.CharField(max_length=200,null=True)
    
    
    REQUIRED_FIELDS=['username','phone']
    USERNAME_FIELD="email"
    
    objects= ProfileManager()
    # is_educator=models.BooleanField(
    #     default=False)
    
    # is_curr_developer=models.BooleanField(
    #     default=False)
    
    # is_admininstator=models.BooleanField(default=False)'

class Educator(models.Model):
    user=models.OneToOneField(customuser,on_delete=models.CASCADE)
    institute=models.ForeignKey(Institute,on_delete=models.CASCADE)
    
class Developer(models.Model):
    user=models.OneToOneField(customuser,on_delete=models.CASCADE)
    
    

    

    
    
    
    
 

