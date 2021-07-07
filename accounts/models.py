from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Admin(models.Model):
    user                = models.OneToOneField(User, on_delete=models.CASCADE, related_name='emp', blank=True, null=True)
    first_name          = models.CharField(max_length=60, blank=False,null=True)
    last_name           = models.CharField(max_length=60, blank= False,null=True)
    phone               = models.BigIntegerField (null=True, blank=True)
    email               = models.EmailField(max_length=70, unique=True, blank=False,null=True)
    status_choice       = (('Active', 'Active'),('Inactive', 'Inactive'))
    status              = models.CharField(max_length=10, default='Active', choices=status_choice) 

    def __str__ (self):
        return str(self.first_name) + ' ' + str(self.last_name)

    @property
    def full_name(self):
        return str(self.first_name) + ' ' + str(self.last_name)