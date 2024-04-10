
import python_weather
import asyncio
import os
import aiohttp
import json
import requests
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily
from requests.auth import HTTPBasicAuth
import geopy
from geopy.geocoders import Nominatim
from geopy.geocoders import get_geocoder_for_service
import ssl
#fdfdca55e586b42c135d05c2e5ca9b3a
#pip install
async def getweather():
  # declare the client. the measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(unit=python_weather.METRIC) as client:
    city = input('Напишите город чтобы узнать погоду ')
    # fetch a weather forecast from a city
    weather = await client.get(city)
    # returns the current day's forecast temperature (int)
    print(weather.temperature)
    
    # get the weather forecast for a few days
    for daily in weather.daily_forecasts:
      print(daily)
      
      # hourly forecasts
      for hourly in daily.hourly_forecasts:
        print(f' --> {hourly!r}')
#asyncio.run(getweather())

# Set time period
start = datetime(2018, 1, 1)
end = datetime(2018, 1, 2)

# Create Point for Vancouver, BC
vancouver = Point(49.2497, -123.1193, 70)

# Get daily data for 2018
data = Daily(vancouver, start, end)

data = data.fetch()

# Plot line chart including average, minimum and maximum temperature
data.plot(y=['tavg', 'tmin', 'tmax'])
print(data)
# importing geopy library








 
# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")
 
# entering the location name
getLoc = loc.geocode("Москва")
 
# printing address
print(getLoc.address)
 
# printing latitude and longitude
print("Latitude = ", getLoc.latitude)
print("Longitude = ", getLoc.longitude)
#print(data)