from django.contrib import admin

# Register your models here.

from .models import Photo, Department, Product, ProductImages

admin.site.register(Department)
admin.site.register(Photo)
admin.site.register(Product)
admin.site.register(ProductImages)
