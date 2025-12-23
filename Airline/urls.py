"""Airline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from air.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('signup',Signup,name="signup"),
	path('about/',About,name='about'),
	path('contact/',Contact,name='contact'),
    path('login',Login,name="login"),
    path('logout/',Logout,name="logout"),
    path('view_user/',View_user,name="view_user"),
    path('admin_home/',admin_home,name="admin_home"),
    path('user_home/',user_home,name="user_home"),
    path('search_flight/',search_flight,name="search_flight"),
    path('Change_Password/',Change_Password,name="Change_Password"),
    path('add_flight/',Add_Flight,name="add_flight"),
    path('all_flight/',All_flight,name="all_flight"),
    path('view_flight/',view_flight,name="view_flight"),
    path('view_feedback', View_feedback, name='view_feedback'),
    path('edit_Flight(<int:pid>)/', Edit_Flight, name='edit_flight'),
    path('delete_flight(<int:pid>)/', delete_flight, name='delete_flight'),
    path('view_flight_detail(<int:pid>)/', View_flight_detail, name='view_flight_detail'),
    path('view_booking_user(<int:pid>)/', View_booking_user, name='view_booking_user'),
    path('admin_view_booking/', Admin_View_Booking, name='admin_view_booking'),
    path('payment/', payment, name='payment'),
    path('mybooking/', mybooking, name='mybooking'),
    path('view_profile/', view_profile, name='view_profile'),
    path('feedback/', feedback, name='feedback'),
    path('search_booking_byadmin/', search_booking_byadmin, name='search_booking_byadmin'),
    path('search_booking_by_id/', search_booking_by_id, name='search_booking_by_id'),
    path('search_flight_by_number/', search_flight_by_number, name='search_flight_by_number'),
    path('book_detail/(<int:pid>)/',Book_detail,name="book_detail"),
    path('booking_detail/(<str:pid>)/',booking_detail,name="booking_detail"),
    path('delete_booking/(<str:pid>)/',delete_booking,name="delete_booking"),
    path('admin_delete_booking/(<str:pid>)/',admin_delete_booking,name="admin_delete_booking"),
    path('delete_user/(<int:pid>)/',delete_user,name="delete_user"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
