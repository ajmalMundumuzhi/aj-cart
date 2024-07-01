from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from customers import views
urlpatterns=[
    path('account',views.account_show,name='account')
]