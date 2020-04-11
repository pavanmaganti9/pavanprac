from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	#return HttpResponse('Hello Pavan!')
	Months = ["Jan","Feb","Mar","April","May","June"]
	return render(request, 'index1.html', {'mnt' : Months})
