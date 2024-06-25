from django.urls import path
from . import views



urlpatterns=[
    path('carts/',views.cart)
]