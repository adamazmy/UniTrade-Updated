from django.contrib import admin

# Register your models here.

from .models import Photo, Department

admin.site.register(Department)
admin.site.register(Photo)
