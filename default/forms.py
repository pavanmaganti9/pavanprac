from django import forms
from .models import sms

class SmsForm(forms.ModelForm):
	name = forms.CharField(max_length=30, required=True)
	mobile = forms.IntegerField(min_value=0, max_value=9999999999,required=True)
	message = forms.CharField(max_length=30, required=True)
	
	class Meta:
		model = sms
		fields = ('name', 'mobile')