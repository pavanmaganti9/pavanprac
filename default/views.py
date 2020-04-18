from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SmsForm
import requests
from django.contrib import messages

# Create your views here.
def index(request):
	#return HttpResponse('Hello Pavan!')
    Months = ["Jan","Feb","Mar","April","May","June"]
    return render(request, 'index1.html', {'mnt' : Months})

def sms(request):
	if request.method == 'POST':
		form = SmsForm(data = request.POST)
		if form.is_valid:
			URL = 'https://www.sms4india.com/api/v1/sendCampaign'
			sms = form.save()
			mobile = request.POST['mobile']
			message = request.POST['message']
			response = sendPostRequest(URL, 'TUW9PPYRFKTQYNZL2OEF3QUSNYOPT1CJ', 'XEHLP3B48UM6TEZL', 'stage', mobile, 'pavanmaganti9@gmail.com', message )
			print(response.text)
			messages.success(request, 'Form Submitted Successfully!')
			return redirect('sms')
	else:
		form = SmsForm()
	return render(request, 'sms.html', {'form': form})

def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
	req_params = {
  					'apikey':apiKey,
  					'secret':secretKey,
  					'usetype':useType,
  					'phone': phoneNo,
  					'message':textMessage,
  					'senderid':senderId
  	}
	return requests.post(reqUrl, req_params)
