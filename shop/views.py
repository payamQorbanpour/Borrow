from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Location
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import AddProductForm

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
    context = {'category': category,
               'categories': categories,
               'location': location,
               'locations': locations,
               'products': products
               }
    return render(request, 'shop/product/list.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})

def product_create(request):
    if not request.user.is_authenticated:
        raise Http404

    form = AddProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        # instance.user = request.user
        instance.save()

        messages.success(request, "Successfully created.")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form" : form,
    }
    return render(request, "shop/product/create.html", context)
