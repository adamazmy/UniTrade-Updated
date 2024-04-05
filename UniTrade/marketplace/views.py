from django.shortcuts import render
from .models import Department, Photo

# Create your views here.


def current(request):
    departments = Department.objects.all()
    photos = Photo.objects.all()


    context = {'departments':departments, 'photos':photos}
    return render(request, 'marketplace/currentListing.html', context)

def inputCondition(request):
    return render(request, 'marketplace/condition.html')

def addItem(request):
    return render(request, 'marketplace/add.html')

def viewItem(request, pk):
    return render(request, 'marketplace/item.html')
