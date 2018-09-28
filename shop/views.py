from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Location, Gallery
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import AddProductForm, GalleryForm
from django.contrib.auth.decorators import login_required
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.forms import modelformset_factory

# Create your views here.


def product_list(request, category_slug=None, location_slug=None):
    category = None
    categories = Category.objects.all()
    location = None
    locations = Location.objects.all()
    products = Product.objects.filter(available=True)
    # paginator = Paginator(products, 4) # Number of objects on a page
    page = request.GET.get('page', 1)
    query = request.GET.get("q")
    if query:
        products = products.filter(
              Q(name__contains=query)
            | Q(description__contains=query)
            | Q(category__name__contains=query)
            ).distinct()
    # try:
    #     products = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer deliver the first page
    #     products = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range deliver last page of results
    #     products = paginator.page(paginator.num_pages)
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


def product_detail(request, uuid, slug):
    product = get_object_or_404(Product, uuid=uuid, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})


@login_required
def product_create(request):

    ImageFormSet = modelformset_factory(Gallery, form=GalleryForm, extra=3)
    if request.method == 'POST':

        addProductForm = AddProductForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Gallery.objects.none())

        if addProductForm.is_valid() and formset.is_valid():
            add_product_form = addProductForm.save(commit=False)
            add_product_form.user = request.user
            add_product_form.save()

            for form in formset.cleaned_data:
                try:
                    image = form['image']
                except KeyError:
                    break
                photo = Gallery(product=add_product_form, image=image)
                photo.save()
            messages.success(request,
                             "Your thing was successfuly uploaded!")
            return HttpResponseRedirect("/")
        else:
            print (addProductForm.errors, formset.errors)
    else:
        addProductForm = AddProductForm()
        formset = ImageFormSet(queryset=Gallery.objects.none())
    return render(request, 'shop/product/create.html',
                  {'addProductForm': addProductForm, 'formset': formset})
