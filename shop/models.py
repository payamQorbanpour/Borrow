from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from shop.choices import STATUS_CHOICES
from django.conf import settings
from django.utils.text import slugify
import uuid

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'location'
        verbose_name_plural = 'locations'

    def get_absolute_url(self):
        return reverse('shop:product_list_by_location', args=[self.slug])

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    uuid = models.CharField(max_length=200,
                            default=int(uuid.uuid4().time_low),
                            editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             default=1,
                             on_delete=models.CASCADE)
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    # image = models.FileField(upload_to='products/%Y/%m/%d/%f', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=0,
                                null=True,
                                blank=True)
    price_per_day = models.DecimalField(max_digits=10,
                                        decimal_places=0,
                                        null=True,
                                        blank=True)
    price_per_week = models.DecimalField(max_digits=10,
                                         decimal_places=0,
                                         null=True,
                                         blank=True)
    price_per_month = models.DecimalField(max_digits=10,
                                          decimal_places=0,
                                          null=True,
                                          blank=True)
    price_per_year = models.DecimalField(max_digits=10,
                                         decimal_places=0,
                                         null=True,
                                         blank=True)
    stock = models.PositiveIntegerField(default=1)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    location = models.ForeignKey(Location,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?09?\d{9,15}$',
                                 message="Phone number must be entered in \
                                 the format: '09123456789'. Up to 11 \
                                 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex],
                                    max_length=11, help_text="Enter your \
                                    number formatted like: 09123456789")
    status = models.IntegerField(choices=STATUS_CHOICES,
                                 default='1')
    health = models.PositiveIntegerField(default=50,
                                         validators=[MinValueValidator(0),
                                                     MaxValueValidator(100),
                                                     ],
                                         help_text="How healthy \
                                         is your thing out of 100?",
                                         blank=False)
    condition = models.TextField(blank=True)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.uuid, self.slug])

    def promoted(self):
        if self.status == 2:
            return True
        else:
            return False

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Gallery(models.Model):
    product = models.ForeignKey(Product,
                                default=None,
                                on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d/%f',
                              verbose_name='Image',
                              blank=True,
                              null=True)
