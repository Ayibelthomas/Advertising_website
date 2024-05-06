"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mpr import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.index),
    path('login/',views.login),
    path('about/',views.about),
    path('contact/',views.contact),
    
    path('customer_reg/',views.customer_reg),

    #admin 
    path('admin_dash/',views.admin_dash),
    path('Admin_viewRequest/',views.Admin_viewRequest),
    path('reject_request/',views.reject_request),
    path('approve/',views.approve),
    path('Admin_viewConfirmedreq/',views.Admin_viewConfirmedreq),
    path('admin_addAmount/',views.admin_addAmount),
    path('addreport/',views.addreport),
    path('admin_viewReport/',views.admin_viewReport),
    path('view_customers/',views.view_customers),
    path('delete_customers/',views.delete_customers),

    
    #Customer
    path('customer_dash/',views.customer_dash),
    path('add_request/',views.add_request),
    path('view_request/',views.view_request),
    path('cancel_request/',views.cancel_request),
    path('customer_viewConfirmedreq/',views.customer_viewConfirmedreq),
    path('pay/',views.pay),
    path('view_report/',views.view_report),
    
]
