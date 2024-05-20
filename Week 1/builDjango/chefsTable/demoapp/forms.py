from django import forms
from .models import Drinks, DrinksCategory, Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'guest_count', 'reservation_time', 'comments']