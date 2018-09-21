from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Location
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import AddProductForm
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def product_list(request, category_slug=None, location_slug=None):
    category = None
    categories = Category.objects.all()
    location = None
    locations = Location.objects.all()
    products = Product.objects.filter(available=True)
    paginator = Paginator(products, 8)
    page = request.GET.get('page', 1)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        products = paginator.page(paginator.num_pages)
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
               'products': products,
               'page': page,
               }
    return render(request, 'shop/product/list.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})

@login_required
def product_create(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse('account:login'))

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
