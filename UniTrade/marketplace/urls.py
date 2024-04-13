from django.urls import path
from . import views

urlpatterns = [
    path('current/', views.current, name='current'),
    path('marketplace/<str:pk>/', views.viewItem, name='item'),
    path('add/', views.addItem, name='add'),
    path('condition/', views.inputCondition, name='condition'),
    path('',views.productPage, name= 'products'),
    path('aboutus/', views.aboutUs, name= 'aboutus'),
    path('faq/', views.faq, name= 'faq'),
    path('books/', views.books, name= 'books')
]