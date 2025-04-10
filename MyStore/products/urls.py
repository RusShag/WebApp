
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
  path('<int:pk>/', views.product_detail, name='product_detail'),
  path('categories/', views.categories_list, name='categories_list'),
  path('categories/<slug:slug>/', views.category_detail, name='category_detail'),
  path('register/', views.register, name='register'),
  path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
  path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
  path('cart/', views.cart_view, name='cart_view'),
  path('update-cart/', views.update_cart, name='update_cart'),
  path('remove-from-cart/', views.remove_from_cart, name='remove_from_cart'),
]
