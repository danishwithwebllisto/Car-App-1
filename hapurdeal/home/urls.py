from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from . import views



urlpatterns = [
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('contact',views.contact,name="contact"),
    path('signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('logout',views.logout,name="logout"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('add-post',views.addpost,name="addpost"),
    path('ads-details',views.postdetails,name="postdetails"),
    path('profile-setting',views.profilesetting,name="profilesetting"),
    path('myads',views.myads,name="myads"),
    path('buy',views.buy,name="buy"),
    path('<str:slug>/',views.adspage,name="adspage")

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
