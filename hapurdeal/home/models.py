from django.db import models
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from django.contrib.auth.models import User
from autoslug import AutoSlugField

# Create your models here.


class WebsiteInfo(models.Model):
	sno = models.AutoField(primary_key=True)
	title = models.CharField(max_length=255,null=True,blank=True)
	logo = models.ImageField(upload_to="images",null=True,blank=True)
	favilogo = models.ImageField(upload_to="images",null=True,blank=True)
	bgimg = models.ImageField(upload_to="images",null=True,blank=True)
	heading = models.CharField(max_length=255,null=True,blank=True)
	subheading = models.CharField(max_length=255,null=True,blank=True)
	des = models.TextField(null=True,blank=True)
	fb = models.CharField(max_length=255,null=True,blank=True)
	twitter = models.CharField(max_length=255,null=True,blank=True)
	linkedin =  models.CharField(max_length=255,null=True,blank=True)
	youtube = models.CharField(max_length=255,null=True,blank=True)
	instagram = models.CharField(max_length=255,null=True,blank=True)
	keyword = models.TextField(null=True,blank=True)
	discription = RichTextField(null=True,blank=True)


	def __str__(self):
		return self.heading

class ContactInfo(models.Model):
	sno = models.AutoField(primary_key=True)
	number = models.CharField(max_length=255,null=True,blank=True)
	email = models.CharField(max_length=255,null=True,blank=True)
	address1 = models.TextField(null=True,blank=True)
	address2 = models.TextField(null=True,blank=True)
	googlemap = models.TextField(null=True,blank=True)

	def __str__(self):
		return self.number


class ContactMessage(models.Model):
	STATUS = (
		("Answered","Answered"),
		("Not Answered","Not Answered")
		)
	sno = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255,null=True,blank=True)
	email = models.CharField(max_length=255,null=True,blank=True)
	number = models.CharField(max_length=255,null=True,blank=True)
	message = RichTextField(null=True,blank=True)
	date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	status = models.CharField(max_length=255,choices=STATUS,default="Not Answered",null=True,blank=True)

	def __str__(self):
		return self.name



class Profile(models.Model):
	sno = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
	business = models.CharField(max_length=255,null=True,blank=True)
	area_locality = models.CharField(max_length=255,null=True,blank=True)
	village_town =  models.CharField(max_length=255,null=True,blank=True)
	district = models.CharField(max_length=255,null=True,blank=True)
	state = models.CharField(max_length=255,null=True,blank=True)
	pincode = models.CharField(max_length=255,null=True,blank=True)
	about = RichTextField(null=True,blank=True)
	profile_photo = models.ImageField(upload_to="images",null=True,blank=True)

	def __str__(self):
		return self.business



class Notification(models.Model):
	sno = models.AutoField(primary_key=True)
	user =  models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
	subject = models.CharField(max_length=255,null=True,blank=True)
	msg = RichTextField()
	date = models.DateTimeField(auto_now_add=True,null=True,blank=True)

	def __str__(self):
		return self.subject



# ----------------------------------------------------------------------------------------

class Seller(models.Model):
	STATUS_PLAN = (
		("Poor","Poor"),
		("Fair","Fair"),
		("Good","Good"),
		("Excellent","Excellent"),
	)

	SOLD_PLAN = (
		("Buy","Buy"),
		("Sold","Sold"),
	)

	sno = models.AutoField(primary_key=True)
	user =  models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
	seller_name = models.CharField(max_length=255,null=True,blank=True)
	seller_mobile = models.CharField(max_length=255,null=True,blank=True)
	image = models.ImageField(upload_to="images",null=True,blank=True)
	make_com = models.CharField(max_length=255,null=True,blank=True)
	model = models.CharField(max_length=255,null=True,blank=True)
	year = models.CharField(max_length=255,null=True,blank=True)
	car_condition  = models.CharField(max_length=255,null=True,blank=True,choices=STATUS_PLAN,default="POOR")
	asking_price = models.CharField(max_length=255,null=True,blank=True)
	is_sold = models.CharField(max_length=255,null=True,blank=True,choices=SOLD_PLAN,default="Buy")


	def __str__(self):
		return self.seller_name


class Order(models.Model):
	sno = models.AutoField(primary_key=True)
	sale =  models.ForeignKey(Seller,on_delete=models.CASCADE,null=True,blank=True)
	buyer_name = models.CharField(max_length=255,null=True,blank=True)
	buyer_mobile = models.CharField(max_length=255,null=True,blank=True)


	def __str__(self):
		return self.buyer_name
