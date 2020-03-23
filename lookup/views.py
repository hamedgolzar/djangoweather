from django.shortcuts import render

# Create your views here.
def home(request):
	#
	import json
	import requests
	api_request=requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=E27A3300-B762-4B17-90E3-2CF609E8BE30")
	try:
		api=json.loads(api_request.content)


	except Exception as e:
		api="Error...."

	return render(request,'home.html',{'api':api})