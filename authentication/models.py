from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Notification(models.Model):
	message = models.CharField(max_length=3000)
	is_read = models.BooleanField(default = False)
	new_messages = models.IntegerField()

   

def __str__(self):
        return self.name

class Member(models.Model):
	user =  models.ForeignKey(User,related_name='member')
	notification = models.ManyToManyField(Notification,default='no new notifications')
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
	committie = models.ManyToManyField('authentication.Committie',related_name='committie')

	def __str__(self):
		return self.user.username


class Committie(models.Model):
   name = models.CharField(max_length=256)
   head =  models.ForeignKey(Member,related_name='committiehead')
   description = models.CharField(max_length=256)

