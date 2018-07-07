from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
import json
import requests



def flight(request) :
	if request.user.is_authenticated():
		template = 'flight.html'
		return render(request, template)
	else :
		return redirect('login')
	
def detail(request) :

		if request.method == 'POST' :
			
			origin = request.POST['ori']
			destination = request.POST['des']
			date = request.POST['date']
			adultcount = request.POST['count']
			
			api_key = "AIzaSyAF1M_y5ABZdZRWKTkhMjMJuq5Ysz6swm8"
			url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key=" + api_key
			headers = {'content-type': 'application/json'}

			params = {
			  "request": {
				"slice": [
				  {
					"origin": origin,
					"destination": destination,
					"date": date
				  }
				],
				"passengers": {
				  "adultCount": adultcount
				},
				"solutions": 20,
				"refundable": False
			  }
			}

			response = requests.post(url, data=json.dumps(params), headers=headers)
			data = response.json()
			print (data)
			detail = [];
			for i in range (20) :
				price = data['trips']['tripOption'][i]['saleTotal']
				airline = data['trips']['tripOption'][i]['slice'][0]['segment'][0]['flight']['carrier']
				flight_no = data['trips']['tripOption'][i]['slice'][0]['segment'][0]['flight']['number']
				forigin = data['trips']['tripOption'][i]['slice'][0]['segment'][0]['leg'][0]['origin']
				#forigin1 = data['trips']['tripOption'][i]['slice'][0]['segment'][0]['leg'][1]['origin']
				dep_time = data['trips']['tripOption'][i]['slice'][0]['segment'][0]['leg'][0]['departureTime']
				fdestination = data['trips']['tripOption'][i]['slice'][0]['segment'][0]['leg'][0]['destination']
				#fdestination1 = data['trips']['tripOption'][i]['slice'][0]['segment'][0]['leg'][1]['destination']
				ari_time = data['trips']['tripOption'][3]['slice'][0]['segment'][0]['leg'][0]['arrivalTime'] 
				duration = data['trips']['tripOption'][3]['slice'][0]['segment'][0]['leg'][0]['duration'] 		
				#detail += [[price,airline,flight_no,forigin,dep_time,fdestination,ari_time]]
				
				detail +=[ {
				
							
								'price' : price,
								'airline' : airline,
								'flight_no' : flight_no,
								'forigin' : forigin,
								'dep_time' : dep_time,
								'fdestination' : fdestination,
								'ari_time' : ari_time,
								'duration' : duration,
						
							
				
						  }	
				]
				
				data1=json.dumps(detail)	
			return HttpResponse(data1)
				
				
			
