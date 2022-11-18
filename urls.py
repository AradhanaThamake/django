from django.contrib import admin
from django.urls import path
from todoapp import views

urlpatterns = [
    path('home',views.home),
    path('product',views.product),
    path('contact',views.contact),
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete),
    path('evenodd/<n>',views.evenodd),
    path('tloop',views.loop),
    path('',views.index),
    path('about',views.about),
    path('create',views.create_task),
    
]

'''
urlspattern[]: It contains the list of urls
to be matched with the request received from the client.

syntax:
path('url_pattern',views.functionname,name="")
'''