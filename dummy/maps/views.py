from django.shortcuts import render
import requests
import json


import phonenumbers
from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode
import folium
# Create your views here.
#-----------------------------------------------------------------------------------------------------------#
def default_map(request): 
    ip = requests.get('https://api.ipify.org?format=json')
    ip_data = json.loads(ip.text)
    res = requests.get('http://ip-api.com/json/'+ ip_data["ip"])#ip json to dictionary
    loc_data = res.text
    loc_data = json.loads(loc_data)#location details json to dictionary
    lat = loc_data['lat']
    lng = loc_data['lon']
    myMap = folium.Map(location=[lat,lng],zoom_start=9)
    folium.Marker([lat,lng],popup=loc_data).add_to((myMap))
    myMap.save("location.html")
    return render(request, 'maps/default.html', {'data' : loc_data})

#Format in which ip-api returns loaction
'''{'status': 'success', 'country': 'Canada', 
'countryCode': 'CA', 'region': 'QC', 
'regionName': 'Quebec', 'city': 'Montreal', 
'zip': 'H1K', 'lat': 45.6085, 'lon': -73.5493, 
'timezone': 'America/Toronto', 'isp': 'Le Groupe Videotron Ltee', 
'org': 'Videotron Ltee', 'as': 'AS5769 Videotron Telecom Ltee', 'query': '24.48.0.1'}'''
#-----------------------------------------------------------------------------------------------------------#

Key = "55dfa4d9047a4de5ba5de1a5a2fbbd6f"


def map_test(number):


    sanNumber = phonenumbers.parse(number)
    loc = geocoder.description_for_number(sanNumber,"en")

    geo_coder = OpenCageGeocode(Key)
    query = str(loc)

    results = geo_coder.geocode(query)
    print(results[0])
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print(lat,lng)
    myMap = folium.Map(location=[lat,lng],zoom_start=9)
    folium.Marker([lat,lng],popup=loc).add_to((myMap))
    myMap.save("location.html")
    #return render(request,'maps/default.html')

number = "+919176283738"
map_test(number)