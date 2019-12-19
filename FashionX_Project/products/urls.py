
from django.urls import path
from . import views


urlpatterns = [
    path('listproducts/',views.list_products,name='list_products'),
    path('listproducts/<int:id>',views.list_products_details,name='list_products_details'),
    path('all_queries/',views.all_queries,name='all_queries'),
    path('person_form/',views.getPersonDetails,name='person_form'),
    path('signup/',views.signup_view,name='signup'),
    path('contact/',views.contact_view,name='contact'),
    path('logout/',views.logout_view,name='logoutnew')
]
