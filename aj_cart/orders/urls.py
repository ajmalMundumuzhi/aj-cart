from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from orders import views
urlpatterns=[
    path('cart',views.cart_show,name='cart')
]