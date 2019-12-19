from django.contrib import admin
from .models import Order

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id','order_by','order_location')

admin.site.register(Order, OrderAdmin)

