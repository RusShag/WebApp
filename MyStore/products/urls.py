
from django.urls import path
from . import views


urlpatterns = [
  path('', views.products_home, name='products_home'),
  # path('create', views.create, name='create'),
  path('computer_case', views.computer_case, name='computer_case'),
  path('notebooks', views.notebooks, name='notebooks'),
path('notebook/<int:id>/', views.notebook_detail, name='notebook_detail'),
  path('monitors', views.monitors, name='monitors'),
  path('accessories', views.accessories, name='accessories'),
]
