"""nebny URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from authentication.views import *
from atfaluna.views import *

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^signup1/', CreateUser.as_view(), name='create-user'),
    url(r'^signup2/',CreateMember.as_view(), name='create-member'),
    url(r'^signin/', UserSignin.as_view(), name='signin-user'),
    url(r'^signout/', UserSignout.as_view(), name='signout-user'),
    url(r'^userdetail/(?P<pk>[0-9]+)/$', UserDetailView.as_view(), name='user-detail'),
    url(r'^useredit/(?P<pk>[0-9]+)/$', UserEdit.as_view(), name='user-edit'),
     url(r'^updatepassword/(?P<pk>[0-9]+)/$', UpdatePassword.as_view(), name='update-password'),

    #commities
    url(r'^listcommitties/$', ListCommittie.as_view(), name='list-committie'),
    url(r'^detailscommitties/(?P<pk>[0-9]+)/$', CommittieDetailView.as_view(), name='comm-details'),

    #notification
     url(r'^listnotifications$', ListNotification.as_view(), name='listnotifications'),
    url(r'^notificationdetials/(?P<pk>[0-9]+)/$', NotificationDetails.as_view(), name='notificationdetails'),
    url(r'^approvemember/(?P<pk>[0-9]+)/$', ApproveMember.as_view(), name='approve-member'),
    #atfaluna
    url(r'^createfamily/',CreateFamily.as_view(), name='create-family'),
    url(r'^createfather/(?P<pk>[0-9]+)/$',CreateFather.as_view(), name='create-father'),
    url(r'^createmother/(?P<pk>[0-9]+)/(?P<id>[0-9]+)/$',CreateMother.as_view(), name='create-mother'),
    url(r'^createhome/(?P<pk>[0-9]+)/(?P<id>[0-9]+)/(?P<mid>[0-9]+)$',CreateHome.as_view(), name='create-home'),
    url(r'^createinstallment/(?P<pk>[0-9]+)/(?P<id>[0-9]+)/(?P<mid>[0-9]+)/(?P<hid>[0-9]+)$',CreateInstallment.as_view(), name='create-installment'),
    url(r'^createchildren/(?P<pk>[0-9]+)/(?P<id>[0-9]+)/(?P<mid>[0-9]+)/(?P<hid>[0-9]+)/(?P<insid>[0-9]+)$',CreateChildren.as_view(), name='create-children'),
    url(r'^familylist/$', FamilyList.as_view(), name='family-list'),
    url(r'^listfather/$', FatherList.as_view(), name='list-father'),
    url(r'^listmother/$', MotherList.as_view(), name='list-mother'),
    url(r'^listchildren/$', ChildrenList.as_view(), name='list-children'),
    url(r'^database/$', Database.as_view(), name='database'),
    url(r'^addchildren/(?P<pk>[0-9]+)/$',AddChildren.as_view(), name='add-children'),
    url(r'^addinstallment/(?P<pk>[0-9]+)/$',AddInstallment.as_view(), name='add-installment'),
     
     url(r'^listhome/$', HomeList.as_view(), name='list-home'),
     url(r'^listinstallment/$',InstallmentList.as_view(), name='list-installment'),
     url(r'^familydetails/(?P<pk>[0-9]+)/$', FamilyDetails.as_view(), name='family-details'),
     url(r'^motherdetails/(?P<pk>[0-9]+)/$', MotherDetails.as_view(), name='mother-details'),
     url(r'^fatherdetails/(?P<pk>[0-9]+)/$', FatherDetails.as_view(), name='father-details'),
     url(r'^homedetails/(?P<pk>[0-9]+)/$', HomeDetails.as_view(), name='home-details'),
     url(r'^childrendetails/(?P<pk>[0-9]+)/$', ChildrenDetails.as_view(), name='children-details'),
     url(r'^installmentdetails/(?P<pk>[0-9]+)/$', InstallmentDetails.as_view(), name='installment-details'),
     url(r'^7alalist/',Ba7s7alaList.as_view(), name='ba7s7ala-list'),
     #edit
    url(r'^updatechild/(?P<pk>[0-9]+)/$', UpdateChildren.as_view(), name='update-child'),
    url(r'^updatemother/(?P<pk>[0-9]+)/$', UpdateMothers.as_view(), name='update-mother'),
    url(r'^updatefather/(?P<pk>[0-9]+)/$', UpdateFathers.as_view(), name='update-father'),
    url(r'^updatehome/(?P<pk>[0-9]+)/$', UpdateHome.as_view(), name='update-home'),
    url(r'^updatefamily/(?P<pk>[0-9]+)/$', UpdateFamily.as_view(), name='update-family'),
    url(r'^updateinstallment/(?P<pk>[0-9]+)/$', UpdateInstallment.as_view(), name='update-installment'),

    url(r'^template/', TemplatesView.as_view(), name='template'),

    ##Added by osama
    url(r'^databasingCommittee/', DatabasingCommitteeView.as_view(), name='databasing-committee'),
    url(r'^educationCommitee/', EducationCommiteeView.as_view(), name='education-committee'),
    url(r'^healthCareCommittee/', HealthCareCommitteeView.as_view(), name='healthCare-committee'),
    url(r'^economicEmpCommittee/', EconomicEmpCommitteeView.as_view(), name='economicEmp-committee'),
    url(r'^reliefCommittee/', ReliefCommitteeView.as_view(), name='relief-committee'),
    url(r'^publicRelationCommittee/', PublicRelationCommitteeView.as_view(), name='publicRelation-committee'),
    url(r'^fundRaisingCommittee/', FundRaisingCommitteeView.as_view(), name='fundRaising-committee'),
    url(r'^mediaCommittee/', MediaCommitteeView.as_view(), name='media-committee'),
    url(r'^humanResourcesCommittee/', HumanResourcesCommitteeView.as_view(), name='humanResources-committee'),
    url(r'^fundRaising/', FundRaisingCommitteeView.as_view(), name='fundRaising-committee'),
    url(r'^financial/', FinancialView.as_view(), name='financial'),
    url(r'^pagesuc/', UnderConstruction.as_view(), name='pages-uc'),
    url(r'^calender/', CalenderView.as_view(), name='calender'),



]
