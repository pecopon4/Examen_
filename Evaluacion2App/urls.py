from django.urls import URLPattern, path
from django.conf.urls import include
from . import views
from .views import listar_producto

urlpatterns = [
    path('', views.index, name = 'index'),
    path('index.html', views.index, name = 'index'),
    #path('cart.html', views.carro, name = 'carro'),
    path('my-account.html', views.mi_cuenta, name = 'mi_cuenta'),
    path('wishlist.html', views.deseos, name = 'deseos'),
    path('contact.html', views.contacto, name = 'contacto'),
    path('product-detail.html', views.productos, name = 'productos'),
    path('gatos.html', views.gatos, name = 'gatos'),
    path('perros.html', views.perros, name = 'perros'),
    #path('checkout.html', views.pago, name = 'pago'),
    #path('salir/', views.salir, name = "salir"),
    path('crud.html', views.crud, name = 'crud'),
    #path('registration/login.html', views.login, name = 'login'),
    path('crud.html', listar_producto, name = 'listarproductos'),
    path('store.html', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

]