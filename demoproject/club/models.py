from django.db import models

class club_members(models.Model):
   author= models.CharField(max_length=255)
   title = models.CharField(max_length=255)
   content=models.CharField(max_length=255)
   date_posted=models.DateField()

# Create your models here.
