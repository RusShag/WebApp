from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'products/category.html', {'categories': categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, 'products/category_detail.html', {
        'category': category,
        'products': products,
    })

def products_home(request):
    return render(request, 'products/products_home.html')

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