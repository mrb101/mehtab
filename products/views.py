from django.shortcuts import render

from django.views.generic import TemplateView, CreateView, DetailView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


from models import Category, Product


class IndexTemplate(TemplateView):
    template_name = 'products/index.html'


class AboutTemplate(TemplateView):
    template_name = 'products/about.html'


class ContactTemplate(TemplateView):
    template_name = 'products/contact.html'


class CategoryList(ListView):
    model = Category
    template_name = 'products/category_list.html'
    context_object_name = 'categories'


class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['name']
    template_name = 'products/category_create.html'
    success_url = '/categories/'
    login_url = '/admin/'
    redirect_field_name = 'next'


class CategoryDetail(DetailView):
    model = Category
    template_name = 'products/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryDetail, self).get_context_data(*args, **kwargs)
        categories = Category.objects.all()
        category = self.get_object()
        context['categories'] = categories
        return context


class CategoryUpdate(LoginRequiredMixin, UpdateView):
    model = Category
    fields = ['name']
    template_name = 'products/category_update.html'


class ProductList(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductList, self).get_context_data(*args, **kwargs)
        category = Category.objects.all()
        context['categories'] = category
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetail, self).get_context_data(*args, **kwargs)
        category = Category.objects.all()
        context['categories'] = category
        return context


class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'stock', 'image', 'category']
    template_name = 'products/product_create.html'
    success_url = '/products/'


class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'stock', 'image', 'category']
    template_name = 'products/product_update.html'
    success_url = '/products/'


class CategoryProductsList(DetailView):
    model = Category
    template_name = 'products/category_product_list.html'
    context_object_name = 'category'

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryProductsList, self).get_context_data(*args, **kwargs)
        categories = Category.objects.all()
        category = self.get_object()
        products = Product.objects.filter(category=category)
        context['products'] = products
        context['categories'] = categories
        return context
