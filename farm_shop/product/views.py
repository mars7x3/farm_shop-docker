from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import *
from django.views import View
from .forms import OrderForm
from .models import *
from django.contrib import messages


class ProductListView(ListView):
    model = Product
    template_name = 'product/products.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        """Get the context for this view."""
        queryset = object_list if object_list is not None else self.object_list
        page_size = self.get_paginate_by(queryset)
        context_object_name = self.get_context_object_name(queryset)
        categories = Category.objects.all()
        if page_size:
            paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, page_size)
            context = {
                'paginator': paginator,
                'page_obj': page,
                'is_paginated': is_paginated,
                'object_list': queryset,
                'categories': categories
            }
        else:
            context = {
                'paginator': None,
                'page_obj': None,
                'is_paginated': False,
                'object_list': queryset,
                'categories': categories
            }
        if context_object_name is not None:
            context[context_object_name] = queryset
        context.update(kwargs)
        return super().get_context_data(**context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'


class ContentView(ListView):
    model = Content
    template_name = 'product/home.html'
    context_object_name = 'company'


class CategoryListView(ListView):
    model = Category
    template_name = 'product/products.html'
    context_object_name = 'categories'


class ContactView(ListView):
    model = Content
    template_name = 'product/contact.html'


class OrderCreateView(View):
    @staticmethod
    def post(request, *args, **kwargs):
        form = OrderForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Заявка отправлена')
            return HttpResponseRedirect(redirect_to=reverse_lazy('contacts'))
        messages.add_message(request, messages.ERROR, 'Ошибка отправки данных')
        return HttpResponseRedirect(redirect_to=reverse_lazy('contacts'))