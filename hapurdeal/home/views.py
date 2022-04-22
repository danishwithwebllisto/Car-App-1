from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login as auth_login , logout as auth_logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def base():
	lenuser = len(User.objects.all())
	lenpost = len(Seller.objects.all())
	return lenuser,lenpost


def home(request):
	web = WebsiteInfo.objects.all()[::-1]
	con = ContactInfo.objects.all()[::-1]
	post = Seller.objects.all()[::-1]
	lenuser ,lenpost = base()

	if request.user.is_authenticated:
		try:
			sno = request.GET.get('sale')
			seller = Seller.objects.filter(sno=sno).first()
			seller.is_sold = "Buy"
			seller.save()

			messages.success(request,"Sucessfully Marked Buy")
			return redirect('/dashboard')
		except:
			pass

		context = {'web':web,'con':con,'allPost':post,'lenus':lenuser,'lenpo':lenpost,}
		return render(request,'home/index.html',context)


	else:	
		context = {'web':web,'con':con,'allPost':post,'lenus':lenuser,'lenpo':lenpost,}
		return render(request,'home/index.html',context)


def contact(request):
	web = WebsiteInfo.objects.all()[::-1]
	con = ContactInfo.objects.all()[::-1]
	lenuser ,lenpost = base()

	if request.method == "POST":
		name = request.POST['name']
		email = request.POST['email']
		number = request.POST['number']
		message = request.POST['message']
		
		if len(number) != 10:
			messages.error(request,"Mobile Number Should Be 10 Digit")
			return redirect('/contact')

		else:
			con = ContactMessage(name=name,email=email,number=number,message=message)
			con.save()
			messages.success(request,"Your Message Has Been Sucessfully Submitted.")
			return redirect('/contact')


	context = {'web':web,'con':con,'lenus':lenuser,'lenpo':lenpost}
	return render(request,'home/contact.html',context)

def signup(request):
	web = WebsiteInfo.objects.all()[::-1]
	con = ContactInfo.objects.all()[::-1]

	if request.method == "POST":
		first_name = request.POST['fname']
		last_name = request.POST['lname']
		number = request.POST['username']
		email_address = request.POST['email']
		password = request.POST['password']
		cpassword = request.POST['confirmpassword']


		if len(number) != 10:
			messages.error(request,"Mobile Number Should Be 10 Digit")
			return redirect('/signup')

		elif password != cpassword:
			messages.error(request,"Confirm Password Should Be Match")
			redirect('/signup')

		else:
			user = User.objects.filter(username=number)
			email = User.objects.filter(email=email_address)
			if len(user) != 0:
				messages.error(request,"Your Mobile is Already Exists")
			elif len(email) != 0:
				messages.error(request,"Your Email is Already Exists")
			else:
				user_register = User.objects.create_user(number,email_address,cpassword)
				user_register.first_name = first_name
				user_register.last_name = last_name
				user_register.save()
				messages.success(request,"Your Account Sucessfully Created")
				return redirect('/login')

	context = {'web':web,'con':con}
	return render(request,'home/user-form.html',context)

def login(request):
	if request.user.is_authenticated:
		return redirect('/')

	web = WebsiteInfo.objects.all()[::-1]
	con = ContactInfo.objects.all()[::-1]

	if request.method == "POST":
		number = request.POST['number']
		password = request.POST['password']

		user = authenticate(request,username=number,password=password)

		if user is not None:
			auth_login(request,user)
			messages.success(request,"Login Sucessfully")
			return redirect('/dashboard')
		else:
			messages.error(request,"Your Username are Password is incorrect.")
			return redirect('/login')

	context = {'web':web,'con':con}
	return render(request,'home/user-form.html',context)

def logout(request):
	auth_logout(request)
	return redirect('/')


def dashboard(request):
	if request.user.is_authenticated:
		web = WebsiteInfo.objects.all()[::-1]
		con = ContactInfo.objects.all()[::-1]
		pro = Profile.objects.filter(user=request.user)
		user = User.objects.filter(username=request.user)
		lenuser ,lenpost = base()


		context = {'web':web,'con':con,'profile':pro,'user_details':user,'lenus':lenuser,'lenpo':lenpost}
		return render(request,'home/dashboard.html',context)
	else:
		return redirect('/login')

def addpost(request):
	if request.user.is_authenticated:
		web = WebsiteInfo.objects.all()[::-1]
		con = ContactInfo.objects.all()[::-1]
		
		pro = Profile.objects.filter(user=request.user)
		user = User.objects.filter(username=request.user)

		if len(pro) == 0:
			messages.error(request,"Please Update Your Profile (*)")
			return redirect('/profile-setting')

		elif request.method == "POST":
			sname = request.POST['name']
			snumber = request.POST['number']
			image = request.FILES['photo']
			condition = request.POST['condition']
			make = request.POST['make']
			model = request.POST['model']
			year = request.POST['year']
			askp = request.POST['askp']

			if len(snumber) != 10:
				messages.error(request,"Mobile Number Should Be 10 Digit")
				return redirect('/add-post')

			elif condition == "select":
				messages.error(request,"Please Select a Car Condition")
				return redirect('/add-post')


			elif int(askp) < 1000 or int(askp) > 100000:
				messages.error(request,"Amount at minimum $1,000 and no more that 100,000")
				return redirect('/add-post')

			else:
				user = request.user
				seller = Seller(user=user,seller_name=sname,seller_mobile=snumber,image=image,make_com=make,model=model,year=year,car_condition=condition,asking_price=askp)
				seller.save()

				sel_id = Seller.objects.filter(user=user).values_list("sno",flat=True)[::-1]

				messages.success(request,f"Thank you For Publish Seller Post ID -  {sel_id[0]}")
				return redirect('/add-post')
				

		else:
			context = {'web':web,'con':con,'profile':pro,'user_details':user}
			return render(request,'home/ad-post.html',context)


	else:
		return redirect('/login')



def postdetails(request):
	adspost = Seller.objects.all()[::-1]
	page = request.GET.get('page', 1)
	year = request.GET.get('year')
	make = request.GET.get('make')
	
	if year:
		adspost = Seller.objects.filter(year=year)

	if make:
		adspost = Seller.objects.filter(make_com=make)


	paginator = Paginator(adspost,12)
	web = WebsiteInfo.objects.all()[::-1]
	con = ContactInfo.objects.all()[::-1]
	lenuser ,lenpost = base()

	try:
		fil = set(Seller.objects.all().values_list('year',flat=True))
		make = set(Seller.objects.all().values_list('make_com',flat=True))
	except:
		fil = []
		make = []


	try:
		adspost_pagi = paginator.page(page)
	except PageNotAnInteger:
		adspost_pagi = paginator.page(1)
	except EmptyPage:
		adspost_pagi = paginator.page(paginator.num_pages)

	if request.user.is_authenticated:
		
		pro = Profile.objects.filter(user=request.user)
		user = User.objects.filter(username=request.user)

		context = {'web':web,'con':con,'profile':pro,'user_details':user,'lenus':lenuser,'lenpo':lenpost,'adspost':adspost_pagi,'adspost_pagi':adspost_pagi,'fill':fil,'make':make}
		return render(request,'home/category-details.html',context)
	else:
		
		context = {'web':web,'con':con,'lenus':lenuser,'lenpo':lenpost,'adspost':adspost_pagi,'adspost_pagi':adspost_pagi,'fill':fil,'make':make}
		return render(request,'home/category-details.html',context)


def adspage(request,slug):
	web = WebsiteInfo.objects.all()[::-1]
	con = ContactInfo.objects.all()[::-1]

	if request.user.is_authenticated:
		pro = Profile.objects.filter(user=request.user)
		user = User.objects.filter(username=request.user)

		lenuser ,lanpost = base()
		print(slug)
		addpost = Seller.objects.filter(sno=slug).first()

		context = {'web':web,'con':con,'profile':pro,'user_details':user,'lenus':lenuser,'lenpo':lanpost,'post':addpost}
		return render(request,'home/ad-details-right.html',context)
	else:
		
		lenuser ,lenpost = base()
		addpost = Seller.objects.filter(sno=slug).first()

		context = {'web':web,'con':con,'lenus':lenuser,'lenpo':lenpost,'post':addpost}
		return render(request,'home/ad-details-right.html',context)


def profilesetting(request):
	if request.user.is_authenticated:
		web = WebsiteInfo.objects.all()[::-1]
		con = ContactInfo.objects.all()[::-1]
		pro = Profile.objects.filter(user=request.user)
		user = User.objects.filter(username=request.user)

		lenuser ,lenpost = base()


		if request.method == "POST":
			user = request.user
			business = request.POST['business']
			area_locality  = request.POST['area']
			village_town  = request.POST['village']
			district = request.POST['district']
			state = request.POST['state']
			pincode = request.POST['pincode']
			about = request.POST['about']
			profile_photo = request.FILES['photo']


			if len(pincode) != 6:
				messages.error(request,"Pincode Should be 6 Digit")
				return redirect('/profile-setting')
			else:
				ex_user = Profile.objects.filter(user=user)

				if len(ex_user) == 0:
					profile = Profile(user=user,business=business,area_locality=area_locality,village_town = village_town, district=district,state = state , pincode = pincode, profile_photo=profile_photo,about=about)
					profile.save()
					messages.success(request,"Your Profile Has Been Updated")
					return redirect('/profile-setting')

					
				else:
					sno = ex_user.values_list('sno', flat=True)
					sno = list(sno)

					profile = Profile(sno = int(sno[0]) ,user=user,business=business,area_locality=area_locality,village_town = village_town, district=district,state = state , pincode = pincode, profile_photo=profile_photo,about=about)
					profile.save()
					messages.success(request,"Your Profile Has Been Updated")
					return redirect('/profile-setting')
		


		context = {'web':web,'con':con,'profile':pro,'user_details':user,'lenus':lenuser,'lenpo':lenpost,}
		return render(request,'home/setting.html',context)
	else:
		return redirect('/login')


def myads(request):
	if request.user.is_authenticated:
		web = WebsiteInfo.objects.all()[::-1]
		con = ContactInfo.objects.all()[::-1]

		pro = Profile.objects.filter(user=request.user)
		user = User.objects.filter(username=request.user)
		userpost = Seller.objects.filter(user=request.user)

		paginator = Paginator(userpost,12)
		page = request.GET.get('page', 1)
		lanuser ,lanpost = base()
	

		try:
			users = paginator.page(page)
		except PageNotAnInteger:
			users = paginator.page(1)
		except EmptyPage:
			users = paginator.page(paginator.num_pages)

		context = {'web':web,'con':con,'profile':pro,'user_details':user,'userpost':users,'lenus':lanuser,'lenpo':lanpost}
		return render(request,'home/my-ads.html',context)

	else:
		return redirect('/login')



def buy(request):
	if request.method == "POST":
		name = request.POST['name']
		mobile = request.POST['mobile']
		sno = request.POST['sno']

		if len(mobile) != 10:
			messages.error(request,"Mobile Number Should Be 10 Digit")
			return redirect('/')

		else:
			obj = Seller.objects.get(sno=sno)
			con = Order(sale=obj,buyer_name=name,buyer_mobile=mobile)
			con.save()
			obj.is_sold = "Sold"

			try:
				make_com = obj.make_com
				model = obj.model
				year = obj.year
				car_condition = obj.car_condition
				price = obj.asking_price
				party_name = name
				party_mobile = mobile
				email = obj.user.email

				commission = int(price) * 5 / 100
				net_amount =  int(price) - commission

				obj.save()
				send_mail(
					subject=f'Check Order From - {party_name} And {party_mobile}',
					message=f'Car Model - {model} And Year is {year} And Make Com - \
					{make_com} And Car Condition - {car_condition} And Price is - {price} And Commission - {commission} And Net Amount - {net_amount}',
					from_email=settings.EMAIL_HOST_USER,
					recipient_list=email,)
			except:
				pass

			messages.success(request,"Your Order Sucessfully Submitted.")
			return redirect('/ads-details')
	else:
		redirect('/ads-details')






