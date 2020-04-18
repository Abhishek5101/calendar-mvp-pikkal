from django import forms
from .models import Event


class DateInput(forms.DateInput):
	input_type = 'date'


class EventForm(forms.ModelForm):
	
	class Meta:
		model = Event
		event_date = forms.DateField(widget=DateInput)
		widgets = {'event_date': DateInput()}
		fields = '__all__'

