from django.db import models

# Create your models here.
class UserCreds(models.Model):
    email = models.CharField(max_length=40, null=False, blank=False)
    username = models.CharField(max_length=40, null=False, blank=False)
    password= models.CharField(max_length=25, null=False, blank=False)
    
    def __str__(self):
        return self.username