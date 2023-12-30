from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
from . forms import (
    Login, Email_Submit_Form, passwordChangeForm
)


urlpatterns = [
    path('', views.HomePage_View.as_view(), name='home'),
    path('searce/',views.Searce, name='searce'),
    # newsletter 
    path('newsletter/',views.Subscribe_done, name='newsletter'),
    # account
    path('signup/', views.SingUp_View.as_view(), name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='common_code/login.html', authentication_form=Login, ), name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    # profile
    path('profile/',views.profile, name='profile'),
    path('add-address/', views.Add_delivery_address.as_view(), name='add_address'),
    path('address-book/',views.addressBook, name='address_book'),
    path('orders/',views.Orders, name='orders'),
    # blog
    path('blog', views.Blog_page, name='blogs'),
    path('blog-details/', views.Blog_Details_page, name='blog_details'),
    path('contact/', views.Contact_page.as_view(), name='contact'),
    # shop
    path('shop/' ,views.Shop_page, name='shop'),
    path('shop/<slug:data>/' ,views.Shop_page, name='shop_page'),
    path('product-details/<int:pk>/', views.Product_details.as_view(), name='product_details'),
    # cart
    path('addTocart/',views.Add_to_cart,name='addTocart'),
    path('cart/',views.My_cart.as_view(), name='cart'),
    path('cart/<int:pk>/',views.My_cart.as_view(), name='cart'),
    # wishlist
    path('addTowishlist/',views.Add_to_wishlist),
    path('wishlist/', views.Wishlist_Item, name='wishlist_item'),
    # quantity 
    path('pluscart/',views.plus_Quantity, name='plus'),
    path('minuscart/',views.minus_Quantity, name='minus'),
    path('removecart/',views.delete_Item, name='delete_item'),
    # checkout
    path('checkout/',views.CheckOut,name='checkout'),
    path('orderStatus/',views.Order_status,name='orderStatus'),
    path('my-order/',views.My_order, name='myOrder'),
    # change password
    path('change-password/',auth_views.PasswordChangeView.as_view(template_name='password/change_pass.html',form_class=passwordChangeForm, success_url='/passwordchangedone/'),name='change_pass'),
    path('password-change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='password/change_done.html'),name='passwordchangedone'),
    # password reset
    path('password_reset/',auth_views.PasswordResetView.as_view(form_class=Email_Submit_Form, template_name='password/email_reset.html'), name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password/email_popup.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password/set_pass.html'),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='password/complete_reset.html'),name='password_reset_complete'),
    
    
]+ static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)