from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'updated', )
    search_fields = ( 'title', ) 


class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount','description',  )
    search_fields = ('name', 'price', 'description' ,) 
    list_filter = ('category', 'author__email','price','updated',)

     
    actions = [ 'publish', 'draft' ]
    
    def publish(self, queryset):
        queryset.update(is_pub=True)
        
    def draft(self, queryset):
        queryset.update(is_pub=False)
    
    
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ( 'item', 'quantity','updated', )
    list_filter = ('updated',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ( 'status', 'client','ordered','shipping_fee', )
    search_fields = ( 'client.email', ) 
    list_filter = ('updated','status')
 
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'timestamp', )
    search_fields = ( 'title', ) 
 
 
admin.site.register(CategoryAdmin2)
