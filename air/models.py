from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
CITY_CHOICE=(('Bhopal','Bhopal'),('Delhi','Delhi'),('Bengaluru','Bengaluru'),('Pune','Pune'),('Mumbai','Mumbai'),('Patna','Patna'))
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    mobile = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    dob = models.DateField(null=True)
    country = models.CharField(max_length=100,null=True,blank=True)
    pincode = models.CharField(max_length=100,null=True,blank=True)
    image = models.FileField(null=True)

    def __str__(self):
        return self.user.username

class Airline(models.Model):
    company_name = models.CharField(max_length=100,null=True)
    flight_name = models.CharField(max_length=100,null=True)
    airport_name = models.CharField(max_length=100,null=True)
    airline_number = models.CharField(max_length=100,null=True)
    from_city = models.CharField(max_length=100,null=True,choices=CITY_CHOICE)
    from_city_arrival = models.CharField(max_length=100,null=True)
    from_city_departure = models.CharField(max_length=100,null=True)
    to_city_arrival = models.CharField(max_length=100,null=True)
    to_city_departure = models.CharField(max_length=100,null=True)
    to_city = models.CharField(max_length=100,null=True,choices=CITY_CHOICE)
    days = models.TextField(null=True)
    fare_economy =models.CharField(max_length=100,null=True)
    number_of_seat_e =models.CharField(max_length=100,null=True)
    number_of_seat_b =models.CharField(max_length=100,null=True)
    fare_business =models.CharField(max_length=100,null=True)
    image = models.FileField(null=True)
    def __str__(self):
        return self.company_name+"-"+self.flight_name+"-"+self.airline_number


class Booking(models.Model):
    user = models.ForeignKey(User,related_name='+', on_delete=models.CASCADE, null=True)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, null=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    total_price = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return  self.user.username + "-" + str(self.booking_id)

class Booking_Passenger(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    booking = models.ForeignKey(Booking,related_name='+',on_delete=models.CASCADE, null=True,)
    booking_id_pass = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)
    age = models.CharField(max_length=100, null=True, blank=True)
    total_price = models.CharField(max_length=100, null=True, blank=True)

    # def __str__(self):
    #     return self.first_name + "-" + self.user.username
class Send_Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    msg = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(max_length=100, null=True, blank=True)

    def __str__(self):
        return  self.user.username





