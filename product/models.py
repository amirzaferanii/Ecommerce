from django.db import models
from django.utils.html import mark_safe

from Account.models import User


class Category(models.Model):
    parent = models.ForeignKey('self', blank=True,null=True,on_delete=models.CASCADE,related_name="sub_category")
    title = models.CharField(max_length=100)
    slug = models.SlugField()


    def __str__(self):
        return self.title


class Size(models.Model):
    title = models.CharField(max_length=15)

    def __str__(self):
       return self.title

    class Meta:
        verbose_name_plural = 'سایز'


class Color(models.Model):
    title = models.CharField(null=True,blank=True,max_length=15)

    def __str__(self):
       return self.title

    class Meta:
        verbose_name_plural = "رنگ ها"


class Gallery(models.Model):
    image = models.ImageField(upload_to="gallery",null=True,blank=True,verbose_name="تصاویر محصول")

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="40" height="60" />')
        return "No Image"
    image_tag.short_description = 'تصویر'


    class Meta:
        verbose_name_plural = "گالری تصاویر"
        verbose_name = "تصویر"

    def __str__(self):
        return self.image.url if self.image else "No Image"




class Product(models.Model):
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=50,verbose_name="نام محصول")
    description = models.TextField(verbose_name="توضیحات محصول")
    price = models.IntegerField(verbose_name="قیمت")
    discount = models.SmallIntegerField(help_text="این فیلد اجباری نیست",blank=True,null=True,default=0,verbose_name="مبلغ قبل تخفیف")
    size = models.ManyToManyField(Size,blank=True, verbose_name="سایز")
    color = models.ManyToManyField(Color,blank=True, verbose_name="رنگ")
    stock = models.PositiveIntegerField(default=0, verbose_name="موجودی")
    image = models.ImageField(upload_to="products",verbose_name="تصویر محصول")
    gallery = models.ManyToManyField(Gallery,related_name="gallery",verbose_name="تصایر")
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "محصولات"
        verbose_name = "محصول"


    def __str__(self):
       return self.title
#
#
# class Inventory(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="inventories")
#     size = models.ForeignKey(Size,null=True,blank=True, on_delete=models.CASCADE, verbose_name="سایز")
#     color = models.ForeignKey(Color,null=True,blank=True, on_delete=models.CASCADE, verbose_name="رنگ")
#     stock = models.PositiveIntegerField(default=0, verbose_name="موجودی")
#
#     class Meta:
#         unique_together = ('product', 'size', 'color')
#         verbose_name_plural = "موجودی محصولات"
#         verbose_name = "موجودی"
#
#     def __str__(self):
#         return f"{self.product}"
#
#     def decrease_quantity(self, amount):
#         if self.stock >= amount:
#             self.stock -= amount
#             self.save()
#         else:
#             raise ValueError("Not enough stock available")


class Specification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='specifications', verbose_name="محصول")
    key = models.CharField(max_length=50, verbose_name="عنوان ویژگی")
    value = models.CharField(max_length=50, verbose_name="مقدار ویژگی")

    class Meta:
        verbose_name_plural = "مشخصات"
        verbose_name = "مشخصه"

    def __str__(self):
        return f"{self.key}: {self.value}"





class Information (models.Model):
    product = models.ForeignKey(Product,null=True, on_delete=models.CASCADE,related_name="informations")
    text = models.TextField()

    def __str__(self):
        return self.text[:30]



class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey('self',null=True, blank=True,on_delete=models.CASCADE, related_name="reply")
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:30]



class Like(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)