from django.contrib import admin

from imagekit.admin import AdminThumbnail

from models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field='image_thumbnail')

admin.site.register(Product)
admin.site.register(Category)
