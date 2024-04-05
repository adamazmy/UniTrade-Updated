from django.urls import path
from . import views

urlpatterns = [
    path('', views.current, name='current'),
    path('marketplace/<str:pk>/', views.viewItem, name='item'),
    path('add/', views.addItem, name='add'),
    path('condition/', views.inputCondition, name='condition'),
]