import phonenumbers
import folium

from phonenumbers import geocoder
phone_number = input(str("Inserer un numéro ici : " ))

#get your api key on opencage
apikey = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

samNumber = phonenumbers.parse(phone_number)

yourLocation = geocoder.description_for_number(samNumber, 'en')
print(yourLocation)

##get isp

from phonenumbers import carrier

isp = phonenumbers.parse(phone_number)
print(carrier.name_for_number(isp, 'en'))


##LOACTION MAP
from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(apikey)

query =  str(yourLocation)

results = geocoder.geocode(query)

print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat,lng], zoom_start = 9)

folium.Marker([lat, lng], popup=yourLocation).add_to((myMap))

##save to html file

myMap.save("location.html")
