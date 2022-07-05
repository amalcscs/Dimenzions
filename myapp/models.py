from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Admin_register(models.Model):
    reg_id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=200,default="")
    username = models.CharField(max_length=100)
    joining_date= models.DateTimeField(null=True,blank=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50) 
    designation = models.CharField(max_length=100,default="")
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    
    
class categories(models.Model):
    cat_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    category_logo = models.ImageField(default = "default.png", upload_to="images")
    sub_category1 = models.CharField(max_length=255)
    sub_category2 =  models.CharField(max_length=255)
    sub_category3 = models.EmailField(max_length=255)
    sub_category4 = models.CharField(max_length=255)
    sub_category5 = models.CharField(max_length=255)
    
    

class items(models.Model):
	modelname = models.CharField(max_length=255,null=True)
	description = models.CharField(max_length=255)
	gib = models.FileField( upload_to="images/",null=True,blank=True)
	price = models.CharField(max_length=255)
	types = models.CharField(max_length=255)
	format = models.CharField(max_length=255)
	modeltype = models.CharField(max_length=255)
	category = models.ForeignKey(categories, on_delete=models.CASCADE, null=True,default='')
	fbx = models.ImageField(default="default.png", upload_to="images")
	
	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url


class payment(models.Model):
    modelname = models.ForeignKey(items,on_delete=models.DO_NOTHING , related_name='pay_model',null=True,blank=True)
    price = models.ForeignKey(items , on_delete=models.DO_NOTHING , related_name='pay_price',null=True,blank=True)
    clientname = models.CharField(max_length=225 ,null=True)
    date=models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True) 


class Customer(models.Model):
	user = models.OneToOneField(Admin_register, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name




class Order(models.Model):
	customer = models.ForeignKey(Admin_register, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
		
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	product = models.ForeignKey(items, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Admin_register, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address

class Product(models.Model):
    product_name=models.CharField(max_length=40)
    product_image= models.ImageField(upload_to='images/',null=True,blank=True)
    price = models.PositiveIntegerField()
    description=models.CharField(max_length=40)
    category = models.ForeignKey(categories, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.product_name