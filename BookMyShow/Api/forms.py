from django.forms import ModelForm
from .models import BookSeat

class BookSeatForm(ModelForm):
    class Meta:
        model = BookSeat
        fields = ['seat','total_amount']