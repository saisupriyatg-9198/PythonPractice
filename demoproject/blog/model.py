from django.db import models
class MemberDup(models.Model):
   author= models.CharField(max_length=255)
   title = models.CharField(max_length=255)
   content=models.CharField(max_length=255)
   date_posted=models.DateField()