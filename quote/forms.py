from django.forms import ModelForm
from quote.models import Quote
from django.forms.extras.widgets import SelectDateWidget
import datetime
from django.utils import timezone
from datetime import date

class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        
        widgets = {
            'DOB': SelectDateWidget(years=range(1950, date.today().year+1)),
        }