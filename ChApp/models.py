from django.db import models
from Members.models import *
# Create your models here.


class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    file_hash = models.CharField(max_length=50,null = True,blank=True)
    file_id = models.CharField(max_length=100,null = True , blank=True)

    def __str__(self):
        return self.title