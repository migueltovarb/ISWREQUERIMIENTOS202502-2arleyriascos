from django.urls import path
from . import views

urlpatterns = [

    path('', views.inicio, name='inicio'),
    # Página principal → lista de productos
    path('', views.lista_productos, name='lista_productos'),

    # CRUD de productos
    path('productos/', views.lista_productos, name='lista_productos'),
    path('productos/registrar/', views.registrar_producto, name='registrar_producto'),

    # Movimientos de inventario
    path('movimientos/entrada/', views.registrar_entrada, name='registrar_entrada'),
    path('movimientos/salida/', views.registrar_salida, name='registrar_salida'),
    
    path('productos/editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),
]