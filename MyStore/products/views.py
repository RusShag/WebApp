from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from .models import Category, Product, CartItem
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)
        cart = request.user.cart  # OneToOneField, поэтому напрямую

        # Проверяем, есть ли уже такой товар
        item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            item.quantity += 1
            item.save()

        return JsonResponse({'success': True, 'message': f'{product.name} добавлен в корзину'})
    return JsonResponse({'success': False, 'message': 'Ошибка запроса'})

@login_required
def cart_view(request):
    cart = request.user.cart
    items = cart.items.select_related('product')  # для оптимизации
    total = cart.total_price()
    return render(request, 'products/cart.html', {'items': items, 'total': total})

@login_required
def update_cart(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        action = request.POST.get('action')
        item = get_object_or_404(CartItem, id=item_id, cart=request.user.cart)

        if action == 'plus':
            item.quantity += 1
        elif action == 'minus':
            if item.quantity > 1:
                item.quantity -= 1
        item.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'message': 'Ошибка запроса'})

@login_required
def remove_from_cart(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item = get_object_or_404(CartItem, id=item_id, cart=request.user.cart)
        item.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'message': 'Ошибка запроса'})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # автоматически входим после регистрации
            return redirect('home')  # или на любую другую страницу
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})

def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'products/category.html', {'categories': categories})

def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)

    sort_by = request.GET.get('sort')  # ← Получаем значение сортировки из GET-параметров

    # Применяем сортировку в зависимости от параметра
    if sort_by == 'name':
        products = products.order_by('name')
    elif sort_by == 'price_asc':
        products = products.order_by('price')
    elif sort_by == 'price_desc':
        products = products.order_by('-price')
    elif sort_by == 'date_new':
        products = products.order_by('-id')  # Самые новые (по id, если нет поля date)
    elif sort_by == 'date_old':
        products = products.order_by('id')

    return render(request, 'products/category_detail.html', {
        'category': category,
        'products': products,
        'current_sort': sort_by,  # ← Передаём выбранную сортировку в шаблон
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

