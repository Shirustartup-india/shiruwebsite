from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index),
    path('land/contact', views.contactus),
    path('form', views.form),
    path('submitall', views.former ),
    path('success', views.success ),
]

