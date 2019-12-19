"""FashionX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.models import User,Group
from django.urls import path,include
from django.conf import settings
from products.admin import product_admin_site


from django.conf.urls.static import static
from django.conf import settings # new

admin.site.site_header="FashionX Admin" # direct main page header 
admin.site.site_title="FashionX Admin Portal" #Page title 
admin.site.index_title="Welcome to FashionX web platform" # on admin page, sub menu header

# below code is for unregister the existing apps from admin
""" admin.site.unregister(User)
admin.site.unregister(Group)
 """

urlpatterns = static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+[
    path('fashionxadmin/', admin.site.urls),
    path('',include('baseapp.urls')),
    path('products/',include('products.urls')),
    path('productadmin/',product_admin_site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('orders/',include('orders.urls'))
]
