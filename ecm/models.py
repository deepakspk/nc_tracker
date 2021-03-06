from django.db import models
from django.contrib.auth.models import User
from accounts.models import Admin

class UserGroup(models.Model):
    user_group      = models.CharField(max_length=100, unique=True)
    user            = models.ManyToManyField(Admin)
    
    def __str__(self):
        return self.user_group

class Stream(models.Model):
    stream           = models.CharField(max_length=60, blank=False,null=True)
    description      = models.TextField(max_length=6000,null=True, blank=True)
    visibility       = models.ManyToManyField(UserGroup, blank=True)
    def __str__(self):
        return str(self.stream)

# Create your models here.
class Item (models.Model):
    name                = models.CharField(max_length=200, blank=False,null=True)
    stream              = models.ForeignKey(Stream, on_delete= models.CASCADE,related_name='can_stream', null=True, blank=True)
    phone               = models.BigIntegerField (null=True, blank=False)
    email               = models.EmailField(max_length=70, unique=True, blank=False,null=True)
    address             = models.CharField(max_length=290, null=True, blank=True)
    description         = models.TextField(max_length=6000, null=True, blank=True)  
    def __str__(self):
        return str(self.name)


class Step(models.Model):
    stream           = models.ForeignKey(Stream, on_delete= models.CASCADE,related_name='step_stream')
    step             = models.CharField(max_length=60, blank=False,null=True)
    description      = models.TextField(max_length=6000, null=True, blank=True)    
    def __str__(self):
        return str(self.step)

class Status(models.Model):
    stream            = models.ForeignKey(Stream, on_delete= models.CASCADE,related_name='status_stream')
    step              = models.ForeignKey(Step, on_delete= models.CASCADE,related_name='status_step')
    status            = models.CharField(max_length=600, null=True, blank=False)
    def __str__(self):
        return str(self.status)

class Activity(models.Model):
    date            = models.DateField(null=True, blank=True)
    item            = models.ForeignKey(Item, on_delete= models.CASCADE,related_name='activity_can')
    stream          = models.ForeignKey(Stream, on_delete= models.CASCADE,related_name='act_stream')
    step            = models.ForeignKey(Step, on_delete= models.CASCADE,related_name='act_step')
    status           = models.ForeignKey(Status, on_delete= models.CASCADE,related_name='act_status')
    note            = models.TextField(max_length=600, null=True, blank=True)
    added_by        = models.ForeignKey(Admin, on_delete= models.CASCADE,related_name='act_added',null=True, blank=True)
    def __str__(self):
        return str(self.item.name)


class Note(models.Model):
    item            = models.ForeignKey(Item, on_delete= models.CASCADE,related_name='comment_can')
    date            = models.DateField(null=True, blank=True)
    note            = models.TextField(max_length=600, null=True, blank=False)
    comment_by      = models.ForeignKey(Admin, on_delete= models.CASCADE,related_name='emp_comment',null=True, blank=True)  
    def __str__(self):
        return str(self.item)

class Doctype(models.Model):
    name             = models.CharField(max_length=600, blank=False,null=True)
    description      = models.TextField(max_length=6000,null=True, blank=True)
    def __str__(self):
        return str(self.name)

        
class Document(models.Model):
    item             = models.ForeignKey(Item, on_delete= models.CASCADE,related_name='doc_can')
    document_type    = models.ForeignKey(Doctype, on_delete= models.CASCADE,related_name='doc_type')
    title            = models.CharField(max_length=600, blank=False,null=True)
    document         = models.FileField(upload_to='documents/')
    def __str__(self):
        return str(self.document_type)