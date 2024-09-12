from product.models import Product
from .models import Shipping

CART_SESSION_ID = 'cart'



class Cart:

    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart



    def remove_cart(self):
        del self.session[CART_SESSION_ID]



    def __iter__(self):
        cart = self.cart.copy()

        for item in cart.values():
            item['product'] = Product.objects.get(id=int(item['id']))
            item['total'] = int(item['price']) * int(item['quantity'])
            item['unique_id'] = self.unique_id_generator(item['product'].id, item['size'], item['color'])
            yield item


    def unique_id_generator(self, id, size, color):
        result = f'{id}-{size}-{color}'
        return result


    def add(self,product,size,color,quantity):
        unique = self.unique_id_generator(product.id, size, color)
        if unique not in self.cart:
            self.cart[unique] = {'quantity': 0, 'price': str(product.price), 'size': size, 'color': color, 'id': product.id}
        self.cart[unique]['quantity'] += int(quantity)
        self.save()



    def delete(self, id):
        if id in self.cart:
            del self.cart[id]
            self.save()

    def update_quantity(self, unique_id, quantity_change):
        if unique_id in self.cart:
            self.cart[unique_id]['quantity'] += quantity_change
            if self.cart[unique_id]['quantity'] <= 0:
                self.delete(unique_id)
            else:
                self.save()

    def sub_total(self):
        cart = self.cart.values()
        sub_total = sum(int(item['price']) * int(item['quantity']) for item in cart)
        return sub_total


    def shipping(self):
        cart = self.cart.values()
        shipping = Shipping.objects.get(title='Post').price
        ship = sum(shipping * int(item['quantity'])for item in cart)
        return ship

    def remove_cart(self):
        del self.session[CART_SESSION_ID]

    def total(self, shipping_title=None):
        sub_total = self.sub_total()
        shipping_cost = 0
        if shipping_title == 'Post':
            shipping_cost = self.shipping()
        return sub_total + shipping_cost

    def save(self):
        self.session.modified = True







