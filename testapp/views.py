from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import CreateView,ListView,DetailView,UpdateView
from testapp.models import Product
from django.core.paginator import Paginator

# Create your views here.

class ProductCreate(CreateView):
    model=Product
    fields= ['ProductId','ProductName','CategoryId','CategoryName']

class ProductList(ListView):
    model=Product

class ProductDetail(DetailView):
    model=Product

class ProductUpdate(UpdateView):
    model=Product
    fields=['ProductId','ProductName','CategoryId','CategoryName']

def listing(request):
    student_list=Product.objects.all()
    paginator= Paginator(product_list,2)

    page_number=request.Get.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,'testapp/product_list.html',{'page_obj':page_obj,'student_list':student_list})
