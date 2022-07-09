from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import logout
import json
import datetime
from .models import * 
from .utils import cookieCart, cartData, guestOrder

def index (request):
    return render(request, 'index.html')

def carro (request):
    return render(request, 'cart.html')

def mi_cuenta (request):
    return render(request, 'my-account.html')

def deseos (request):
    return render(request, 'wishlist.html')

def contacto (request):
    return render(request, 'contact.html')

def productos (request):
    return render(request, 'product-detail.html')

def gatos (request):
    return render(request, 'gatos.html')

def perros (request):
    return render(request, 'perros.html')

def pago (request):
    return render(request, 'checkout.html')

def login(request):
    return render(request, 'login.html')

def crud(request):
    productos = producto.objects.all()
    return render(request, 'crud.html', {'productos': productos})

def listar_producto(request):
    productos = producto.objects.all()
    return render(request, "crud.html", {"productos" : productos})

def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/store.html', context)


def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)
