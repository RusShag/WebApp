import os
import uuid
from django.contrib.auth.models import User
from django.db import models

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return sum(item.total_price() for item in self.items.all())

    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

# Функция для уникального имени загружаемого изображения
def product_image_upload_to(instance, filename):
    unique_id = uuid.uuid4()
    extension = filename.split('.')[-1]
    new_filename = f'product_{unique_id}.{extension}'
    return os.path.join('products/', new_filename)

# Модель категории товаров (например, "Ноутбуки", "Мониторы" и т.д.)
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='categories/', blank=True)

    class Meta:
        db_table = 'products_category'

    def __str__(self):
        return self.name

# Общая модель товара
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100, blank=True)  # Новое поле
    ram = models.PositiveIntegerField(blank=True, null=True)  # Новое поле
    storage = models.PositiveIntegerField(blank=True, null=True)  # Новое поле
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=product_image_upload_to, blank=True)

    class Meta:
        db_table = 'products_product'

    def __str__(self):
        return self.name

# ----- СТАРЫЕ МОДЕЛИ, ВРЕМЕННО ОТКЛЮЧЕНЫ -----

# def notebook_image_upload_to(instance, filename):
#     unique_id = uuid.uuid4()
#     extension = filename.split('.')[-1]
#     new_filename = f'notebook_{unique_id}.{extension}'
#     return os.path.join('notebooks/', new_filename)

# class Notebook(models.Model):
#     brand = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#     processor = models.CharField(max_length=100)
#     ram = models.PositiveIntegerField()
#     storage = models.PositiveIntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField(blank=True)
#     image = models.ImageField(upload_to=notebook_image_upload_to, blank=True)

#     class Meta:
#         db_table = 'products_notebook'

#     def __str__(self):
#         return f"{self.brand} {self.model}"

# class Monitor(models.Model):
#     model = models.CharField(max_length=100)
#     processor = models.CharField(max_length=100)

#     class Meta:
#         db_table = 'products_monitor'

#     def __str__(self):
#         return f"{self.model}"