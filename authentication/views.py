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

class IndexView(ListView):
	template_name = 'index.html'
	model = User
	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		
		if self.request.user.is_authenticated():
			member = Member.objects.get(user=self.request.user)
			#user=customuser.user
			#unread=user.notifications.unread()	
			
			context['member']=member
		return context

class CreateUser(FormView):
	template_name= 'SignUp.html'
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
		member = Member()
		member.user = user1
		member.is_head = False
		member.is_UB = False
		member.is_deleted = False
		member.save()
		
		return HttpResponseRedirect(reverse_lazy('home'))

class UserSignin(View):
	model = User
	template_name='SignIn.html'

	def get(self,request,*args, **kwargs):
		return render(request,self.template_name)

	def post(self,request,*args, **kwargs):
		user=authenticate(
			username=request.POST['username'],
			password=request.POST['password'])
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
		return HttpResponseRedirect(reverse_lazy('home'))

class UserDetailView(DetailView):

	template_name='detail_view.html'
	model = User

def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['user'] = User
        return context

class UserEdit(UpdateView):
    model = User
    fields = ['first_name','last_name']
    template_name = 'user_update.html'

    def get_success_url(self):
    	return reverse('user-detail', kwargs={'pk': self.kwargs['pk']})

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
        context['head'] = User
        context['member'] = User
        return context