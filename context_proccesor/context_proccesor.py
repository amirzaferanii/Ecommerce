



CART_SESSION_ID = 'cart'

def cart_item_count(request):
    cart = request.session.get(CART_SESSION_ID, {})
    cart_length = len(cart)
    return {'cart_item_count': cart_length}