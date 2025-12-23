from django.contrib import admin
from air.models import *

# Register your models here.
admin.site.register(Airline)
admin.site.register(Booking)
admin.site.register(Booking_Passenger)
admin.site.register(UserProfile)
admin.site.register(Send_Feedback)

