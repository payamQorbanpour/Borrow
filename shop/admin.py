from django.contrib import admin
from .models import Category, Product, Location, Gallery

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Location, LocationAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name',
                    'id',
                    'uuid',
                    'slug',
                    'available',
                    'created',
                    'updated',
                    ]
    list_filter = ['available', 'created', 'updated']
    list_editable = ['available', ]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['product', 'image']


admin.site.register(Gallery, GalleryAdmin)
