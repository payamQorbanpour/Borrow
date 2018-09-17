from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Location

# Create your views here.

def product_list(request, category_slug=None, location_slug=None):
    category = None
    categories = Category.objects.all()
    location = None
    locations = Location.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    elif location_slug:
        location = get_object_or_404(Location, slug=location_slug)
        products = products.filter(location=location)
    return render(request, 'shop/product/list.html', {'category': category, 'categories': categories, 'location': location, 'locations': locations, 'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})
