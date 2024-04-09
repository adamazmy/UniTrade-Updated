from django.db import models

# Create your models here.



class Department(models.Model):
    name = models.CharField(max_length = 100, null = False, blank = False)

    def __str__(self):
        return self.name
    
class Photo(models.Model):
    department = models.ForeignKey(Department, on_delete = models.SET_NULL, null = True, blank=True)
    image = models.ImageField(null = False, blank = False)
    description = models.TextField()

    def __str__(self):
        return self.description
    
class Product(models.Model):
    CONDITION_CHOICES = [
        ('pre_owned', 'Pre-owned'),
        ('new_with_box', 'New with Box'),
        ('new_without_box', 'New without Box'),
        ('new_with_defects', 'New with Defects'),
    ]

    title = models.CharField(max_length=255, null=False, blank=False)
    brand = models.CharField(max_length=255, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='new_with_box')
    description = models.TextField()
    product_id = models.AutoField(primary_key=True)
    userID = models.CharField(max_length=100,  null=True)
    # image = models.ImageField(upload_to='product_images/', default='https://png.pngtree.com/png-clipart/20190918/ourmid/pngtree-load-the-3273350-png-image_1733730.jpg')

    def __str__(self):
        return self.title
    

def product_directory_path(instance, filename):
    print("########################################",instance)
    # Access the title of the related Product instance
    product_title_cleaned = instance.title.replace(" ", "_")
    return f'products/{product_title_cleaned}/{filename}'


class ProductImages(models.Model):

    imageID = models.AutoField(primary_key=True)
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    imageURL = models.ImageField(upload_to='product_images/', default='https://png.pngtree.com/png-clipart/20190918/ourmid/pngtree-load-the-3273350-png-image_1733730.jpg')

    ##imageURL = models.ImageField(upload_to=product_directory_path)

    def __str__(self):
        return f"Image {self.imageID} of Product {self.product_id}"

