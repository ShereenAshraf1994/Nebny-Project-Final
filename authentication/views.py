from django.shortcuts import render
from django.views.generic import FormView, TemplateView,View, UpdateView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView,View, UpdateView, ListView, DeleteView
from django.views.generic.detail import DetailView
from authentication.forms import *
from django.contrib.auth.forms import UserCreationForm
from authentication.models import *

class IndexView(ListView):
	template_name = 'template.html'
	model = User
	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		user = self.request.user
		
		if self.request.user.is_authenticated():
			member = Member.objects.get(user=self.request.user)
			#user=customuser.user
			#unread=user.notifications.unread()	

			context['member']=member
		return context 





class CreateUser(FormView):
	template_name= 'login2.html'
	form_class= UserForm

	def post(self,request,*args,**kwargs):
		form=self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return JsonResponse({'err_List':self.get_form().errors,'success':0})

	def form_valid(self, form):
		form.save()
		user1 = authenticate(
				username=form.cleaned_data['username'],
				password=form.cleaned_data['password2'])

		login(self.request, user1)
		
		
		return HttpResponseRedirect(reverse_lazy('create-member'))


class CreateMember(CreateView):
	model = Member
	template_name= 'login3.html'
	fields=['guc_id','committie','faculty','position']

	def get_context_data(self, **kwargs):
		context = super(CreateMember, self).get_context_data(**kwargs)
		return context

	
	def form_valid(self, form):
		u=self.request.user
		form.instance.user=u
		form.save()
	
		
		#user = User1.objects.get(id)
		#form.Product.use1 = user
		#form.instance.employee.user= self.request.user
		return super(CreateMember, self).form_valid(form)

	def get_success_url(self):
		notification = Notification()
		notification.message="New Profile request"
		if(self.object.position == "Member"):		
			notification.reciver = self.object.committie.head

		if(self.object.position == "Head"):
			core = Core.objects.all()
			for c in core:
				for comm in c.committies.all():
					if (self.object.committie == comm):
						notification.reciver = c.core_president


			support = Support.objects.all()
			for s in support:
				for comm in s.committies.all():
					if (self.object.committie == comm):
						notification.reciver = c.support_president

		if(self.object.position == "Core President"):
			president = Member.objects.get(position="President")
			notification.reciver = president			




		notification.reciver.new_messages +=1
		notification.sender = self.object
		notification.reciver.save()
		notification.save()
			
	
		return reverse('signin-user')
	


class UserSignin(View):
	model = User
	#template_name='template.html'
	template_name='login.html'

	def get(self,request,*args, **kwargs):
		return render(request,self.template_name)

	def post(self,request,*args, **kwargs):
		user=authenticate(
			username=request.POST['username1'],
			password=request.POST['password1'])
		if user:
			if user.is_active:
				login(self.request,user)
				return HttpResponseRedirect(reverse_lazy('home'))
			else:
				return JsonResponse({'success':0,'error':"Your account has been disabled"})
		else:
			return JsonResponse({'success':0,'error':"Invalid login details supplied."})

class UserSignout(View):
	def get(self,request,*args,**kwargs):
		logout(request)
		return HttpResponseRedirect(reverse_lazy('signin-user'))

class UserDetailView(DetailView):

	template_name='detail_view.html'
	model = User

	def get_context_data(self, **kwargs):
		context = super(UserDetailView, self).get_context_data(**kwargs)
		member = Member.objects.get(user=self.request.user)
		context['member'] = member
		return context


class UserEdit(UpdateView):
    model = User
    fields = ['first_name','last_name','email']
    template_name = 'user_update.html'

    def get_success_url(self):
    	return reverse('user-detail', kwargs={'pk': self.kwargs['pk']})

class UpdatePassword(CreateView):

	template_name= 'update_password.html'
	form_class= PasswordForm

	def post(self,request,*args,**kwargs):

		form=self.get_form()
		form.username = self.request.user.username
		form.save()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return JsonResponse({'err_List':self.get_form().errors,'success':0})

	def form_valid(self, form):
		
		
		
		return HttpResponseRedirect(reverse_lazy('home'))



class ListCommittie(ListView):

	template_name='list_committies.html'
	model = Committie

	def get_context_data(self, **kwargs):
		context = super(ListCommittie, self).get_context_data(**kwargs)
		#context['products_list'] = Product.objects.filter(user=self.request.user)
		return context

class CommittieDetailView(DetailView):

	template_name='comm_detail_view.html'
	model = Committie


	def get_context_data(self, **kwargs):
		context = super(CommittieDetailView, self).get_context_data(**kwargs)
		c_id = self.kwargs['pk']
		committie1 = Committie.objects.get(id=c_id)
		members = Member.objects.filter(committie=committie1)
		context['members']=members

		return context


class ListNotification(ListView):
	template_name='list_notification.html'
	model = Notification

	def get_context_data(self, **kwargs):
		context = super(ListNotification, self).get_context_data(**kwargs)
		member = Member.objects.get(user=self.request.user)
		context['member']=member
		member.new_messages=0
		member.save()
		return context


class NotificationDetails(DetailView):

	template_name='notification_details.html'
	model = Notification

	def get_context_data(self, **kwargs):
		context = super(NotificationDetails, self).get_context_data(**kwargs)
		notification = Notification.objects.get(id=self.kwargs['pk'])
		notification.is_read = True
		notification.save()
		context['notification'] = notification
		return context


class ApproveMember(View):
	model = Member
	def get(self,request,*args, **kwargs):
		 member = Member.objects.get(id=self.kwargs['pk'])
		 member.approved=True
		 if (member.position == "Head"):
		 	member.is_head = True
		 if (member.position == "Core President"):
		 	member.is_UB = True
		 if (member.position == "Support President"):
		 	member.is_UB = True

		 member.save()
		 return HttpResponseRedirect (reverse('home'))


		
class TemplatesView(ListView):

	template_name='template.html'
	model = User

	def get_context_data(self, **kwargs):
		context = super(TemplatesView, self).get_context_data(**kwargs)
		context['head'] = User
		context['member'] = User
		return context


##Added by oasama
class  DatabasingCommitteeView(ListView):

	template_name='databasingCommittee.html'
	model = User

	def get_context_data(self, **kwargs):
		context = super(DatabasingCommitteeView, self).get_context_data(**kwargs)
		context['head'] = User
		context['member'] = User
		return context		


class  EducationCommiteeView(ListView):

	template_name='educationCommittee.html'
	model = User

	def get_context_data(self, **kwargs):
		context = super(EducationCommiteeView, self).get_context_data(**kwargs)
		context['head'] = User
		context['member'] = User
		return context		

class  HealthCareCommitteeView(ListView):

	template_name='healthCareCommittee.html'
	model = User

	def get_context_data(self, **kwargs):
		context = super(HealthCareCommitteeView, self).get_context_data(**kwargs)
		context['head'] = User
		context['member'] = User
		return context		






class  EconomicEmpCommitteeView(ListView):

	template_name='economicEmpCommittee.html'
	model = User

	def get_context_data(self, **kwargs):
		context = super(EconomicEmpCommitteeView, self).get_context_data(**kwargs)
		context['head'] = User
		context['member'] = User
		return context		

class  ReliefCommitteeView(ListView):

	template_name='reliefCommittee.html'
	model = User

	def get_context_data(self, **kwargs):
		context = super(ReliefCommitteeView, self).get_context_data(**kwargs)
		context['head'] = User
		context['member'] = User
		return context		

class  PublicRelationCommitteeView(ListView):

	template_name='prCommittee.html'
	model = User

	def get_context_data(self, **kwargs):
		context = super(PublicRelationCommitteeView, self).get_context_data(**kwargs)
		context['head'] = User
		context['member'] = User
		return context		

class  FundRaisingCommitteeView(ListView):

	template_name='frCommittee.html'
	model = User

	def get_context_data(self, **kwargs):
		context = super(FundRaisingCommitteeView, self).get_context_data(**kwargs)
		context['head'] = User
		context['member'] = User
		return context		

class  MediaCommitteeView(ListView):

	template_name='mediaCommittee.html'
	model = User

	def get_context_data(self, **kwargs):
		context = super(MediaCommitteeView, self).get_context_data(**kwargs)
		context['head'] = User
		context['member'] = User
		return context		


class  HumanResourcesCommitteeView(ListView):

	template_name='hrCommittee.html'
	model = User

	def get_context_data(self, **kwargs):
		context = super(HumanResourcesCommitteeView, self).get_context_data(**kwargs)
		context['head'] = User
		context['member'] = User
		return context	


class  FundRaisingCommitteeView(ListView):

	template_name='frCommittee.html'
	model = User

	def get_context_data(self, **kwargs):
		context = super(FundRaisingCommitteeView, self).get_context_data(**kwargs)
		context['head'] = User
		context['member'] = User
		return context		


class  FinancialView(ListView):

	template_name='financialCommittee.html'
	model = User

	def get_context_data(self, **kwargs):
		context = super(FinancialView, self).get_context_data(**kwargs)
		context['head'] = User
		context['member'] = User
		return context					

		

class  UnderConstruction(ListView):

	template_name='pages_uc.html'
	model = User

	def get_context_data(self, **kwargs):
		context = super(UnderConstruction, self).get_context_data(**kwargs)
		context['head'] = User
		context['member'] = User
		return context		

class  CalenderView(ListView):

	template_name='pages_calendar.html'
	model = User

	def get_context_data(self, **kwargs):
		context = super(CalenderView, self).get_context_data(**kwargs)
		context['head'] = User
		context['member'] = User
		return context				