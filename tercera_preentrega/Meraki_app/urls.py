from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # página de inicio
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),  # agregar productos
    path('productos/', views.lista_productos, name='lista_productos'),  # lista de productos
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),  # detalles del producto
    path('stock/', views.lista_stock, name='lista_stock'),  # lista de stock
    path('precios/', views.lista_precios, name='lista_precios'),  # lista de precios
]