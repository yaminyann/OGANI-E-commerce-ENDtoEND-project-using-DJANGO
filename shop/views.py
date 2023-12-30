from django.shortcuts import render,redirect,HttpResponseRedirect
from django.views import View
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from . forms import (
    SignUp,Customar_Registration,Newsletter_form,Contact_form
)
from . models import (
    Product,Cart,Wishlist,Customar,Newsletter,OrderPlaced,Carousel_slider,Contact
)

# Show Pruduct homepage 
class HomePage_View(View):
    def get(self, request):
        fresh_meat = Product.objects.filter(category = 'Fresh Meat')
        vegetables = Product.objects.filter(category = 'Vegetables')
        Fastfood = Product.objects.filter(category = 'Fastfood')
        oranges = Product.objects.filter(category = 'Fruit & Nut Gifts')
        latest_products = Product.objects.filter(latest_products=True)
        
        total_item_in_cart = 0
        total_item_in_wishlist = 0
        if request.user.is_authenticated:
            total_item_in_wishlist = len(Wishlist.objects.filter(user=request.user))
            total_item_in_cart = len(Cart.objects.filter(user=request.user))
       
        # newsletter sdubscribe form
        form = Newsletter_form()
        # carousel slider
        slider = Carousel_slider.objects.all()
        
        context = {
            'form':form,
            'slider':slider,
            'fresh_meat':fresh_meat,
            'vegetables':vegetables,
            'Fastfood':Fastfood,
            'oranges':oranges,
            'total_item_in_cart':total_item_in_cart,
            'total_item_in_wishlist':total_item_in_wishlist,
            'latest_products':latest_products
        }
        return render(request,'common_code/index.html',context)
    
    def post(self,request):
        form = Newsletter_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            data = Newsletter(email=email)
            data.save()
            context = {
                'form':form
            }
            messages.success(request,'Thanks for subscribe the Newsletter !')
            return render(request,'common_code/base.html',context)
         
         
# newspaper subcriber redirect page
def Subscribe_done(request):
    return render(request,'common_code/newslatter.html')
  
    
# Product Details Page
class Product_details(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        item_already_in_cart = False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user))
        related_product = Product.objects.filter(category=product.category)
        total_item_in_cart = 0
        total_item_in_wishlist = 0
        if request.user.is_authenticated:
            total_item_in_wishlist = len(Wishlist.objects.filter(user=request.user))
            total_item_in_cart = len(Cart.objects.filter(user=request.user))
        # pagination
        paginator = Paginator(related_product,9)
        page_number = request.GET.get('page')
        related_product_item = paginator.get_page(page_number)
        context = {
           'item_already_in_cart':item_already_in_cart,
            'product':product,
            'related_product':related_product_item,
            'total_item_in_cart':total_item_in_cart,
            'total_item_in_wishlist':total_item_in_wishlist
        }
        return render(request, 'shop/pr_details.html',context)
    
# Blog Page
def Blog_page(request):
    return render(request, 'shop/blog.html')

# Blog Details Page
def Blog_Details_page(request):
    return render(request, 'shop/blog_details.html')

# Contact page
class Contact_page(View):
    def get(self,request):
        form = Contact_form()
        context = {
            'form':form
            }
        return render(request, 'shop/contact.html',context)
    
    def post(self,request):
        form = Contact_form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            data = Contact(name=name,email=email,message=message)
            data.save()
            context = {
            'form':form
            }
        return render(request, 'shop/contact.html',context)
    

# Shop Page
def Shop_page(request, data=None):
    if data == None:
        product_item = Product.objects.all()
        # product catagory
    elif data == 'meat':
        product_item = Product.objects.filter(category='Fresh Meat')
    elif data == 'vegetables':
        product_item = Product.objects.filter(category='Vegetables')
    elif data == 'fruits_and_nuts':
        product_item = Product.objects.filter(category='Fruit & Nut Gifts')
    elif data == 'berries':
        product_item = Product.objects.filter(category='Fresh Berries')
    elif data == 'ocean_foods':
        product_item = Product.objects.filter(category='Ocean Foods')
    elif data == 'butter_eggs':
        product_item = Product.objects.filter(category='Butter and eggs')
    elif data == 'fastFood':
        product_item = Product.objects.filter(category='Fastfood')
    elif data == 'fresh_onion':
        product_item = Product.objects.filter(category='Fresh Onion')
    elif data == 'papaya_crisps':
        product_item = Product.objects.filter(category='Papayaya & Crisps')
    elif data == 'oatmeal':
        product_item = Product.objects.filter(category='Oatmeal')
    elif data == 'banana':
        product_item = Product.objects.filter(category='Fresh Banana')
        # color category
    elif data == 'white':
        product_item = Product.objects.filter(color='White')
    elif data == 'gray':
        product_item = Product.objects.filter(color='Gray')
    elif data == 'red':
        product_item = Product.objects.filter(color='Red')
    elif data == 'black':
        product_item = Product.objects.filter(color='Black')
    elif data == 'blue':
        product_item = Product.objects.filter(color='Blue')
    elif data == 'green':
        product_item = Product.objects.filter(color='Green')
        # size category
    elif data == 'large':
        product_item = Product.objects.filter(size='Large')
    elif data == 'medium':
        product_item = Product.objects.filter(size='Medium')
    elif data == 'small':
        product_item = Product.objects.filter(size='Small')
    elif data == 'tiny':
        product_item = Product.objects.filter(size='Tiny')
   
    total_product = len(product_item)  
    sale_off_item = Product.objects.all()
    latest_products = Product.objects.filter(latest_products=True)
    # cart & wishlist total item
    total_item_in_cart = 0
    total_item_in_wishlist = 0
    if request.user.is_authenticated:
        total_item_in_wishlist = len(Wishlist.objects.filter(user=request.user))
        total_item_in_cart = len(Cart.objects.filter(user=request.user))
        
    # pagination
    paginator = Paginator(product_item,9)
    page_number = request.GET.get('page')
    product_item_total = paginator.get_page(page_number)
    total_page = product_item_total.paginator.num_pages
    context = {
        'item':product_item_total,
        'last_page':total_page,
        'page_list':[ n+1 for n in range(total_page)],
        'total_product':total_product,
        'sale_off':sale_off_item,
        'total_item_in_cart':total_item_in_cart,
        'total_item_in_wishlist':total_item_in_wishlist,
        'latest_products':latest_products
    }
    return render(request, 'shop/shop.html', context)


# Add product in cart
@login_required
def Add_to_cart(request):
    user = request.user 
    product_id = request.GET.get('product_ID')
    item = Product.objects.get(id=product_id)
    Cart(user=user, product=item).save()
    return redirect('/cart') 

# Add product in Wishlist
def Add_to_wishlist(request):
    user = request.user 
    product_id = request.GET.get('product_ID')
    item = Product.objects.get(id=product_id)
    Wishlist(user=user, product=item).save()
    return redirect('/wishlist')


# Show Wishlist Page
def Wishlist_Item(request):
    if request.user.is_authenticated:
        user = request.user
        wishlist = Wishlist.objects.filter(user=user)
        
        # show number of ammount item
        total_item_in_wishlist = 0
        total_item_in_cart = 0
        if request.user.is_authenticated:
            total_item_in_wishlist = len(Wishlist.objects.filter(user=request.user))
            total_item_in_cart = len(Cart.objects.filter(user=request.user))
            
        context = {
            'wishlist':wishlist,
            'total_item_in_wishlist':total_item_in_wishlist,
            'total_item_in_cart':total_item_in_cart,
        }
        return render(request, 'shop/wishlist_item.html', context)
        
        
        
# Show Cart Page
@method_decorator(login_required, name='dispatch')
class My_cart(View):
    def get(self,request):
        # show number of ammount item
        total_item_in_cart = 0
        total_item_in_wishlist = 0
        if request.user.is_authenticated:
            total_item_in_wishlist = len(Wishlist.objects.filter(user=request.user))
            total_item_in_cart = len(Cart.objects.filter(user=request.user))
                    
        if request.user.is_authenticated:
            user = request.user
            cart = Cart.objects.filter(user=user)
            item_quantity_total = 0.0
            shipping_charge = 120
            total_ammount  = 0.0
            ammount  = 0.0
            cart_item = [ p for p in Cart.objects.all() if p.user == user]
            if cart_item:
                for item in cart_item:
                    temp_ammount = (item.quantity * item.product.discount_price)
                    ammount += temp_ammount
                    total_ammount = shipping_charge + ammount
                    context = {
                        'user_cart':cart,
                        'item_quantity_total':item_quantity_total,
                        'ammount':ammount,
                        'total_ammount':total_ammount,
                        'total_item_in_cart':total_item_in_cart,
                        'total_item_in_wishlist':total_item_in_wishlist,
                        'shipping_charge':shipping_charge,
                        }
            
                    return render(request, 'shop/cart.html',context)
            else:
                return render(request, 'shop/empty_cart.html',{'total_item_in_cart':total_item_in_cart,'total_item_in_wishlist':total_item_in_wishlist})



# Quantity incrase 
def plus_Quantity(request):
  if request.method == 'GET':
    prod_id = request.GET['prod_id']
    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.quantity += 1
    c.save()
    
    user = request.user
    item_quantity_total = 0.0
    shipping_charge = 120
    ammount  = 0.0
    total_ammount  = 0.0
    cart_item = [ p for p in Cart.objects.all() if p.user == user]
    if cart_item:
        for item in cart_item:
            temp_ammount = (item.quantity * item.product.discount_price)
            ammount += temp_ammount
            total_ammount = shipping_charge + ammount

            # show number of ammount item
            total_item_in_cart = 0
            total_item_in_wishlist = 0
            if request.user.is_authenticated:
                total_item_in_wishlist = len(Wishlist.objects.filter(user=request.user))
                total_item_in_cart = len(Cart.objects.filter(user=request.user))
                    
            context = {
                'quantity':c.quantity,
                'item_quantity_total':item_quantity_total,
                'ammount':ammount,
                'total_ammount':total_ammount,
                'total_item_in_cart':total_item_in_cart,
                'total_item_in_wishlist':total_item_in_wishlist,
                'shipping_charge':shipping_charge,
            }
    return JsonResponse(context)



# Quantity decrase
def minus_Quantity(request):
  if request.method == 'GET':
    prod_id = request.GET['prod_id']
    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.quantity -= 1
    c.save()
    
    user = request.user
    item_quantity_total = 0.0
    shipping_charge = 120
    ammount  = 0.0
    total_ammount  = 0.0
    cart_item = [ p for p in Cart.objects.all() if p.user == user]
    if cart_item:
        for item in cart_item:
            temp_ammount = (item.quantity * item.product.discount_price)
            ammount += temp_ammount
            total_ammount = shipping_charge + ammount

            # show number of ammount item
            total_item_in_cart = 0
            total_item_in_wishlist = 0
            if request.user.is_authenticated:
                total_item_in_wishlist = len(Wishlist.objects.filter(user=request.user))
                total_item_in_cart = len(Cart.objects.filter(user=request.user))
                    
            context = {
                'quantity':c.quantity,
                'item_quantity_total':item_quantity_total,
                'ammount':ammount,
                'total_ammount':total_ammount,
                'total_item_in_cart':total_item_in_cart,
                'total_item_in_wishlist':total_item_in_wishlist,
                'shipping_charge':shipping_charge,
            }
    return JsonResponse(context)


# delete Item in Cart
def delete_Item(request):
  if request.method == 'GET':
    prod_id = request.GET['prod_id']
    c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
    c.delete()
    
    user = request.user
    item_quantity_total = 0.0
    shipping_charge = 120
    ammount  = 0.0
    total_ammount  = 0.0
    cart_item = [ p for p in Cart.objects.all() if p.user == user]
    if cart_item:
        for item in cart_item:
            temp_ammount = (item.quantity * item.product.discount_price)
            ammount += temp_ammount
            total_ammount = shipping_charge + ammount

            # show number of ammount item
            total_item_in_cart = 0
            total_item_in_wishlist = 0
            if request.user.is_authenticated:
                total_item_in_wishlist = len(Wishlist.objects.filter(user=request.user))
                total_item_in_cart = len(Cart.objects.filter(user=request.user))
                    
            context = {
                'quantity':c.quantity,
                'item_quantity_total':item_quantity_total,
                'ammount':ammount,
                'total_ammount':total_ammount,
                'total_item_in_cart':total_item_in_cart,
                'total_item_in_wishlist':total_item_in_wishlist,
                'shipping_charge':shipping_charge,
            }
    return JsonResponse(context)


@login_required
# Checkout Page
def CheckOut(request):
    address = Customar.objects.filter(user=request.user)
    item = Cart.objects.filter(user=request.user)
    # show number of ammount item
    total_item_in_cart = 0
    total_item_in_wishlist = 0
    if request.user.is_authenticated:
        total_item_in_wishlist = len(Wishlist.objects.filter(user=request.user))
        total_item_in_cart = len(Cart.objects.filter(user=request.user))
    # ammount calculation
    shipping_charge = 120
    total_ammount  = 0.0
    ammount  = 0.0
    cart_item = [ p for p in Cart.objects.all() if p.user == request.user]
    if cart_item:
        for product in cart_item:
            temp_ammount = (product.quantity * product.product.discount_price)
            ammount += temp_ammount
            total_ammount = shipping_charge + ammount
    context = {
        'address':address,
        'item':item,
        'ammount':ammount,
        'total_ammount':total_ammount,
        'total_item_in_cart':total_item_in_cart,
        'total_item_in_wishlist':total_item_in_wishlist,
    }
    return render(request, 'shop/checkout.html',context)


@login_required
# Order status 
def Order_status(request):
    user = request.user
    custid = request.GET.get('Customar_ID')
    customar = Customar.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user,customar=customar,product=c.product,quantity=c.quantity).save()
        c.delete()
    status = OrderPlaced.objects.filter(user=request.user)
    context = {
        'status':status
        }
    return render(request, 'shop/order_status.html',context)


@login_required
# My Order
def My_order(request):
    status = OrderPlaced.objects.filter(user=request.user)
    context = {
        'status':status
        }
    return render(request, 'shop/order_status.html',context)

# Signup page
class SingUp_View(View):
    def get(self,request):
        form = SignUp()
        data = {
            'form':form
        }
        return render(request, 'common_code/signup.html',data)
    
    def post(self, request):
        form = SignUp(request.POST)
        if form.is_valid():
            messages.success(request, 'Contratulations Registration successfull')
            form.save()
        data = {
            'form':form
        }
        return render(request, 'common_code/signup.html', data)
    
    
# Searce Item
def Searce(request):
    total_item_in_cart = 0
    total_item_in_wishlist = 0
    if request.user.is_authenticated:
        total_item_in_cart = len(Cart.objects.filter(user=request.user))
        total_item_in_wishlist = len(Wishlist.objects.filter(user=request.user))
        
    if request.method == 'GET':
        quary = request.GET.get('quary')
        if quary :
            searce_item = Product.objects.filter(title__icontains=quary)
            total = len(searce_item)
        context = {
            'total':total,
            'searce_item':searce_item,
            'total_item_in_wishlist':total_item_in_wishlist,
            'total_item_in_cart':total_item_in_cart
        }
        return render(request, 'common_code/searce_item.html', context)
    
    else:
        return render(request, 'common_code/searce_item.html', context)
    
# Customar Profile
@method_decorator(login_required, name='dispatch')
class Add_delivery_address(View):
    def get(self,request):
        form = Customar_Registration()
        context = {
            'form':form
        }
        return render(request, 'profile/add_address.html', context) 
    
    def post(self,request):
        form = Customar_Registration(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            division = form.cleaned_data['division']
            district = form.cleaned_data['district']
            zipcode = form.cleaned_data['zipcode']
            area = form.cleaned_data['area']
            mobile = form.cleaned_data['mobile']
            effective_delivery = form.cleaned_data['effective_delivery']
            address_book = Customar(
                user=user,name=name,division=division,district=district,
                zipcode=zipcode,area=area,mobile=mobile,effective_delivery=effective_delivery
            )
            address_book.save()
            messages.success(request, 'Addrsss update successfully !')
            context = {
            'form':form,
            }
            return render(request,'profile/add_address.html',context)
        else:
            return render(request,'profile/add_address.html',{'form':form})
            
# add address
@login_required
def profile(request):
    profile_info = Customar.objects.filter(user=request.user) 
    return render(request, 'profile/profile.html',{'profile_info':profile_info})

# address book
@login_required
def addressBook(request):
    address = Customar.objects.filter(user=request.user)
    context = {
        'address':address,
    }
    return render(request, 'profile/address_book.html',context)

# order 
@login_required
def Orders(request):
    all_orders = OrderPlaced.objects.filter(user=request.user)
    context = {
        'all_orders':all_orders
    }
    return render(request,'profile/order.html',context)

# Change password
@method_decorator(login_required, name='dispatch')
class Change_Password(View):
    def get(self,request):
        return render(request,'password/change_pass.html')
    
