# mi_proyecto/urls.py
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
   # path('', include('fabrica.urls')),  # Incluye las URLs de la aplicación fabrica
    path('fabrica/', views.fabrica_view, name='fabrica'),
    path('fabrica/agregar/', views.agregar_producto, name='agregar_producto'),
]
