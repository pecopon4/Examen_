from django.contrib import admin
from django.urls import path, include
from django import views
from Evaluacion2App.views import carro, listar_producto

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Evaluacion2App.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('Evaluacion2App/templates/crud.html', listar_producto, name = 'listarproductos'),
]
