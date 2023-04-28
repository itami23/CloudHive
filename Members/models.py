from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    class Types(models.TextChoices):
        SUPERVISOR = "SUPERVISOR","Supervisor"
        NORMAL = "NORMAL","Normal"
        EMPLOYEE = "EMPLOYEE","Employee"

    type = models.CharField(max_length=50,choices=Types.choices)


class Supervisor(User):
    class Meta:
        proxy = True

    def save(self,*args,**kwargs):
        if not self.pk:
            self.type = User.Types.SUPERVISOR
            return super().save(*args,**kwargs)
        

class Normal(User):
    class Meta:
        proxy = True
    def save(self,*args,**kwargs):
        if not self.pk:
            self.type = User.Types.NORMAL
            return super().save(*args,**kwargs)


class Employee(User):
    class Meta:
        proxy = True
    def save(self,*args,**kwargs):
        if not self.pk:
            self.type = User.Types.EMPLOYEE
            return super().save(*args,**kwargs)
        








