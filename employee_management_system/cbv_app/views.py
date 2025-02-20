from django.shortcuts import render,HttpResponse
from cbv_app.models import Product
from django.urls import reverse_lazy

# Create your views here.
from django.views import View
from django.views.generic import CreateView,UpdateView,DeleteView,ListView

def index(request):
    prds=Product.objects.all()
    return render(request,'show.html',{'prds':prds})

class Myclass(View):
    def get(self, request):
        return HttpResponse("Views from Classs")
    
class CreateProd(CreateView):
    model=Product
    fields='__all__'
    template_name='create.html'
    success_url=reverse_lazy('show')

class UpdateProd(UpdateView):
    model=Product
    fields=['prod_name','price','quantity']
    template_name='update.html'
    success_url=reverse_lazy('show')

class DeleteProd(DeleteView):
    model=Product
    template_name='delete.html'
    success_url=reverse_lazy('show')

class ListProd(ListView):
    model=Product
    template_name='product_list.html'
    