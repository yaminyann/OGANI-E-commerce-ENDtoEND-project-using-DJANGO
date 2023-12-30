from django.db import models
from django.contrib.auth.models import User


# Customar
DIVISION_CHOICES = (
    ('Dhaka','Dhaka'),
    ('Rangpur','Rangpur'),
    ('Rajshahi','Rajshahi'),
    ('Khulna','Khulna'),
    ('Barishal','Barishal'),
    ('Chattogram','Chattogram'),
    ('Mymenshing','Mymenshing'),
    ('Sylhet','Sylhet'),
)
DELIVERY_CHOICES = (
    ('Home','Home'),
    ('Office','Office'),
)
class Customar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    division = models.CharField(choices=DIVISION_CHOICES, max_length=50)
    district = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    area = models.CharField(max_length=150)
    mobile = models.CharField(default="+880 ", max_length=15)
    effective_delivery = models.CharField(choices=DELIVERY_CHOICES, max_length=50)
    
    def __str__(self):
        return str(self.id)
    
# Product    
CATEGORY_CHOICES = (
    ('Fresh Meat','Fresh Meat'),
    ('Vegetables','Vegetables'),
    ('Fruit & Nut Gifts','Fruit & Nut Gifts'),
    ('Fresh Berries','Fresh Berries'),
    ('Ocean Foods','Ocean Foods'),
    ('Butter and eggs','Butter and eggs'),
    ('Fastfood','Fastfood'),
    ('Fresh Onion','Fresh Onion'),
    ('Papayaya & Crisps','Papayaya & Crisps'),
    ('Oatmeal','Oatmeal'),
    ('Fresh Banana','Fresh Banana'),
)
COLOR_CHOICES = (
    ('White','White'),
    ('Red','Red'),
    ('Blue','Blue'),
    ('Black','Black'),
    ('Gray','Gray'),
    ('Green','Green'),
)
POPULAR_SIZE_CHOICHES = (
    ('Large','Large'),
    ('Medium','Medium'),
    ('Small','Small'),
    ('Tiny','Tiny'),
)
ITEM_PER_CHOICES = (
    ('0.5kg','0.5kg'),
    ('1-KG','Per KG'),
    ('500ml','500ml'),
    ('1 Box','Per Box'),
    ('Per Piece','Per Piece '),
    ('1 Litre','Per Litre'),
)
AVAILABILITY_CHOICES = (
    ('In Stock','In Stock'),
    ('Stock Out','Stock Out'),
)

class Product(models.Model):
    title = models.CharField(max_length=75)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    color = models.CharField(choices=COLOR_CHOICES, max_length=8, blank=True, null=True)
    size = models.CharField(choices=POPULAR_SIZE_CHOICHES, max_length=8, blank=True, null=True)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    discription = models.TextField()
    information = models.TextField()
    reviews = models.TextField(blank=True, null=True)
    p_image = models.ImageField(upload_to='Product_Image')
    p_image1 = models.ImageField(upload_to='Product_Image1', null=True,blank=False)
    p_image2 = models.ImageField(upload_to='Product_Image2', null=True,blank=False)
    p_image3 = models.ImageField(upload_to='Product_Image3', null=True,blank=False)
    p_image4 = models.ImageField(upload_to='Product_Image4', null=True,blank=False)
    availability = models.CharField(choices=AVAILABILITY_CHOICES, max_length=20)
    shipping = models.CharField(max_length=100)
    weight = models.CharField(choices=ITEM_PER_CHOICES, max_length=15)
    sale_off_discount_parcent = models.FloatField(blank=True, null=True)
    latest_products = models.BooleanField(default=False) 
    
    
    def __str__(self):
        return str(self.id)
    
    
    
# Cart
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
       
    def __str__(self):
        return str(self.id)
    
    @property
    def Subtotal(self):
        return self.quantity * self.product.discount_price
    
    
# Wishlist
class Wishlist(models.Model):
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)
    

    
# Newsletter 
class Newsletter(models.Model):
    email = models.EmailField(max_length=50)
    


# Orders 
STATUS_CHOICE = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the Way', 'On the Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customar = models.ForeignKey(Customar, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=70, choices=STATUS_CHOICE, default='Pending')


    @property
    def total(self):
        return self.quantity * self.product.discount_price
    
# Carousel Silder
class Carousel_slider(models.Model):
    sub_title = models.CharField(max_length=100)
    titie = models.CharField(max_length=100)
    discription = models.CharField(max_length=150)
    image = models.ImageField(upload_to='carousel', null=True,blank=False)
    
    def __str__(self):
        return str(self.id)
    
# Contact 
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=1500)
    
    def __str__(self):
        return str(self.id)