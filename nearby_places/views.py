from django.shortcuts import render ,redirect
from django.http import HttpResponse
import urllib.request
from urllib.request import urlopen
from contextlib import closing
import json
import decimal
from nearby_places.models import explore
from django.template import loader

def Cafe(request):
	if request.user.is_authenticated():		
			url = 'http://freegeoip.net/json/'
			with closing(urlopen(url)) as response:
					location = json.loads(response.read())
					lng =  location['longitude']
					lat =  location['latitude']
			lat1 = decimal.Decimal(22.7167)+decimal.Decimal(0.007798)
			lng1 = decimal.Decimal(75.8333)+decimal.Decimal(0.044059)

			name = explore.objects.all()
			AUTH_KEY = 'AIzaSyAF1M_y5ABZdZRWKTkhMjMJuq5Ysz6swm8'
			LOCATION = str(lat1) + "," + str(lng1)
			RADIUS = 1000
			TYPES = 'cafe'
			MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
											   '?location=%s'
											   '&radius=%s'
											   '&types=%s'
											   '&key=%s') % (LOCATION, RADIUS, TYPES, AUTH_KEY)
			f = urllib.request.urlopen(MyUrl)
			json_string = f.read()
			f.close()
			location = json.loads(json_string)

			for r in location['results']:
				
				if explore.objects.filter(name=r['name']) :
					z='noo'
				#elif r['rating'] is not None :    
				 #   explore.objects.create(name=r['name'],rating=r['rating'],lat=r['geometry']['location']['lat'],lng=r['geometry']['location']['lng'],vicinity=r['vicinity'],type='cafe')
				 #   z = 'uyoo'
				else:
					explore.objects.create(name=r['name'],lat=r['geometry']['location']['lat'],lng=r['geometry']['location']['lng'],vicinity=r['vicinity'],type='cafe')    

			
			z = explore.objects.filter(type='cafe')
			context = { 'z' : z ,
						  
				}
			return render(request,'nearbyplaces.html',context)
	else :
		return redirect('login')
		
def Hospital(request):
		
		if request.user.is_authenticated():	
			url = 'https://freegeoip.net/json/'
			with closing(urlopen(url)) as response:
					location = json.loads(response.read())
					lng =  location['longitude']
					lat =  location['latitude']
			lat1 = decimal.Decimal(22.7167)+decimal.Decimal(0.007798)
			lng1 = decimal.Decimal(75.8333)+decimal.Decimal(0.044059)		

			name = explore.objects.all()
			AUTH_KEY = 'AIzaSyAF1M_y5ABZdZRWKTkhMjMJuq5Ysz6swm8'
			LOCATION = str(lat1) + "," + str(lng1)
			RADIUS = 1000
			TYPES = 'hospital'
			MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
											   '?location=%s'
											   '&radius=%s'
											   '&types=%s'
											   '&key=%s') % (LOCATION, RADIUS, TYPES, AUTH_KEY)
			f = urllib.request.urlopen(MyUrl)
			json_string = f.read()
			f.close()
			location = json.loads(json_string)

			for r in location['results']:
				
				if explore.objects.filter(name=r['name']) :
					z='noo'
				#elif r['rating'] is not None :    
				 #   explore.objects.create(name=r['name'],rating=r['rating'],lat=r['geometry']['location']['lat'],lng=r['geometry']['location']['lng'],vicinity=r['vicinity'],type='cafe')
				 #   z = 'uyoo'
				else:
					explore.objects.create(name=r['name'],lat=r['geometry']['location']['lat'],lng=r['geometry']['location']['lng'],vicinity=r['vicinity'],type='hospital')    

			z = explore.objects.filter(type='hospital')
			context = { 'z' : z   }
			return render(request,'nearbyplaces.html',context)
		else :
		    return redirect('login')	
			
        
def School(request):
     if request.user.is_authenticated():		
        url = 'https://freegeoip.net/json/'
        with closing(urlopen(url)) as response:
         location = json.loads(response.read())
         lng =  location['longitude']
         lat =  location['latitude']
         lat1 = decimal.Decimal(22.7167)+decimal.Decimal(0.007798)
         lng1 = decimal.Decimal(75.8333)+decimal.Decimal(0.044059)		
        name = explore.objects.all()
        AUTH_KEY = 'AIzaSyAF1M_y5ABZdZRWKTkhMjMJuq5Ysz6swm8'
        LOCATION = str(lat1) + "," + str(lng1)
        RADIUS = 1000
        TYPES = 'school'
        MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
                                           '?location=%s'
                                           '&radius=%s'
                                           '&types=%s'
                                           '&key=%s') % (LOCATION, RADIUS, TYPES, AUTH_KEY)
        f = urllib.request.urlopen(MyUrl)
        json_string = f.read()
        f.close()
        location = json.loads(json_string)

        for r in location['results']:
            
            if explore.objects.filter(name=r['name']) :
                z='noo'
            #elif r['rating'] is not None :    
             #   explore.objects.create(name=r['name'],rating=r['rating'],lat=r['geometry']['location']['lat'],lng=r['geometry']['location']['lng'],vicinity=r['vicinity'],type='cafe')
             #   z = 'uyoo'
            else:
                explore.objects.create(name=r['name'],lat=r['geometry']['location']['lat'],lng=r['geometry']['location']['lng'],vicinity=r['vicinity'],type='school')    

        z = explore.objects.filter(type='school')
        context = { 'z' : z   }
        return render(request,'nearbyplaces.html',context)
     else:return redirect('login')        
                
	
def Shopping_mall(request):
    if request.user.is_authenticated():         
      url = 'https://freegeoip.net/json/'
      with closing(urlopen(url)) as response:
       location = json.loads(response.read())
       lng = location['longitude']
       lat = location['latitude']
       lat1 = decimal.Decimal(22.7167)+decimal.Decimal(0.007798)
       lng1 = decimal.Decimal(75.8333)+decimal.Decimal(0.044059)           

      name = explore.objects.all()
      AUTH_KEY = 'AIzaSyAF1M_y5ABZdZRWKTkhMjMJuq5Ysz6swm8'
      LOCATION = str(lat1) + "," + str(lng1)
      RADIUS = 1000
      TYPES = 'shopping_mall'
      MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
					   '?location=%s'
					   '&radius=%s'
					   '&types=%s'
					   '&key=%s') % (LOCATION, RADIUS, TYPES, AUTH_KEY)
      f = urllib.request.urlopen(MyUrl)
      json_string = f.read()
      f.close()
      location = json.loads(json_string)

      for r in location['results']:
            
            if explore.objects.filter(name=r['name']) :
                z='noo'
            #elif r['rating'] is not None :    
             #   explore.objects.create(name=r['name'],rating=r['rating'],lat=r['geometry']['location']['lat'],lng=r['geometry']['location']['lng'],vicinity=r['vicinity'],type='cafe')
             #   z = 'uyoo'
            else:
                explore.objects.create(name=r['name'],lat=r['geometry']['location']['lat'],lng=r['geometry']['location']['lng'],vicinity=r['vicinity'],type='shopping_mall')    

      z = explore.objects.filter(type='shopping_mall')
      context = { 'z' : z   }
      return render(request,'nearbyplaces.html',context)
    else:return redirect('login')            
		
	
def Restaurant(request):
    if request.user.is_authenticated():         
      url = 'https://freegeoip.net/json/'
      with closing(urlopen(url)) as response:
       location = json.loads(response.read())
       lng = location['longitude']
       lat = location['latitude']
       lat1 = decimal.Decimal(22.7167)+decimal.Decimal(0.007798)
       lng1 = decimal.Decimal(75.8333)+decimal.Decimal(0.044059)           

      name = explore.objects.all()
      AUTH_KEY = 'AIzaSyAF1M_y5ABZdZRWKTkhMjMJuq5Ysz6swm8'
      LOCATION = str(lat1) + "," + str(lng1)
      RADIUS = 1000
      TYPES = 'restaurant'
      MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
					   '?location=%s'
					   '&radius=%s'
					   '&types=%s'
					   '&key=%s') % (LOCATION, RADIUS, TYPES, AUTH_KEY)
      f = urllib.request.urlopen(MyUrl)
      json_string = f.read()
      f.close()
      location = json.loads(json_string)

      for r in location['results']:
            
            if explore.objects.filter(name=r['name']) :
                z='noo'
            #elif r['rating'] is not None :    
             #   explore.objects.create(name=r['name'],rating=r['rating'],lat=r['geometry']['location']['lat'],lng=r['geometry']['location']['lng'],vicinity=r['vicinity'],type='cafe')
             #   z = 'uyoo'
            else:
                explore.objects.create(name=r['name'],lat=r['geometry']['location']['lat'],lng=r['geometry']['location']['lng'],vicinity=r['vicinity'],type='restaurant')    

      z = explore.objects.filter(type='restaurant')
      context = { 'z' : z   }
      return render(request,'nearbyplaces.html',context)
    else:return redirect('login')
    
def Movie_theater(request):
    if request.user.is_authenticated():         
      url = 'https://freegeoip.net/json/'
      with closing(urlopen(url)) as response:
       location = json.loads(response.read())
       lng = location['longitude']
       lat = location['latitude']
       lat1 = decimal.Decimal(22.7167)+decimal.Decimal(0.007798)
       lng1 = decimal.Decimal(75.8333)+decimal.Decimal(0.044059)           

      name = explore.objects.all()
      AUTH_KEY = 'AIzaSyAF1M_y5ABZdZRWKTkhMjMJuq5Ysz6swm8'
      LOCATION = str(lat1) + "," + str(lng1)
      RADIUS = 1000
      TYPES = 'movie_theater'
      MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
					   '?location=%s'
					   '&radius=%s'
					   '&types=%s'
					   '&key=%s') % (LOCATION, RADIUS, TYPES, AUTH_KEY)
      f = urllib.request.urlopen(MyUrl)
      json_string = f.read()
      f.close()
      location = json.loads(json_string)

      for r in location['results']:
            
            if explore.objects.filter(name=r['name']) :
                z='noo'
            #elif r['rating'] is not None :    
             #   explore.objects.create(name=r['name'],rating=r['rating'],lat=r['geometry']['location']['lat'],lng=r['geometry']['location']['lng'],vicinity=r['vicinity'],type='cafe')
             #   z = 'uyoo'
            else:
                explore.objects.create(name=r['name'],lat=r['geometry']['location']['lat'],lng=r['geometry']['location']['lng'],vicinity=r['vicinity'],type='movie_theater')    

      z = explore.objects.filter(type='movie_theater')
      context = { 'z' : z   }
      return render(request,'nearbyplaces.html',context)
    else:return redirect('login')
    
		
def detail(request,id) : 
		  z = explore.objects.get(pk = id)
		  context = { 'z' : z ,
					}
		  return render(request,'detail.html',context)		
			
