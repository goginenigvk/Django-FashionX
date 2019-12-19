from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from products.models import Products
from django.db.models import Max,Avg
from products.forms import PersonForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import ContactForm
from django.contrib import messages


# Create your views here.

def list_products(request):
    messages.add_message(request, messages.INFO, 'Fahsionx')
    messages.info(request, 'Listing the products.')
    x=Products.objects.all()[0:1]
    allproducts=Products.objects.all()
    print(allproducts.query)
  
    context={
        'raja':allproducts,
        'mahendra':x
    }
    return render(request,'products.html',context)

def list_products_details(request,id):
    product_details=Products.objects.filter(id=id).select_related()
    print(product_details.query)
    context={
        'product_info': product_details
    }
    return render(request,'productdetails.html',context)


def all_queries(request):
    all_product_count =Products.objects.all().count()
    # countQuery=str(all_product_count.query)
    # print(countQuery)

    all_product_max_cost =Products.objects.all().aggregate(Max('product_cost'))
    all_product_avg_cost =Products.objects.all().aggregate(Avg('product_cost'))

    second_largest_row=Products.objects.order_by('-product_published_date')[1]
    get_cost_less_than_3000= Products.objects.filter(product_cost__lte=3000)
    
    get_prodcost_prodname=Products.objects.filter(
        product_name__startswith='u',
        product_category__product_category_name__istartswith='t'
    ).select_related()

    get_disctint_product_name=Products.objects.distinct('product_name').order_by('-product_name')
    context={
        'all_product_count':all_product_count,

        'all_product_max_cost':all_product_max_cost,
        'all_product_avg_cost':all_product_avg_cost,

        'second_largest_row':second_largest_row,
        'get_cost_less_than_3000':get_cost_less_than_3000,

        'get_prodcost_prodname':get_prodcost_prodname,
        'get_disctint_product_name':get_disctint_product_name,
    }

    return render(request,'productdata.html',context)


def getPersonDetails(request):
  
    if request.method == 'POST':
       form=PersonForm(request.POST) 
       if form.is_valid():
           print(form.cleaned_data)
           return HttpResponseRedirect('/products/')

    else:
       form=PersonForm(initial={'name1':"DOE"})
       age=form.fields['age']
       print(age)

    context={
        'form':form
    }
    return render(request,'person/person.html',context)


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
      
        if form.is_valid():
            form.save()
           
            return redirect('listproducts')
    else:
        form=UserCreationForm()
    return render(request, 'person/signup.html', {'form': form})


def contact_view(request):
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('you are succefully completed the form')

    else:
        form=ContactForm
    
    return render(request,'person/contact.html',{'form':form})


def logout_view(request):
    logout(request)

    return redirect("login")

