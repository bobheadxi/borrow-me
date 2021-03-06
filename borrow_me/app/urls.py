"""borrow_me URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.views.generic import TemplateView
from .views import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^submit/', TemplateView.as_view(template_name='site/submission.html'), name='submit'),
    url(r'^item/', views.ItemView.as_view(), name='item'),
    url(r'^user/', views.UserView.as_view(), name='user'),
    url(r'^accounts/profile/', views.profile, name='profile'),
]
