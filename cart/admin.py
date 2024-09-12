from django.contrib import admin


from . import models


admin.site.register(models.Shipping)

class OrderItemInline(admin.TabularInline):
    model = models.OrderItem
    extra = 0


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'created_at', 'is_paid')
    inlines = (OrderItemInline,)
    list_filter = ('created_at', 'is_paid')


@admin.register(models.DiscountCode)
class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'percentage', 'quantity')



@admin.register(models.UsedDiscount)
class UsedDiscountCodeAdmin(admin.ModelAdmin):
    list_display = ('user', 'discount', 'used_at')

