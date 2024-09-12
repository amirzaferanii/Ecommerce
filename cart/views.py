from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import JsonResponse
from product.models import Product
from .cart_module import Cart
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Shipping, Order, OrderItem, UsedDiscount
from cart.models import DiscountCode



class CartDetailView(View):
    def get(self,request):
        cart = Cart(request)
        shippings = Shipping.objects.all()
        return render(request,'cart/cart_detail.html',{'cart':cart,'shippings':shippings})


class CartAddView(View):
    def post(self,request, pk):
        product = get_object_or_404(Product,pk=pk)
        size, color, quantity = request.POST.get('size'), request.POST.get('color'), request.POST.get('quantity')
        cart = Cart(request)
        cart.add(product, size, color, quantity)
        return redirect('cart:cart_detail')


class CartDeleteView(View):
    def get(self, request, id, *args, **kwargs):
        cart = Cart(request)
        cart.delete(id)
        return redirect("cart:cart_detail")



@require_POST
@csrf_exempt
def update_cart_item_quantity(request):
    unique_id = request.POST.get('unique_id')
    action = request.POST.get('action')
    cart = Cart(request)

    if action == 'increase':
        cart.update_quantity(unique_id, 1)
    elif action == 'decrease':
        cart.update_quantity(unique_id, -1)

    shipping_title = request.POST.get('shipping_title')
    cart_sub_total = cart.sub_total()
    cart_shipping = cart.shipping() if shipping_title == 'Post' else 0
    item = cart.cart[unique_id]
    item_total = int(item['quantity']) * int(item['price'])
    cart_total = cart.total(shipping_title)

    return JsonResponse({
        'quantity': item['quantity'],
        'item_total': item_total,
        'cart_sub_total': cart_sub_total,
        'shipping': cart_shipping,
        'cart_total': cart_total,
    })



@require_POST
@csrf_exempt
def calculate_total_with_shipping(request):
    shipping_title = request.POST.get('shipping_title')
    cart = Cart(request)
    total_with_shipping = cart.total(shipping_title)
    return JsonResponse({'total_with_shipping': total_with_shipping})



class OrderDetailView(View):
    def get(self,request,pk):
        order = Order.objects.get(id=pk)
        return render(request, 'cart/order_detail.html', {'order':order})


class OrderCreationView(LoginRequiredMixin,View):
    def get(self,request):
        cart = Cart(request)
        shiping = request.GET.get('shiping')
        shipping_cost = cart.shipping() if shiping == 'Post' else 0
        total_price = cart.total(shiping)
        order = Order.objects.create(user=request.user,total_price=total_price, shipping_type=shiping,shipping_price=shipping_cost)
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], color=item['color'], size=item['size'],
                                     price=item['price'], quantity=item['quantity'],total=item['total'])
        cart.remove_cart()
        return redirect('cart:order_detail', order.id)


class ApplyDiscount(View):
    def post(self, request, pk):
        discount_code = request.POST.get('discount_code')
        order = get_object_or_404(Order, pk=pk)
        discount = get_object_or_404(DiscountCode, title=discount_code)

        # چک کردن اینکه آیا کاربر قبلاً از این کد تخفیف استفاده کرده است یا خیر
        if UsedDiscount.objects.filter(user=request.user, discount=discount).exists():
            return redirect('cart:order_detail', order.id)

        if discount.quantity == 0:
            return redirect('cart:order_detail', order.id)

        order.total_price -= order.total_price * discount.percentage / 100
        order.save()

        discount.quantity -= 1
        discount.save()

        # ذخیره استفاده از کد تخفیف برای این کاربر
        UsedDiscount.objects.create(user=request.user, discount=discount)

        return redirect('cart:order_detail', order.id)






