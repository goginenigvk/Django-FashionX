from django.shortcuts import render
from django.views import View
from .models import Order,OrderReciepts
from django.http import HttpResponseRedirect
from .forms import OrderForm,OrderRecieptForm
from django.urls import reverse
from django.core.paginator import Paginator
# Create your views here.

class ListOrders(View):
   def get(self,request):
        allorders=Order.objects.all()
        p=Paginator(allorders,3)
        page = request.GET.get('page')
        allorders = p.get_page(page)
        context={
            'orderpost':allorders,
        }
        return render(request,'listorders.html',context)
    
    
class OrderFormView(View):  
    def get(self,request):
        if request.method == 'POST':
            form=OrderForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('list_orders'))             
        else:
            form=OrderForm
            
        return render(request,'orderform.html',{'form':form})
        
    def post(self,request):
        if request.method == 'POST':
            form=OrderForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('list_orders'))           
        else:
            form=OrderForm
            
        return render(request,'orderform.html',{'form':form})



def order_reciept_upload_file(request):
    if request.method == 'POST':
        form = OrderRecieptForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = OrderRecieptForm()
        print(form)
    return render(request, 'orderreciept.html', {'form': form})
        
            
         


