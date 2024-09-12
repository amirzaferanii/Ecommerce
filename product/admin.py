from django.contrib import admin
from . import models

class InformationAdmin(admin.StackedInline):
    model = models.Information
    extra = 1

class SpecificationAdmin(admin.TabularInline):
    model = models.Specification
    extra = 1



@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title" , "price")
    inlines = (InformationAdmin,SpecificationAdmin)

admin.site.register(models.Color)
admin.site.register(models.Size)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image_tag',)

admin.site.register(models.Gallery, GalleryAdmin)

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'parent')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(models.Comment)

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created')

