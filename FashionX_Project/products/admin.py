from django.contrib import admin
from products.models import Products,ProductCategory,Contact
from django.contrib.admin import AdminSite


# Register your models here.

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('product_category_name','product_category_slug')
    prepopulated_fields={'product_category_slug':('product_category_name',)}
admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductsAdmin(admin.ModelAdmin):
     list_display=('product_category','product_name','product_image','product_cost','product_volume','product_published_date','product_size_choices')
     list_filter=('product_category','product_size_choices')
     prepopulated_fields={'product_slug':('product_name',)}

admin.site.register(Products,ProductsAdmin)


#Creating the new admin for Products apps
# this admin will be managing the product app

class ProductAdminSite(AdminSite):
    site_header="FashionX Product Admin" # direct main page header 
    site_title="FashionX Product Admin Portal" #Page title 
    index_title="Welcome to FashionX Product site" # on admin page, sub menu header

product_admin_site= ProductAdminSite(name='productadmin')

product_admin_site.register(Products)
product_admin_site.register(ProductCategory)


class ContactAdminForm(admin.ModelAdmin):
    list_display=('name','email','subject','mobile')


admin.site.register(Contact,ContactAdminForm)









