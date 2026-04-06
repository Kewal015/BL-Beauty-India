from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),          # homepage
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('blogs/', views.gallery, name='blogs'),
    path('contact/', views.contact, name='contact'),
]