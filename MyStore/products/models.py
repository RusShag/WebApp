import os
import uuid
from django.db import models

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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
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