from django.shortcuts import render

def index(request):
	context={
		'page_title':'EMPLOYEE DATABASE TRIAL',
		'card_title':'PT. INDEXIM COALINDO',
	}
	return render(request,'index.html',context)