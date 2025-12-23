from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import datetime
# Create your views here.
def home(request):
    return render(request,'carousel.html')


def About(request):
    return render(request, 'about.html')


def Contact(request):
    return render(request, 'contact.html')


def Signup(request):
    error = False
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        u = request.POST['uname']
        p = request.POST['pwd']
        e = request.POST['email']
        con = request.POST['mobile']
        c = request.POST['city']
        d = request.POST['date']
        s = request.POST['state']
        co = request.POST['country']
        pin = request.POST['pincode']
        image = request.FILES['image']
        user = User.objects.create_user(username=u, email=e, password=p, first_name=f, last_name=l)
        UserProfile.objects.create(user=user, mobile=con,city=c,state=s,dob=d,country=co,pincode=pin,image=image)
        error = True
    d = {'error': error}
    return render(request, 'signup.html', d)


def Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                messages.success(request,'Admin Login Successfully')
                return redirect('/admin_home/')
            elif user:
                login(request, user)
                messages.success(request,'Login Successfully')
                return redirect('/user_home/')
            else:
                error = "not"
        except:
            error = "not"
    d = {'error': error}
    return render(request, 'login.html', d)
def admin_home(request):
    return render(request,'admin_home.html')

def user_home(request):
    return render(request,'user_home.html')
def Logout(request):
    logout(request)
    return redirect('home')


def View_user(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    pro = UserProfile.objects.all()
    d = {'user': pro}
    return render(request, 'view_user.html', d)


def Add_Flight(request):
    if not request.user.is_authenticated:
        return redirect('login')
    # cat = Category.objects.all()
    error = False
    if request.method == "POST":
        company_name = request.POST['company_name']
        flight_name = request.POST['flight_name']
        airline_number = request.POST['airline_number']
        from_city = request.POST['from_city']
        from_city_arrival = request.POST['from_city_arrival']
        from_city_departure = request.POST['from_city_departure']
        to_city_arrival = request.POST['to_city_arrival']
        to_city_departure = request.POST['to_city_departure']
        to_city = request.POST['to_city']
        days = request.POST['days']
        fare_economy = request.POST['fare_economy']
        number_of_seat_e = request.POST['number_of_seat_e']
        number_of_seat_b = request.POST['number_of_seat_b']
        fare_business = request.POST['fare_business']
        airport_name = request.POST['airport_name']
        image = request.FILES['image']
        Airline.objects.create(company_name=company_name, image=image, fare_business=fare_business,
                               number_of_seat_b=number_of_seat_b, number_of_seat_e=number_of_seat_e,
                               fare_economy=fare_economy, days=days, to_city=to_city, to_city_departure=to_city_departure,
                                to_city_arrival=to_city_arrival, from_city_departure=from_city_departure, from_city_arrival=from_city_arrival,
                                from_city=from_city,airline_number=airline_number, flight_name=flight_name,airport_name=airport_name)
        messages.success(request, 'Flight Add Successfully')
        return redirect('view_flight')
    d ={'error':error,'city_choices':CITY_CHOICE}
    return render(request, 'add_flight.html', d)

def Edit_Flight(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    # cat = Category.objects.all()
    error = False
    flight=Airline.objects.get(id=pid)
    if request.method == "POST":
        company_name = request.POST['company_name']
        flight_name = request.POST['flight_name']
        airline_number = request.POST['airline_number']
        from_city = request.POST['from_city']
        from_city_arrival = request.POST['from_city_arrival']
        from_city_departure = request.POST['from_city_departure']
        to_city_arrival = request.POST['to_city_arrival']
        to_city_departure = request.POST['to_city_departure']
        to_city = request.POST['to_city']
        days = request.POST['days']
        fare_economy = request.POST['fare_economy']
        number_of_seat_e = request.POST['number_of_seat_e']
        number_of_seat_b = request.POST['number_of_seat_b']
        fare_business = request.POST['fare_business']
        try:
            i1= request.FILES['image']
            flight.image=i1
            flight.save()
        except:
            pass
        flight.company_name=company_name
        flight.fare_business=fare_business
        flight.number_of_seat_b=number_of_seat_b
        flight.number_of_seat_e=number_of_seat_e
        flight.fare_economy=fare_economy
        flight.days=days
        flight.to_city=to_city
        flight.to_city_departure=to_city_departure
        flight.to_city_arrival=to_city_arrival
        flight.from_city_departure=from_city_departure
        flight.from_city_arrival=from_city_arrival
        flight.from_city=from_city
        flight.airline_number=airline_number
        flight.flight_name=flight_name
        flight.save()
        messages.success(request, 'Edit Detail Successfully')
        return redirect('view_flight_detail',flight.id)
    d ={'error': error,'flight':flight,'city_choices':CITY_CHOICE}
    return render(request, 'edit_flight.html', d)
def view_flight(request):
    airline = Airline.objects.all()
    d = {'data':airline}
    return render(request, 'view_flight.html', d)
def delete_flight(request,pid):
    airline = Airline.objects.get(id=pid)
    airline.delete()
    return redirect('view_flight')
def View_flight_detail(request, pid):
    air = Airline.objects.get(id=pid)
    d = {'air': air}
    return render(request, 'view_flight_detail.html', d)
def All_flight(request):
    airline = Airline.objects.all()
    d = {'airline':airline}
    return render(request, 'all_flight.html', d)


def Admin_View_Booking(request):
    if not request.user.is_authenticated:
        return redirect('login')
    book = Booking.objects.all()
    d = {'book': book}
    return render(request, 'admin_viewBokking.html', d)


def View_feedback(request):
    if not request.user.is_authenticated:
        return redirect('login_admin')
    feed = Send_Feedback.objects.all()
    d = {'feed': feed}
    return render(request, 'view_feedback.html', d)


def View_booking_user(request):
    if not request.user.is_authenticated:
        return redirect('login')
    book = Booking.objects.filter(user=request.user)
    d = {'book': book}
    return render(request, 'mybooking.html', d)

def search_flight(request):
    data=''
    if request.method=="POST":
        from_city=request.POST['from_city']
        to_city=request.POST['to_city']
        data=Airline.objects.filter(from_city=from_city,to_city=to_city)
    d={'data':data,'city_choices':CITY_CHOICE}
    return render(request,'search_flight.html',d)

def Change_Password(request):
    if request.method=="POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        d = request.POST['pwd3']
        if c == d:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(d)
            u.save()
            messages.success(request,'Password Changed Successfully')
    return render(request,'change_password.html')



def Book_detail(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    error = False
    fixed_stage = 0
    data2 = Airline.objects.get(id=pid)
    user = UserProfile.objects.get(user=request.user)
    pro = Booking_Passenger.objects.filter(user=request.user)
    book = Booking.objects.filter(user=request.user)
    if request.method=="POST":
        m= request.POST["mobile"]
        c = request.POST["city"]
        pin= request.POST["pincode"]
        country= request.POST["country"]
        #d= request.POST["date"]
        total_price= request.POST["total_price"]
        booking  = Booking.objects.create(airline=data2,user=request.user,total_price=total_price,mobile=m,city=c,pincode=pin,country=country,date=datetime.date.today())
        total = request.POST.get('total_stage')
        for st in range(1, int(total)+1 ):
            fname = request.POST["fname" + str(st)]
            lname = request.POST["lname" + str(st)]
            age = request.POST["age" + str(st)]
            gender = request.POST["gender" + str(st)]
            fare = request.POST["fare" + str(st)]
            passenger = Booking_Passenger.objects.create(user=request.user,booking=booking,last_name=lname,first_name=fname,gender=gender,age=age,total_price=fare)
        messages.success(request, 'Booking Successfully')
        return redirect('payment')
    d = {'data2':data2,'pro':pro,'book':book,'error':error,'pid':pid,'fixed_stage':fixed_stage}
    return render(request,'book_detail.html',d)

def payment(request):
    return render(request,'payment.html')

def mybooking(request):
    if not request.user.is_authenticated:
        return redirect('login')
    pro = Booking_Passenger.objects.filter(user=request.user)
    book = Booking.objects.filter(user=request.user)
    d={'book':book,'pro':pro}
    return render(request,'mybooking.html',d)

def booking_detail(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    book = Booking.objects.get(booking_id=pid)
    pro=Booking_Passenger.objects.filter(booking=book)
    d={'book':book,'pro':pro}
    return render(request,'booking_detail.html',d)

def delete_booking(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    book = Booking.objects.get(booking_id=pid)
    book.delete()
    return redirect('mybooking')

def view_profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    data=UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        f = request.POST['first_name']
        l = request.POST['last_name']
        e = request.POST['email']
        con = request.POST['mobile']
        c = request.POST['city']
        s = request.POST['state']
        co = request.POST['country']
        pin = request.POST['pincode']
        data.user.first_name=f
        data.user.last_name=l
        data.user.email=e
        data.mobile=con
        data.city=c
        data.state=s
        data.country=co
        data.pincode=pin
        try:
            i1= request.FILES['image']
            data.image=i1
            data.save()
        except:
            pass
        data.save()
        messages.success(request,'Edit Detail Successfuly')
    d={'data':data}

    return render(request,'view_profile.html',d)

def feedback(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error=False
    if request.method == 'POST':
        m = request.POST['msg']
        u = request.POST['username']
        Send_Feedback.objects.create(user=request.user,username=u,msg=m,date=datetime.date.today())
        error=True
    d={'error':error}
    return render(request,'feedback.html',d)

def delete_user(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    data=User.objects.get(id=pid)
    data.delete()
    return redirect('view_user')

def search_booking_byadmin(request):
    if not request.user.is_staff:
        return redirect('login')
    data1=''
    d1=''
    d2=''
    if request.method == 'POST':
        d1= request.POST['from_date']
        d2 = request.POST['to_date']
        i1 = datetime.datetime.fromisoformat(d1)
        i2 = datetime.datetime.fromisoformat(d2)
        data1=Booking.objects.filter(date__gte=datetime.date(i1.year,i1.month,i1.day),date__lte=datetime.date(i2.year,i2.month,i2.day))
    d={'data':data1,'d1':d1,'d2':d2}
    return render(request,'search_booking.html',d)
def search_booking_by_id(request):
    if not request.user.is_staff:
        return redirect('login')
    data1=''
    d1=''
    if request.method == 'POST':
        try:
            d1= request.POST['booking_id']
            data1=Booking.objects.filter(booking_id=d1)
        except:
            pass
    d={'data':data1,'d1':d1}
    return render(request,'search_booking_by_id.html',d)
def search_flight_by_number(request):
    if not request.user.is_staff:
        return redirect('login')
    data1=''
    d1=''
    if request.method == 'POST':
        try:
            d1= request.POST['number']
            data1=Airline.objects.filter(airline_number=d1)
        except:
            pass
    d={'data':data1,'d1':d1}
    return render(request,'search_flight_by_number.html',d)
def admin_delete_booking(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    book = Booking.objects.get(booking_id=pid)
    book.delete()
    return redirect('admin_view_booking')
