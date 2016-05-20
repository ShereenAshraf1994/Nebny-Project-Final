from django.db import models
from django.contrib.auth.models import User
from atfaluna.models import *
# Create your models here.

class Member(models.Model):
	user =  models.ForeignKey(User,related_name='member')
	is_head = models.BooleanField(default=False)
	is_UB = models.BooleanField(default=False)
	faculty_choices=(
        ('Pharmacy','Pharmacy'),
        ('Management','Management'),
        ('Engineering','Engineering'),
        ('Applied Arts','Applied Arts'),
        ('Business Informatics','Business Informatics'),
        )
	faculty = models.CharField(max_length=100,choices=faculty_choices,default="Pharmacy")
	is_deleted = models.BooleanField(default=False)
	guc_id = models.CharField(max_length=50)
	committie = models.ForeignKey('authentication.Committie',related_name='committie',blank=True,null=True)
	approved = models.BooleanField(default=False)
	new_messages = models.IntegerField(default=0)
	position_choices =(
		('President','President'),
        ('Core President','Core President'),
        ('Support President','Support President'),
        ('Head','Head'),
        ('Member','Member'),
        )
	position = models.CharField(max_length=100, choices=position_choices,default="Member")

	def __str__(self):
		return self.user.username




class Notification(models.Model):
	message = models.CharField(max_length=3000)
	is_read = models.BooleanField(default = False)
	sender = models.ForeignKey(Member,related_name='notifier',blank=True,null=True)
	reciver = models.ForeignKey(Member,related_name = 'reciver',null=True,blank=True)



	def __str__(self):
		return self.message


class Committie(models.Model):
   name = models.CharField(max_length=256)
   head =  models.ForeignKey('authentication.Member',related_name='committiehead')
   description = models.CharField(max_length=256)
   mother = models.ManyToManyField('atfaluna.Parent',related_name='mothers',blank=True)
   father = models.ManyToManyField('atfaluna.Parent',related_name='fathers',blank=True)
   children = models.ManyToManyField('atfaluna.Children',related_name='child',blank=True)
   home = models.ManyToManyField('atfaluna.Home',related_name='house',blank=True)


   def __str__(self):
   	return self.name

class Core(models.Model):
	description = models.CharField(max_length=1500)
	core_president = models.ForeignKey('authentication.Member',related_name='core_president')
	committies = models.ManyToManyField('authentication.Committie',related_name='core')

class Support(models.Model):
	description = models.CharField(max_length=1500)
	support_president = models.ForeignKey('authentication.Member',related_name='supprt_president')
	committies = models.ManyToManyField('authentication.Committie',related_name='support')
