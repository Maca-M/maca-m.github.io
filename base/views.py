from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Product

class Login(LoginView) :
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('products')

class ListProducts(LoginRequiredMixin, ListView) :
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwarg):
        context = super().get_context_data(**kwarg)
        #context['products'] = context['products'].filter(user=self.request.user)

        search_value = self.request.GET.get('search') or ''
        if search_value:
            context['products'] = context['products'].filter(code__icontains=search_value) or context['products'].filter(name__icontains=search_value)

        context['search_value'] = search_value

        return context

class DetailProduct(LoginRequiredMixin, DetailView) :
    model = Product
    context_object_name = 'product'

class NewProduct(LoginRequiredMixin, CreateView) :
    model = Product
    context_object_name = 'new-product'
    fields = '__all__'
    success_url = reverse_lazy('products')

    # def form_valid(self, form) :
    #     form.instance.user = self.request.user
    #     return super(NewProduct, self).form_valid(form)


class EditProduct(LoginRequiredMixin, UpdateView) :
    model = Product
    context_object_name = 'product'
    fields = '__all__'
    success_url = reverse_lazy('products')

class DeleteProduct(LoginRequiredMixin, DeleteView) :
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('products')