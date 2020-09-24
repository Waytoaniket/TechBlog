from django.contrib import admin

# Register your models here.
from .models import Product, Video, GamingProduct

admin.site.register(Product)
admin.site.register(Video)
admin.site.register(GamingProduct)



