from django.shortcuts import render
from django.views.generic import FormView, TemplateView,View, UpdateView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView,View, UpdateView, ListView, DeleteView
from django.views.generic.detail import DetailView
from authentication.forms import UserForm
from django.contrib.auth.forms import UserCreationForm
from authentication.models import *
from atfaluna.models import *
from django.core import serializers






class CreateChildren(CreateView):
	model = Children
	template_name= 'create_children.html'
	fields=['name','birthdate','education_level','school_name','doros_number','doros_type','doros_expenses','doros_needed','is_graduate',
		'gradutae_degree','is_worker','salary','per','is_sick','disease','medecine','health_care_expenses','health_care_paid_by','want_kashf',
		'is_atraf_sena3eya','is_3aseel_kalawy','is_surgery_needed','is_special_needs','health_care_needed','education_needed','economic_development_needed',
		'relif_needed']

	def post(self,request,*args,**kwargs):
		form=self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return JsonResponse({'err_List':self.get_form().errors,'success':0})

	def form_valid(self, form):

		form.save()
	
		
		#user = User1.objects.get(id)
		#form.Product.use1 = user
		#form.instance.employee.user= self.request.user
		return super(CreateChildren, self).form_valid(form)
	def get_success_url(self):
		family = Family.objects.get(id=self.kwargs['pk'])
		father1 = Parent.objects.get(id=self.kwargs['id'])
		mother1 = Parent.objects.get(id=self.kwargs['mid'])
		home1 = Home.objects.get(id = self.kwargs['hid'])
		installment1 = Installment.objects.get(id = self.kwargs['insid'])
		children_id1=self.object.pk
		family.mother = mother1
		family.father = father1
		family.installment.add(installment1)
		family.home=home1
		family.children.add(self.object)
		family.save()

		#sending notifications to committies
		health_care_committie = Committie.objects.get(name='Health care')
		health_care_members = Member.objects.filter(committie=health_care_committie)
		education_committie = Committie.objects.get(name='Education')
		education_members = Member.objects.filter(committie=education_committie)
		relif_committie = Committie.objects.get(name='Relif')
		relif_members = Member.objects.filter(committie=relif_committie)
		economic_development_committie = Committie.objects.get(name='Economic development')
		economic_members = Member.objects.filter(committie=economic_development_committie)
		member=Member.objects.get(user=self.request.user)

		#sending notifications to healtch care
		if (self.object.health_care_needed == 'True' ):
			notification = Notification()
			notification.message="You have new ba7s hala"
			for m in health_care_members:
				notification.reciver=m
				notification.sender=member
				m.new_messages+=1
				m.save()
				notification.save()
			health_care_committie.children.add(self.object)
			health_care_committie.save()
		#sendinng notifications to education
		if(self.object.education_needed == 'True'):
			notification = Notification()
			notification.message="You have new ba7s hala"
			notification.save()
			for m in education_members:
				notification.reciver=m
				notification.sender=member
				m.new_messages+=1
				m.save()
				notification.save()
			education_committie.children.add(self.object)
			education_committie.save()
		#sending to economic
		if(self.object.economic_development_needed == 'True'):
			notification = Notification()
			notification.message="You have new ba7s hala"
			notification.save()
			for m in economic_members:
				notification.reciver=m
				notification.sender=member
				m.new_messages+=1
				m.save()
				notification.save()
			economic_development_committie.children.add(self.object)
			economic_development_committie.save()
		#sending to relif
		if(self.object.relif_needed == 'True'):
			notification = Notification()
			notification.message="You have new ba7s hala"
			notification.save()
			for m in relif_members:
				notification.reciver=m
				notification.sender=member
				m.new_messages+=1
				m.save()
				notification.save()
			relif_committie.children.add(self.object)
			relif_committie.save()

		return reverse('family-details', kwargs={'pk':family.id})

class AddChildren(CreateView):
	model = Children
	template_name= 'create_children.html'
	fields=['name','birthdate','education_level','school_name','doros_number','doros_type','doros_expenses','doros_needed','is_graduate',
		'gradutae_degree','is_worker','salary','per','is_sick','disease','medecine','health_care_expenses','health_care_paid_by','want_kashf',
		'is_atraf_sena3eya','is_3aseel_kalawy','is_surgery_needed','is_special_needs','health_care_needed','education_needed','economic_development_needed',
		'relif_needed']

	def post(self,request,*args,**kwargs):
		form=self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return JsonResponse({'err_List':self.get_form().errors,'success':0})

	def form_valid(self, form):

		form.save()
	
		
		#user = User1.objects.get(id)
		#form.Product.use1 = user
		#form.instance.employee.user= self.request.user
		return super(AddChildren, self).form_valid(form)
	def get_success_url(self):
		family = Family.objects.get(id=self.kwargs['pk'])
		children_id1=self.object.pk
		family.children.add(self.object)
		family.save()

		#sending notifications to committies
		health_care_committie = Committie.objects.get(name='Health care')
		health_care_members = Member.objects.filter(committie=health_care_committie)
		education_committie = Committie.objects.get(name='Education')
		education_members = Member.objects.filter(committie=education_committie)
		relif_committie = Committie.objects.get(name='Relif')
		relif_members = Member.objects.filter(committie=relif_committie)
		economic_development_committie = Committie.objects.get(name='Economic development')
		economic_members = Member.objects.filter(committie=economic_development_committie)
		member=Member.objects.get(user=self.request.user)

		#sending notifications to healtch care
		if (self.object.health_care_needed == 'True' ):
			notification = Notification()
			notification.message="You have new ba7s hala"
			for m in health_care_members:
				notification.reciver=m
				notification.sender=member
				m.new_messages+=1
				m.save()
				notification.save()
			health_care_committie.children.add(self.object)
			health_care_committie.save()
		#sendinng notifications to education
		if(self.object.education_needed == 'True'):
			notification = Notification()
			notification.message="You have new ba7s hala"
			notification.save()
			for m in education_members:
				notification.reciver=m
				notification.sender=member
				m.new_messages+=1
				m.save()
				notification.save()
			education_committie.children.add(self.object)
			education_committie.save()
		#sending to economic
		if(self.object.economic_development_needed == 'True'):
			notification = Notification()
			notification.message="You have new ba7s hala"
			notification.save()
			for m in economic_members:
				notification.reciver=m
				notification.sender=member
				m.new_messages+=1
				m.save()
				notification.save()
			economic_development_committie.children.add(self.object)
			economic_development_committie.save()
		#sending to relif
		if(self.object.relif_needed == 'True'):
			notification = Notification()
			notification.message="You have new ba7s hala"
			notification.save()
			for m in relif_members:
				notification.reciver=m
				notification.sender=member
				m.new_messages+=1
				m.save()
				notification.save()
			relif_committie.children.add(self.object)
			relif_committie.save()

		return reverse('family-details', kwargs={'pk':family.id})
		


class CreateHome(CreateView):
	model = Home
	template_name= 'create_home.html'
	fields=['building_status','wall_status','roof_status','floor_status','kitchen','toilet','sarf_sehy','water_shabaka','electrical_equipments_needed',
		'electrical_equipments_radee2a','furniture_needed','furniture_radee2','living_rooms_no','address']

	def post(self,request,*args,**kwargs):
			form=self.get_form()
			if form.is_valid():
				return self.form_valid(form)
			else:
				return JsonResponse({'err_List':self.get_form().errors,'success':0})

	def form_valid(self, form):
			form.save()
		
			
			#user = User1.objects.get(id)
			#form.Product.use1 = user
			#form.instance.employee.user= self.request.user
			return super(CreateHome, self).form_valid(form)
	def get_success_url(self):
		family = Family.objects.get(id=self.kwargs['pk'])
		father = Parent.objects.get(id=self.kwargs['id'])
		mother = Parent.objects.get(id=self.kwargs['mid'])
				#sending notifications to committies
		health_care_committie = Committie.objects.get(name='Health care')
		health_care_members = Member.objects.filter(committie=health_care_committie)
		education_committie = Committie.objects.get(name='Education')
		education_members = Member.objects.filter(committie=education_committie)
		relif_committie = Committie.objects.get(name='Relif')
		relif_members = Member.objects.filter(committie=relif_committie)
		economic_development_committie = Committie.objects.get(name='Economic development')
		economic_members = Member.objects.filter(committie=economic_development_committie)
		member=Member.objects.get(user=self.request.user)

		#sending notifications to healtch care
		
		#sendinng notifications to education
		
		#sending to economic

		#sending to relif
		if(self.object.relif_needed == 'True'):
			notification = Notification()
			notification.message="You have new ba7s hala"
			notification.save()
			for m in relif_members:
				notification.reciver=m
				notification.sender=member
				m.new_messages+=1
				m.save()
				notification.save()
			relif_committie.home.add(self.object)
			relif_committie.save()


		return reverse('create-installment', kwargs={'hid':self.object.pk,'pk':family.id,'id':father.id,'mid':mother.id})


class CreateFather(CreateView):
	model = Parent
	template_name= 'create_father.html'
	fields=['name','birthdate','age','education_level','is_3a2el','job','job_status','marital_status','national_id','mobile','work_status','salary','is_sick',
	'disease','medecine','health_care_expenses','health_care_paid_by','want_kashf','is_atraf_sena3eya','is_3aseel_kalawy','is_surgery_needed','is_special_needs',
	'want_project','project_idea','project_cost','project_profit','project_notes','health_care_needed','education_needed','economic_development_needed']



	def post(self,request,*args,**kwargs):
		form=self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return JsonResponse({'err_List':self.get_form().errors,'success':0})

	def form_valid(self, form):

		form.save()
	
		
		#user = User1.objects.get(id)
		#form.Product.use1 = user
		#form.instance.employee.user= self.request.user
		return super(CreateFather, self).form_valid(form)

	def get_success_url(self):
		family = Family.objects.get(id=self.kwargs['pk'])

				#sending notifications to committies
		health_care_committie = Committie.objects.get(name='Health care')
		health_care_members = Member.objects.filter(committie=health_care_committie)
		education_committie = Committie.objects.get(name='Education')
		education_members = Member.objects.filter(committie=education_committie)
		relif_committie = Committie.objects.get(name='Relif')
		relif_members = Member.objects.filter(committie=relif_committie)
		economic_development_committie = Committie.objects.get(name='Economic development')
		economic_members = Member.objects.filter(committie=economic_development_committie)
		member=Member.objects.get(user=self.request.user)

		#sending notifications to healtch care
		if (self.object.health_care_needed == 'True' ):
			notification = Notification()
			notification.message="You have new ba7s hala"
			for m in health_care_members:
				notification.reciver=m
				notification.sender=member
				m.new_messages+=1
				m.save()
				notification.save()
			health_care_committie.father.add(self.object)
			health_care_committie.save()
		#sendinng notifications to education
		if(self.object.education_needed == 'True'):
			notification = Notification()
			notification.message="You have new ba7s hala"
			notification.save()
			for m in education_members:
				notification.reciver=m
				notification.sender=member
				m.new_messages+=1
				m.save()
				notification.save()
			education_committie.father.add(self.object)
			education_committie.save()
		#sending to economic
		if(self.object.economic_development_needed == 'True'):
			notification = Notification()
			notification.message="You have new ba7s hala"
			notification.save()
			for m in economic_members:
				notification.reciver=m
				notification.sender=member
				m.new_messages+=1
				m.save()
				notification.save()
			economic_development_committie.father.add(self.object)
			economic_development_committie.save()
		
		return reverse('create-mother', kwargs={'id':self.object.pk,'pk':family.id})

class CreateMother(CreateView):
	model = Parent
	template_name= 'create_mother.html'
	fields=['name','birthdate','age','education_level','is_3a2el','job','job_status','marital_status','national_id','mobile','work_status','salary','is_sick',
	'disease','medecine','health_care_expenses','health_care_paid_by','want_kashf','is_atraf_sena3eya','is_3aseel_kalawy','is_surgery_needed','is_special_needs',
	'want_project','project_idea','project_cost','project_profit','project_notes','health_care_needed','education_needed','economic_development_needed']



	def post(self,request,*args,**kwargs):
		form=self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return JsonResponse({'err_List':self.get_form().errors,'success':0})

	def form_valid(self, form):
		form.save()
	
		
		#user = User1.objects.get(id)
		#form.Product.use1 = user
		#form.instance.employee.user= self.request.user
		return super(CreateMother, self).form_valid(form)

	def get_success_url(self):
		family = Family.objects.get(id=self.kwargs['pk'])
		father = Parent.objects.get(id=self.kwargs['id'])


				#sending notifications to committies
		health_care_committie = Committie.objects.get(name='Health care')
		health_care_members = Member.objects.filter(committie=health_care_committie)
		education_committie = Committie.objects.get(name='Education')
		education_members = Member.objects.filter(committie=education_committie)
		relif_committie = Committie.objects.get(name='Relif')
		relif_members = Member.objects.filter(committie=relif_committie)
		economic_development_committie = Committie.objects.get(name='Economic development')
		economic_members = Member.objects.filter(committie=economic_development_committie)
		member=Member.objects.get(user=self.request.user)

		#sending notifications to healtch care
		if (self.object.health_care_needed == 'True' ):
			notification = Notification()
			notification.message="You have new ba7s hala"
			for m in health_care_members:
				notification.reciver=m
				notification.sender=member
				m.new_messages+=1
				m.save()
				notification.save()
			health_care_committie.mother.add(self.object)
			health_care_committie.save()
		#sendinng notifications to education
		if(self.object.education_needed == 'True'):
			notification = Notification()
			notification.message="You have new ba7s hala"
			notification.save()
			for m in education_members:
				notification.reciver=m
				notification.sender=member
				m.new_messages+=1
				m.save()
				notification.save()
			education_committie.mother.add(self.object)
			education_committie.save()
		#sending to economic
		if(self.object.economic_development_needed == 'True'):
			notification = Notification()
			notification.message="You have new ba7s hala"
			notification.save()
			for m in economic_members:
				notification.reciver=m
				notification.sender=member
				m.new_messages+=1
				m.save()
				notification.save()
			economic_development_committie.mother.add(self.object)
			economic_development_committie.save()
		#sending to relif
		
		return reverse('create-home', kwargs={'mid':self.object.pk,'pk':family.id,'id':father.id})

class CreateInstallment(CreateView):
	model = Installment
	template_name= 'create_installment.html'
	fields=['name','no_installments_left','installment_value']

	def post(self,request,*args,**kwargs):
		form=self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return JsonResponse({'err_List':self.get_form().errors,'success':0})

	def form_valid(self, form):
		form.save()
	
		
		#user = User1.objects.get(id)
		#form.Product.use1 = user
		#form.instance.employee.user= self.request.user
		return super(CreateInstallment, self).form_valid(form)

	def get_success_url(self):
		family = Family.objects.get(id=self.kwargs['pk'])
		father = Parent.objects.get(id=self.kwargs['id'])
		mother = Parent.objects.get(id=self.kwargs['mid'])
		home = Home.objects.get(id = self.kwargs['hid'])
		return reverse('create-children', kwargs={'insid':self.object.pk,'pk':family.id,'id':father.id,'mid':mother.id,'hid':home.id})




class AddInstallment(CreateView):
	model = Installment
	template_name= 'create_installment.html'
	fields=['name','no_installments_left','installment_value']

	def post(self,request,*args,**kwargs):
		form=self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return JsonResponse({'err_List':self.get_form().errors,'success':0})

	def form_valid(self, form):
		form.save()
	
		
		#user = User1.objects.get(id)
		#form.Product.use1 = user
		#form.instance.employee.user= self.request.user
		return super(AddInstallment, self).form_valid(form)

	def get_success_url(self):
		family = Family.objects.get(id=self.kwargs['pk'])
		family.installment.add(self.object)
		family.save()
		
		return reverse('family-details', kwargs={'pk':family.id})



class CreateFamily(CreateView):
	model = Family
	template_name= 'create_family.html'
	fields=['poverty_level','family_members','other_members','other_notes','is_member_ommi','ommi','ommi_free_time','is_ma3ashat_sho2on_egtma3eya',
	'is_ma3ashat_ta2meneya','masdar_da5l','installment','food_expenses','transportation_expenses','education_expenses','total_health_care_expenses',
	'electricity_expenses','water_expenses','mobile_expenses','rent_expenses','gas_expenses','smoking_expenses','is_tamweneya_card','no_people_in_tamweneya_card',
	]


	def post(self,request,*args,**kwargs):
		form=self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return JsonResponse({'err_List':self.get_form().errors,'success':0})

	def form_valid(self, form):
		member1 = Member.objects.get(user=self.request.user)
		form.instance.member = member1
		form.save()
	
		
		#user = User1.objects.get(id)
		#form.Product.use1 = user
		#form.instance.employee.user= self.request.user
		return super(CreateFamily, self).form_valid(form)

	def get_success_url(self):
		return reverse('create-father', kwargs={'pk':self.object.pk})


class FamilyList(ListView):

	template_name='family_list.html'
	model = Family

	def get_context_data(self, **kwargs):
		context = super(FamilyList, self).get_context_data(**kwargs)
		member = Member.objects.get(user=self.request.user)
		context['member']=member
		return context

class FamilyDetails(DetailView):

	template_name='family_details.html'
	model = Family

	def get_context_data(self, **kwargs):
		context = super(FamilyDetails, self).get_context_data(**kwargs)
		family = Family.objects.get(id=self.kwargs['pk'])
		family_member = family.member
		member = Member.objects.get(user=self.request.user)
		context['member']=member
		context['family_member']=family_member
		
		return context

class ChildrenDetails(DetailView):

	template_name='children_details.html'
	model = Children

	def get_context_data(self, **kwargs):
		context = super(ChildrenDetails, self).get_context_data(**kwargs)
		child = Children.objects.get(id=self.kwargs['pk'])
		family = Family.objects.get(children=child)
		member = Member.objects.get(user=self.request.user)
		context['family']=family
		context['member']=member
		#data = serializers.serialize( "python", Children.objects.filter(id=c_id.id) )
		#context['data']=data
		 #for instance in data 
    	#	 for field, value in instance.fields.items 
        #		 field : value 


		
		return context

class MotherDetails(DetailView):

	template_name='mother_details.html'
	model = Parent

	def get_context_data(self, **kwargs):
		context = super(MotherDetails, self).get_context_data(**kwargs)
		mother1 = Parent.objects.get(id=self.kwargs['pk'])
		family = Family.objects.get(mother=mother1)
		context['family'] = family

		
		return context

class FatherDetails(DetailView):

	template_name='father_details.html'
	model = Parent

	def get_context_data(self, **kwargs):
		context = super(FatherDetails, self).get_context_data(**kwargs)
		father1 = Parent.objects.get(id=self.kwargs['pk'])
		family=Family.objects.get(father=father1)
		context ['family']=family
		return context

class HomeDetails(DetailView):

	template_name='home_details.html'
	model = Home

	def get_context_data(self, **kwargs):
		context = super(HomeDetails, self).get_context_data(**kwargs)
		home1 = Home.objects.get(id=self.kwargs['pk'])
		family = Family.objects.get(home=home1)
		context['family'] = family
		
		return context

class InstallmentDetails(DetailView):

	template_name='installment_details.html'
	model = Installment

	def get_context_data(self, **kwargs):
		context = super(InstallmentDetails, self).get_context_data(**kwargs)
		family=Family.objects.get(installment=self.object)
		context['family']= family


		
		return context

		


class Ba7s7alaList(ListView):
	template_name='list_ba7s7ala.html'
	model = Committie
	def get_context_data(self, **kwargs):
		context = super(Ba7s7alaList, self).get_context_data(**kwargs)
		member = Member.objects.get(user=self.request.user)
		committie1 = member.committie
		if hasattr(committie1, 'fathers'):
			fathers = committie1.father
			context['fathers']=fathers
		if hasattr(committie1, 'mothers'):
			mothers = committie1.mother
			context['mothers']=mothers
		if hasattr(committie1, 'children'):
			children = committie1.children
			context['children']=children
		if hasattr(committie1, 'home'):
			home = committie1.home
			context['home']=home

		return context
	
class UpdateMothers(UpdateView):
	template_name='update_mothers.html'
	model = Parent
	fields=['name','birthdate','age','education_level','is_3a2el','job','job_status','marital_status','national_id','mobile','work_status','salary','is_sick',
	'disease','medecine','health_care_expenses','health_care_paid_by','want_kashf','is_atraf_sena3eya','is_3aseel_kalawy','is_surgery_needed','is_special_needs',
	'want_project','project_idea','project_cost','project_profit','project_notes','health_care_needed','education_needed','economic_development_needed','relif_needed']


	def get_success_url(self):
		return reverse('mother-details', kwargs={'pk': self.kwargs['pk']})

class UpdateFathers(UpdateView):
	template_name='update_fathers.html'
	model = Parent
	fields=['name','birthdate','age','education_level','is_3a2el','job','job_status','marital_status','national_id','mobile','work_status','salary','is_sick',
	'disease','medecine','health_care_expenses','health_care_paid_by','want_kashf','is_atraf_sena3eya','is_3aseel_kalawy','is_surgery_needed','is_special_needs',
	'want_project','project_idea','project_cost','project_profit','project_notes','health_care_needed','education_needed','economic_development_needed','relif_needed']


	def get_success_url(self):
		return reverse('father-details', kwargs={'pk': self.kwargs['pk']})

class UpdateChildren(UpdateView):
	template_name='update_children.html'
	model = Children
	fields=['name','birthdate','education_level','school_name','doros_number','doros_type','doros_expenses','doros_needed','is_graduate',
		'gradutae_degree','is_worker','salary','per','is_sick','disease','medecine','health_care_expenses','health_care_paid_by','want_kashf',
		'is_atraf_sena3eya','is_3aseel_kalawy','is_surgery_needed','is_special_needs','health_care_needed','education_needed','economic_development_needed',
		'relif_needed']

	def get_success_url(self):
		return reverse('children-details', kwargs={'pk': self.kwargs['pk']})

class UpdateInstallment(UpdateView):
	template_name='update_installment.html'
	model = Installment
	fields=['name','no_installments_left','installment_value']


	def get_success_url(self):
		return reverse('installment-details', kwargs={'pk': self.kwargs['pk']})

class UpdateFamily(UpdateView):

	template_name= 'update_family.html'
	model = Family

	fields=['poverty_level','family_members','other_members','other_notes','is_member_ommi','ommi','ommi_free_time','is_ma3ashat_sho2on_egtma3eya',
	'is_ma3ashat_ta2meneya','masdar_da5l','installment','food_expenses','transportation_expenses','education_expenses','total_health_care_expenses',
	'electricity_expenses','water_expenses','mobile_expenses','rent_expenses','gas_expenses','smoking_expenses','is_tamweneya_card','no_people_in_tamweneya_card',
	]
	def get_success_url(self):
		return reverse('family-details', kwargs={'pk': self.kwargs['pk']})


class UpdateHome(UpdateView):
	model = Home
	template_name= 'update_home.html'
	fields=['building_status','wall_status','roof_status','floor_status','kitchen','toilet','sarf_sehy','water_shabaka','electrical_equipments_needed',
		'electrical_equipments_radee2a','furniture_needed','furniture_radee2','living_rooms_no','address']

	def get_success_url(self):
		return reverse('home-details', kwargs={'pk': self.kwargs['pk']})

class FatherList(ListView):

	template_name='list_father.html'
	model = Parent

	def get_context_data(self, **kwargs):
		context = super(FatherList, self).get_context_data(**kwargs)


		return context

class MotherList(ListView):

	template_name='list_mother.html'
	model = Parent

	def get_context_data(self, **kwargs):
		context = super(MotherList, self).get_context_data(**kwargs)


		return context

class HomeList(ListView):

	template_name='list_home.html'
	model = Home

	def get_context_data(self, **kwargs):
		context = super(HomeList, self).get_context_data(**kwargs)


		return context


class InstallmentList(ListView):

	template_name='list_installment.html'
	model = Installment

	def get_context_data(self, **kwargs):
		context = super(InstallmentList, self).get_context_data(**kwargs)


		return context

class ChildrenList(ListView):

	template_name='childrenList.html'
	model = Children

	def get_context_data(self, **kwargs):
		context = super(ChildrenList, self).get_context_data(**kwargs)


		return context

class Database(ListView):

	template_name='template.html'
	model = Family

	def get_context_data(self, **kwargs):
		context = super(Database, self).get_context_data(**kwargs)
	


		return context


#class DeleteFather(DeleteView):
#	template_name='delete_father.html'
#	model = Parent

#	def get_success_url(self):
#		return reverse('product-list', kwargs={'pk': self.kwargs['id']})