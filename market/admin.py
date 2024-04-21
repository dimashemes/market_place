from django.contrib import admin
from django.utils.html import mark_safe
from .models import Product, ProductImages,CartItem, FavoriteItem, Category


class ProductImagesInline(admin.StackedInline):
    model = ProductImages
    extra = 1
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        return mark_safe(f'<img src = "{obj.image.url}" width="50%"/>')
    
    image_preview.short_description = 'Превью картинки'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesInline]
    search_fields = ['name',]

admin.site.register(CartItem)
admin.site.register(FavoriteItem)
admin.site.register(Category)

