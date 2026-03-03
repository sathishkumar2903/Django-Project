from django.contrib import admin
from .models import *
# from .models import Catagroy
# from .models import Product


# Register your models here.
class CatagroyAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'description')

admin.site.register(Catagory,CatagroyAdmin)
admin.site.register(Product)