from django.contrib import admin

from products.models import Basket, Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'code', 'marka', 'model',
                    'price_rozn', 'rest', 'name',
                    'season_list', 'thorn')

    fields = ('marka', 'model', 'name', 'price_rozn', 'price',
              'season_list', 'thorn', 'code', 'quality', 'rest',
              'color_disk', 'type_list', 'wrh_list', 'category',
              'description', 'image',)

    readonly_fields = ('code', 'marka',)
    search_fields = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0

