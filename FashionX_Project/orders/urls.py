
from django.urls import path,include
from orders.views import ListOrders,OrderFormView,OrderReciepts
from . import views 

urlpatterns = [
     path('listorder/',ListOrders.as_view(),name='list_orders'),
     path('orderform/',OrderFormView.as_view(),name='order_form'),
     path('orderrecieptupload/',views.order_reciept_upload_file,name='order_reciept_upload')
]
