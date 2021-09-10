from django.contrib import admin
# .models is a relative import (same directory)
from .models import Product

# Register your models here.
admin.site.register(Product)