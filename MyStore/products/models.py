import os
import uuid
from django.db import models



# class Articles(models.Model):
#     title = models.CharField('Название', max_length=50)
#     anons = models.CharField('Анонс', max_length=250)
#     full_text = models.TextField('Статья')
#     date = models.DateTimeField('Дата публикации')
#     image = models.ImageField('Изображение', upload_to='media/articles/')  # Новое поле для изображения
#
#     def __str__(self):
#         return self.title
#
#     def get_absolute_url(self):
#         return f'/products/{self.id}'
#
#     class Meta:
#         verbose_name = 'Товар'
#         verbose_name_plural = 'Товары'

# Начинаем работать с PostgreSQL

def notebook_image_upload_to(instance, filename):
    # Генерируем уникальный ID для файла
    unique_id = uuid.uuid4()
    # Получаем расширение файла
    extension = filename.split('.')[-1]
    # Создаем новое имя файла
    new_filename = f'notebook_{unique_id}.{extension}'
    return os.path.join('notebooks/', new_filename)

class Notebook(models.Model):
    brand = models.CharField(max_length=100)  # Бренд ноутбука
    model = models.CharField(max_length=100)  # Модель ноутбука
    processor = models.CharField(max_length=100)  # Процессор
    ram = models.PositiveIntegerField()  # Оперативная память (в ГБ)
    storage = models.PositiveIntegerField()  # Хранилище (в ГБ)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    description = models.TextField(blank=True)  # Описание
    image = models.ImageField(upload_to=notebook_image_upload_to, blank=True)  # Изображение ноутбука

    class Meta:
        db_table = 'products_notebook'  # Указываем название таблицы

    def __str__(self):
        return f"{self.brand} {self.model}"

class Monitor(models.Model):
    model = models.CharField(max_length=100)  # Модель ноутбука
    processor = models.CharField(max_length=100)  # Процессор

    class Meta:
        db_table = 'products_monitor'  # Указываем название таблицы

    def __str__(self):
        return f"{self.model}"
