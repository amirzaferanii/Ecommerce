from django.db import models
from Account.models import User
from product.models import Product, Color, Size


class Shipping(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'حمل و نقل'
        verbose_name_plural = 'حمل و نقل ها'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    total_price = models.IntegerField(default=0, verbose_name="کل خرید")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ سفارش')
    shipping_type = models.CharField(max_length=30,blank=True,null=True,verbose_name="نوع ارسال")
    shipping_price = models.IntegerField(default=0,verbose_name='هزینه ارسال')
    total_price = models.IntegerField(default=0, verbose_name="مبلغ کل")
    is_paid = models.BooleanField(default=False, verbose_name='وضعیت پرداخت')
    address = models.TextField(null=True,blank=True)

    def __str__(self):
        return f'{self.user.phone}-{self.user.fullname}'

    class Meta:
        verbose_name_plural = "سفارشات"
        verbose_name = "سفارش"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='سفارش')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items', verbose_name='محصول')
    size = models.CharField(null=True,blank=True,max_length=12, verbose_name='سایز')
    color = models.CharField(null=True,blank=True,max_length=12, verbose_name='رنگ')
    quantity = models.SmallIntegerField(verbose_name='تعداد')
    price = models.PositiveIntegerField(verbose_name='قیمت')
    total = models.PositiveIntegerField(default=0,verbose_name='جمع')


    def __str__(self):
        return f'{self.product.title} - {self.color} - {self.size} - {self.quantity}'

    class Meta:
        verbose_name_plural = "اقلام سفارش"
        verbose_name = "نوع سفارش"



class DiscountCode(models.Model):
    title = models.CharField(max_length=100,unique=True,verbose_name='عنوان')
    percentage = models.SmallIntegerField(default=0,verbose_name='درصد')
    quantity = models.SmallIntegerField(default=0,verbose_name='تعداد')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تخفیف'
        verbose_name_plural = 'تخفیفات'


class UsedDiscount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='کاربر')
    discount = models.ForeignKey(DiscountCode, on_delete=models.CASCADE,verbose_name='کد تخفیف')
    used_at = models.DateTimeField(auto_now_add=True,verbose_name='استفاده شده')

    def __str__(self):
        return f'{str(self.user)} - {self.discount}'

    class Meta:
        unique_together = ('user', 'discount')