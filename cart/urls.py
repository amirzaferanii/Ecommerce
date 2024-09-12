from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.CartDetailView.as_view(), name='cart_detail'),
    path('add/<int:pk>', views.CartAddView.as_view(), name='cart_add'),
    path('delete/<str:id>', views.CartDeleteView.as_view(), name='cart_delete'),
    path('update/', views.update_cart_item_quantity, name='update_cart_item_quantity'),
    path('calculate-total-with-shipping/', views.calculate_total_with_shipping, name='calculate_total_with_shipping'),
    path('order/<int:pk>', views.OrderDetailView.as_view(), name='order_detail'),
    path('order/add', views.OrderCreationView.as_view(), name='order_creation'),
    path('discount/<int:pk>', views.ApplyDiscount.as_view(), name='discount'),
]
