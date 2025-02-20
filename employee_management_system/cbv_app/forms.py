from django import forms
from cbv_app.models import Product
from django.views.generic import CreateView,UpdateView, DeleteView
from django.urls import reverse_lazy

class ProductForm(forms.ModelForm):
    model=Product
    fields='__all__'

class CreateProd(CreateView):
    model=Product
    fields='__all__'
    template='create.html'
    success_url=reverse_lazy('prod_list')
    
class UpdateProd(UpdateView):
    model=Product
    fields=['prod_name','price','quantity']
    template='update.html'
    success_url=reverse_lazy('prod_list')

class DeleteProd(DeleteView):
    model=Product
    fields=['prod_name','price','quantity']
    template='delete.html'
    success_url=reverse_lazy('prod_list')

