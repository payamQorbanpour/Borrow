from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shop'

urlpatterns = [
    url(r'^create/$', views.product_create, name='product_create'),
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^categories/(?P<location_slug>[-\w]+)/$', views.product_list, name='product_list_by_location'),
    url(r'^(?P<uuid>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
