from django.shortcuts import render, get_object_or_404
from .models import Notebook
# from .forms import ArticlesForm
# from django.views.generic import DetailView, UpdateView, DeleteView


def products_home(request):
    return render(request, 'products/products_home.html')
#
#
# class ProductsDetailView(DetailView):
#     model = Articles
#     template_name = 'products/details_view.html'
#     context_object_name = 'article'
#
#
# class ProductsUpdateView(UpdateView):
#     model = Articles
#     template_name = 'products/create.html'
#
#     form_class = ArticlesForm
#
#
# class ProductsDeleteView(DeleteView):
#     model = Articles
#     success_url = '/products'
#     template_name = 'products/products-delete.html'
#
#
# def create(request):
#     error = ''
#     if request.method == 'POST':
#         form = ArticlesForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('products_home')
#         else:
#             error = 'Форма была неверной'
#
#     form = ArticlesForm()
#
#     data = {
#         'form': form,
#         'error': error
#     }
#     return render(request, 'products/create.html', data)


def computer_case(request):
    return render(request, 'products/computer_case.html')

def notebooks(request):
    notebooks_list = Notebook.objects.all()  # Получаем все объекты Notebook
    context = {
        'notebooks': notebooks_list,  # Передаем список ноутбуков в контекст
    }
    return render(request, 'products/notebooks.html', context)

def monitors(request):
    return render(request, 'products/monitors.html')

def accessories(request):
    return render(request, 'products/accessories.html')

def notebook_detail(request, id):
    notebook = get_object_or_404(Notebook, id=id)  # Получаем ноутбук по id
    context = {
        'notebook': notebook,  # Передаем найденный объект в шаблон
    }
    return render(request, 'products/notebook_detail.html', context)