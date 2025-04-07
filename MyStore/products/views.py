from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def products_home(request):
    products = Articles.objects.order_by('-date')
    return render(request, 'products/products_home.html', {'products': products})


class ProductsDetailView(DetailView):
    model = Articles
    template_name = 'products/details_view.html'
    context_object_name = 'article'


class ProductsUpdateView(UpdateView):
    model = Articles
    template_name = 'products/create.html'

    form_class = ArticlesForm


class ProductsDeleteView(DeleteView):
    model = Articles
    success_url = '/products'
    template_name = 'products/products-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'products/create.html', data)