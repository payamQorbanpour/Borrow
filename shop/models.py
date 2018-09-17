from django.db import models
from django.urls import reverse
from phone_field import PhoneField
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from shop.choices import *

# Create your models here.

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
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=1)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=200, default="")
    phone_regex = RegexValidator(regex=r'^\+?09?\d{9,15}$', message="Phone number must be entered in the format: '09123456789'. Up to 11 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=11, help_text="Enter your number formatted like: 09********")
    status = models.IntegerField(choices=STATUS_CHOICES, default='1')
    health = models.PositiveIntegerField(default=10,
                                        validators=[MinValueValidator(0),MaxValueValidator(100),],
                                        help_text="How healthy is your thing out of 100?",
                                        blank=False)

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    def special(self):
        if self.status == 2:
            return True
        else:
            return False
