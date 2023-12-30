from django.contrib import admin
from . models import (
    Product,Cart,Wishlist,Customar,Newsletter,OrderPlaced,Carousel_slider,Contact
)
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'category',
        'color',
        'size',
        'selling_price',
        'discount_price',
        'discription',
        'information',
        'reviews',
        'p_image',
        'p_image1',
        'p_image2',
        'p_image3',
        'p_image4',
        'availability',
        'shipping',
        'weight',
        'sale_off_discount_parcent'
    ]
    
@admin.register(Cart)
class Cart_Admin(admin.ModelAdmin):
    list_display = [
        'id','user','product','quantity'
    ]
    
@admin.register(Wishlist)
class Wishlist_Admin(admin.ModelAdmin):
    list_display = [
        'id','user','product'
    ]
@admin.register(Customar)
class Customar_admin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'name',
        'division',
        'district',
        'zipcode',
        'area',
        'mobile',
        'effective_delivery'
    ]
@admin.register(Newsletter)
class Newsletter_admin(admin.ModelAdmin):
    list_display = [
        'id',
        'email',
    ]
@admin.register(OrderPlaced)
class OrderPlaced_admin(admin.ModelAdmin):
    list_display = [
        'id',
        'user',
        'customar',
        'product',
        'order_date',
        'quantity',
        'status'
    ]
@admin.register(Carousel_slider)
class Carousel_slider_admin(admin.ModelAdmin):
    list_display = [
        'id',
        'sub_title',
        'titie',
        'discription',
        'image',
    ]
@admin.register(Contact)
class Contact_admin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'email',
        'message',
    ]
