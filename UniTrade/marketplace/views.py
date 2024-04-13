from django.shortcuts import render, redirect
from django.db import models
from .models import Department, Photo, Product, Productimage
import os
from django.core.files.storage import FileSystemStorage

# Create your views here.


def current(request):
    departments = Department.objects.all()
    productimages = Productimage.objects.all()
    products =Product.objects.all()


    context = {'departments':departments, 'productimages':productimages, 'products': products}
    return render(request, 'marketplace/currentListing.html', context)

def inputCondition(request):
    return render(request, 'marketplace/condition.html')



def addItem(request):
    print("POST 1")
    print(request.method)
    if request.method == 'POST':
        print("POST")
        title = request.POST.get('title')

        print(title)

        brand = request.POST.get('brand', '')
        print(brand)

        department = request.POST.get('department')
        print(department)

        price = request.POST['price']
        print(price)

        condition = request.POST['condition']
        print(condition)

        description = request.POST['description']

        print(title, brand, department, price, condition, description)

        images = request.FILES.getlist('image')  # for single file upload
       
      
        # Create and save the new object to the database

        new_object = Product(
            title=title,
            brand=brand,
            department_id=department,  # assuming department is a ForeignKey
            price=price,
            condition=condition,
            description=description,
            userID = 1
            # image=image  # make sure your model has an 'image' field
        )
        new_object.save()

        auto_generated_key = new_object.pk
        save_path = 'static/images/' +str(auto_generated_key)
        os.makedirs(save_path)

        
        for image in images:

            #save_path = 'static/images/' + str(auto_generated_key)  # It's better to store in 'media' for Django projects
            # fs = FileSystemStorage(location=save_path)

            # # Save the image
            # filename = fs.save(image.name, image)  # 'image.name' should be used carefully

            # image.save('13', image.filename)

            image_object = Productimage(
            imageURL = image,
            product_id = auto_generated_key
            )
            image_object.save()
        
        # products = Product.objects.all()
        #return render(request, 'marketplace/currentListing.html', {'products': products})
        return redirect('current')  # Redirect after POST

    # If not POST method or there are form errors
    departments = Department.objects.all()  # Assuming you have a Department model
    
    return render(request, 'marketplace/add.html', {'departments': departments})

    




def viewItem(request, pk):

    
    return render(request, 'marketplace/item.html')


def productPage(request):

    return render(request, 'marketplace/products.html')


def aboutUs(request):

    return render(request,'marketplace/aboutus.html')


def faq(request):

    return render(request, 'marketplace/faq.html')


def books(request):

    return render(request, 'marketplace/books.html')
