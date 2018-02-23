from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
# from django.forms.extras.widgets import SelectDateWidget
from django.contrib.admin import widgets

from .models import Person,Rent,Car,User

class PersonForm(ModelForm):
	class Meta:
		model =  Person
		exclude=[]

		# widgets = {
		# 	'dob': forms.DateInput(
		# 		attrs={
		# 		'type': 'date', 
		# 		'value': datetime.datetime.now().strftime("%Y-%m-%d")
		# 		}, format="%Y-%m-%d"
		# 	),
		# }
		
	def __init__(self, *args, **kwargs):
		super(PersonForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))

class RentForm(ModelForm):
	# user = forms.ModelChoiceField(queryset=User.objects.all())
	car = forms.ModelChoiceField(queryset=Car.objects.all(),required = True)
	start_datetime = forms.DateTimeField(help_text='Required. Format: YYYY-MM-DD HH:MM:SS',required = True)
	# stop_datetime = forms.DateTimeField(help_text='Required. Format: YYYY-MM-DD HH:MM:SS',required = True)
	fee = forms.DecimalField(help_text='Required. Format: 0.00',required = True)


	class Meta:
		model =  Rent 
		fields = ['car', 'start_datetime', 'fee' ]
		exclude=['user', 'stop_datetime']
		# field1 = forms.ModelChoiceField(queryset=Car, empty_label="(Nothing)")


		# widgets = {
		# 	'dob': forms.DateInput(
		# 		attrs={
		# 		'type': 'date', 
		# 		'value': datetime.datetime.now().strftime("%Y-%m-%d")
		# 		}, format="%Y-%m-%d"
		# 	),
		# }
		
	def __init__(self, *args, **kwargs):
		super(RentForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.help_text_inline = True
		self.helper.add_input(Submit('submit', 'Submit'))



