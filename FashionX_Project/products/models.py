from django.db import models
from django import forms
from datetime import datetime
from ckeditor.fields import RichTextField

PRODUCT_SIZE_CHOICES=[
    ('Small','S'),
    ('Medium','M'),
    ('Large','L'),
]

class ProductCategory(models.Model):
    product_category_name=models.CharField(max_length=20)
    product_category_slug=models.SlugField(max_length=20)

    def __str__(self):
        return self.product_category_name

    class Meta:
        verbose_name_plural='Product Categories'


class Products(models.Model):
    product_category=models.ForeignKey('ProductCategory', related_name='ProductCategory', on_delete=models.CASCADE)
    product_name=models.CharField(max_length=40,null=True,blank=True)
    product_slug=models.SlugField(max_length=40)
    product_image=models.ImageField(upload_to='images/product/')
    product_description=RichTextField()
    product_cost=models.FloatField()
    product_volume=models.IntegerField()
    product_published_date=models.DateField(default=datetime.now,blank=True)
    product_size_choices=models.CharField(max_length=20,choices=PRODUCT_SIZE_CHOICES)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name_plural='ProductVS'
        ordering=['product_cost']
        app_label = 'products'
        db_table = 'products_products'
        get_latest_by = "product_published_date"
        required_db_vendor=''

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(help_text='type email with .com')
    subject=models.TextField()
    mobile=models.IntegerField()


    
    