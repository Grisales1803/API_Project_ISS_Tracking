import requests
import datetime
from ISS_location import locationISS
from weather import weather
from country import info_country
from distance_ISS import distance_to_ISS
from flask import Flask, render_template, request 

app = Flask('app')
# Activate the App inside Flask
# / is the main page of the website, example AOL
@app.route('/')  
def home():
  # Obtain latitude and longitude from the ISS location function
  lat, lon = locationISS()
  # Obtain the map URL
  map = "https://google.com/maps/place/"+ lat +","+ lon
  # Obtain the temperature in Celsius and the weather description
  temp, description, country_code, water = weather(lat, lon)
  # Obtain the flag and the flag meaning of the country
  country = country_code
  if water == False:
    flag, flag_meaning, country_name = info_country(country)
  else:
    flag = "https://static.vecteezy.com/system/resources/previews/028/086/717/original/ocean-water-surface-waves-isolated-on-transparent-background-file-cut-out-ai-generated-png.png"
    flag_meaning = "The ISS is over water"
    country_name = "The Ocean"
  # Obtain the distance from the ISS to my location, which is Saskatoon, SK, Canada
  lat2, lon2 = 52.133220, -106.670070 # Saskatoon, SK coordinates
  dist = distance_to_ISS(lat, lon, lat2, lon2)
  # Return the values that are going to be used in the HTML page
  return render_template("index.html", lat=lat, lon=lon, map=map, temp=temp, description=description,country=country_name, flag=flag, flag_meaning=flag_meaning, dist=dist)

# Run the app
app.run(host='0.0.0.0', port=8080)