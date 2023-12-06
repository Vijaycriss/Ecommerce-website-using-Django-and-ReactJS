from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customers import Customer
from django.views import View
from store.models.product import Product
from store.models.order import Order

class CheckOut(View):
    
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.POST.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)
        
        
        for products in Product:
            print(cart.get(str(products.id)))
            order = Order(customer = Customer(id=customer),
                           products=products,
                           price = products.price,
                           address = address,
                           phone=phone,
                           quantity = cart.get(str(products.id)))
            order.save()
        request.session['cart'] ={}
        
        return redirect('cart')
                                               
                                               