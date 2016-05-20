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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^signup/', CreateUser.as_view(), name='create-user'),
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^signin/', UserSignin.as_view(), name='signin-user'),
    url(r'^signout/', UserSignout.as_view(), name='signout-user'),
    url(r'^userdetail/(?P<pk>[0-9]+)/$', UserDetailView.as_view(), name='user-detail'),
    url(r'^useredit/(?P<pk>[0-9]+)/$', UserEdit.as_view(), name='user-edit'),
    #commities
    url(r'^listcommitties/$', ListCommittie.as_view(), name='list-committie'),
    url(r'^detailscommitties/(?P<pk>[0-9]+)/$', CommittieDetailView.as_view(), name='comm-details'),

    url(r'^template/', TemplateView.as_view(), name='template'),
]
