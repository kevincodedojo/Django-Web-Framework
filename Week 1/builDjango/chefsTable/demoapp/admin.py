from django.contrib import admin
from .models import Drinks, DrinksCategory, Booking, Employee

# Register your models here.
admin.site.register(Drinks)
admin.site.register(DrinksCategory)
admin.site.register(Booking)
admin.site.register(Employee)