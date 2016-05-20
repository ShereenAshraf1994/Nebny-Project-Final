from django.db import models
from django.forms import extras
from authentication.models import *

class Installment(models.Model):
	name = models.CharField(max_length=100,null=True,blank=True)
	no_installments_left = models.IntegerField(null=True,blank=True)
	installment_value  = models.IntegerField(null=True,blank=True)
	def __str__(self):
		return self.name


class Home(models.Model):
	building_choices=(
        ('1','طوب متبيض'),
        ('2','طوب احمر'),
        ('3','خشب'),
        ('4','صفيح'),
        ('5','طوب لبن'),
        ('6','اخرى'),
        )
	roof_choices = (
        ('1','اسمنت'),
        ('2','خشب'),
        ('3','قش'),
        ('4','صفيح'),
        ('5','اخرى'),
        )
	floor_choices=(
		('1','سيراميك'),
        ('2','خشب'),
        ('3','بلاط'),
        ('4','اسمنت'),
        ('5','اخرى'),
        )
	boolean_choices=(
		('True','نعم'),
		('False', 'لا'),
		)
	toilet_choices=(
		('1','مشترك'),
		('2','خاص')
		)
	building_status =  models.CharField(max_length=100,choices=building_choices,default='1')
	wall_status = models.CharField(max_length=100,choices=building_choices,default='1')
	roof_status = models.CharField(max_length=100,choices=roof_choices,default='1')
	floor_status = models.CharField(max_length=100,choices=floor_choices,default='1')
	kitchen = models.CharField(max_length=100,choices=boolean_choices,default='True')
	toilet = models.CharField(max_length=100,choices=toilet_choices,default='1')
	sarf_sehy  = models.CharField(max_length=100,choices=boolean_choices,default='True')
	water_shabaka = models.CharField(max_length=100,choices=boolean_choices,default='True')
	electrical_equipments_needed = models.CharField(max_length=1000,null=True,blank=True)
	electrical_equipments_radee2a = models.CharField(max_length=1000,null=True,blank=True)
	furniture_needed = models.CharField(max_length=1000,null=True,blank=True)
	furniture_radee2 = models.CharField(max_length=1000,null=True,blank=True)
	living_rooms_no = models.IntegerField(default=1)
	address = models.CharField(max_length=1000,null=True,blank=True)
	relif_needed = models.CharField(max_length=100,choices=boolean_choices,default='False')

	def __str__(self):
		return self.address

	



class Parent(models.Model):
	name = models.CharField(max_length=3000)
	birthdate = models.CharField(max_length=100,null=True,blank=True)
	age = models.IntegerField(null=True,blank=True)
	boolean_choices=(
		('True','نعم'),
		('False', 'لا'),
		)
	education_choices=(
		('1','غير متعلم'), 
		('2','ابتدائي'), 
		('3','اعدادي'), 
		('4','ثانوية'), 
		('5','بكالريوس'), 
		('6','دبلوم زراعى'), 
		('7','دبلوم تجاري'), 
		('8','دبلوم صناعي'), 
		('9','اخري'), 

		)
	job_choices = (
		('1','دائم'),
		('2', 'متقطع'),
		)
	marital_choices= (
		('1','متزوج'),
		('2','أعزب'),
		('3','مطلق'),
		('4','أرمل'),

		)
	education_level = models.CharField(max_length=100,choices=education_choices,default='1')
	is_3a2el = models.CharField(max_length=100,choices=boolean_choices,default='True')
	job = models.CharField(max_length=100)
	job_status = models.CharField(max_length=100,choices=job_choices,default='1')
	marital_status = models.CharField(max_length=100,choices=marital_choices,default='1')
	national_id = models.IntegerField(null=True,blank=True)
	mobile = models.IntegerField(null=True,blank=True)
	work_choices = (
		('1','ثابت'),
		('2','يومية'),
		('3','اسبوعي'),
		('4','لا يعمل'),
		)
	work_status = models.CharField(max_length=100,choices=work_choices,default='1')
	salary = models.IntegerField(null=True,blank=True)
	is_sick =models.CharField(max_length=100,choices=boolean_choices,default='True')
	disease = models.CharField(max_length=300,null=True,blank=True)
	medecine = models.CharField(max_length=300,null=True,blank=True)
	health_care_expenses = models.IntegerField(null=True,blank=True)
	paid_by_choices=   (
		('1','علي نفقته'),
		('2','التأمين الصحي'),
		('3','متبرع'),
		('4','نفقة الدولة'),
		)
	health_care_paid_by = models.CharField(max_length=100,choices=paid_by_choices,default='1')
	want_kashf = models.CharField(max_length=100,choices=boolean_choices,default='True')
	is_atraf_sena3eya  = models.CharField(max_length=100,choices=boolean_choices,default='False')
	is_3aseel_kalawy  = models.CharField(max_length=100,choices=boolean_choices,default='False')
	is_surgery_needed  = models.CharField(max_length=100,choices=boolean_choices,default='False')
	is_special_needs = models.CharField(max_length=100,choices=boolean_choices,default='False')
	want_project = models.CharField(max_length=100,choices=boolean_choices,default='False')
	project_idea = models.CharField(max_length=1000,null=True,blank=True)
	project_cost = models.CharField(max_length=1000,null=True,blank=True)
	project_profit = models.CharField(max_length=1000,null=True,blank=True)
	project_notes = models.CharField(max_length=3000,null=True,blank=True)
	other_notes = models.CharField(max_length=3000,null=True,blank=True)
	health_care_needed = models.CharField(max_length=100,choices=boolean_choices,default='False')
	education_needed =  models.CharField(max_length=100,choices=boolean_choices,default='False')
	economic_development_needed = models.CharField(max_length=100,choices=boolean_choices,default='False')
	


	def __str__(self):
		return self.name




class Children(models.Model):
	name = models.CharField(max_length=100)
	birthdate = models.CharField(max_length=100)
	education_choices  =(
		('1','حضانة'), 
		('2','1 اب'), 
		('3','2 اب'), 
		('4','3 اب'), 
		('5','4 اب'), 
		('6','5 اب'), 
		('7','6 اب'), 
		('8','1 اع'), 
		('9','2 اع'), 
		('10','3 اع'), 
		('11','1 س'), 
		('12','2 س'), 
		('13','3 س'), 
		('14','جامعة'), 
		('15','خريج'), 
		('16','متسرب'), 

		)
	boolean_choices=(
		('True','نعم'),
		('False', 'لا'),
		)
	education_level = models.CharField(max_length=100,choices=education_choices,default='1')
	school_name = models.CharField(max_length=100)
	doros_number = models.IntegerField(null=True,blank=True)
	doros_choices = (
		('1','مجموعة المدرسة'), 
		('2','درس خصوصي'), 
		)
	doros_type = models.CharField(max_length=100,choices=doros_choices,default='1')
	doros_expenses = models.IntegerField(null=True,blank=True)
	doros_needed = models.CharField(max_length=300,null=True,blank=True)
	is_graduate = models.CharField(max_length=100,choices=boolean_choices,default='1')
	gradutae_degree = models.CharField(max_length=100,null=True,blank=True)
	work_choices=(
		('1','نعم'),
		('2', 'لا'),
		('3', 'في الاجازت'),
		)

	is_worker = models.CharField(max_length=100,choices=work_choices,default='1')
	work = models.CharField(max_length=100,blank=True,null=True)
	salary = models.IntegerField(null=True,blank=True)
	per_choices=(
		('1','أسبوعياً'),
		('2','شهرياً'),
		('3','سنوياً'),
		('4','يوميا'),
		)
	per = models.CharField(max_length=100,choices=per_choices,default='4')
	is_sick =models.CharField(max_length=100,choices=boolean_choices,default='True')
	disease = models.CharField(max_length=300,null=True,blank=True)
	medecine = models.CharField(max_length=300,null=True,blank=True)
	health_care_expenses = models.IntegerField(null=True,blank=True)
	paid_by_choices=   (
		('1','علي نفقته'),
		('2','التأمين الصحي'),
		('3','متبرع'),
		('4','نفقة الدولة'),
		)
	health_care_paid_by = models.CharField(max_length=100,choices=paid_by_choices,default='1')
	want_kashf = models.CharField(max_length=100,choices=boolean_choices,default='False')
	is_atraf_sena3eya  = models.CharField(max_length=100,choices=boolean_choices,default='False')
	is_3aseel_kalawy  = models.CharField(max_length=100,choices=boolean_choices,default='False')
	is_surgery_needed  = models.CharField(max_length=100,choices=boolean_choices,default='False')
	is_special_needs = models.CharField(max_length=100,choices=boolean_choices,default='False')
	health_care_needed = models.CharField(max_length=100,choices=boolean_choices,default='False')
	education_needed =  models.CharField(max_length=100,choices=boolean_choices,default='False')
	economic_development_needed = models.CharField(max_length=100,choices=boolean_choices,default='False')
	relif_needed = models.CharField(max_length=100,choices=boolean_choices,default='False')

	def __str__(self):
		return self.name


class Family(models.Model):
	home = models.ForeignKey(Home,related_name="home",null=True,blank=True)
	father = models.ForeignKey(Parent,related_name="father",null=True,blank=True)
	mother = models.ForeignKey(Parent,related_name="mother",null=True,blank=True)
	children = models.ManyToManyField(Children,related_name="children",blank=True)
	poverty_level = models.IntegerField()
	family_members = models.IntegerField()
	boolean_choices=(
		('True','نعم'),
		('False', 'لا'),
		)
	other_members = models.CharField(max_length=100,choices=boolean_choices,default='False')
	other_notes  = models.CharField(max_length=1000,null=True,blank=True)
	is_member_ommi = models.CharField(max_length=100,choices=boolean_choices,default='1')
	ommi = models.CharField(max_length=100,blank=True,null=True)
	ommi_free_time = models.CharField(max_length=300,null=True,blank=True)
	is_ma3ashat_sho2on_egtma3eya = models.CharField(max_length=100,choices=boolean_choices,default='False')
	is_ma3ashat_ta2meneya=models.CharField(max_length=100,choices=boolean_choices,default='False')
	masader_da5l_choices = (
		('1','جمعيات شرعية'),
		('2','جمعيات خيرية'),
		('3',' اهل الخير'),
		('4','الاقارب'),
		('5','الجيران'),
		('6','اخري'),
		)
	masdar_da5l = models.CharField(max_length=100,choices=masader_da5l_choices,default='1')
	installment = models.ManyToManyField(Installment,related_name="installment",blank=True)
	food_expenses = models.IntegerField(null=True,blank=True)
	transportation_expenses = models.IntegerField(null=True,blank=True)
	education_expenses = models.IntegerField(null=True,blank=True)
	total_health_care_expenses = models.IntegerField(null=True,blank=True)
	electricity_expenses = models.IntegerField(null=True,blank=True)
	water_expenses = models.IntegerField(null=True,blank=True)
	mobile_expenses = models.IntegerField(null=True,blank=True)
	rent_expenses = models.IntegerField(null=True,blank=True)
	gas_expenses =  models.IntegerField(null=True,blank=True)
	smoking_expenses = models.IntegerField(null=True,blank=True)
	is_tamweneya_card =  models.CharField(max_length=100,choices=boolean_choices,default='False')
	no_people_in_tamweneya_card = models.IntegerField(null=True,blank=True)
	member = models.ForeignKey('authentication.Member',related_name="member")
	

	def __str__(self):
   		return self.father

	
	