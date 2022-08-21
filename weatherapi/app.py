from flask import Flask, request
from config import *
import requests
import datetime as dt
from cachetools import cached, TTLCache

app = Flask(__name__)

cache = TTLCache(maxsize=1, ttl=120)

def temp_to_celsius(temp):
    return round((temp - 273.15), 2)


def temp_to_fahrenheit(temp):
    return round(temp_to_celsius(temp) * (9/5) + 32, 2)

def unix_to_timestamp(time):
    hour = dt.datetime.fromtimestamp(time).strftime('%H:%M')
    return hour

def get_wind(wind):
    wind_blow = ""
    if wind < 1:
        wind_blow = "Calm"
    elif wind >= 1 and wind <= 3:
        wind_blow = "Light Air"
    elif wind >= 4 and wind <= 7:
        wind_blow = "Light Breeze"
    elif wind >= 8 and wind <= 12:
        wind_blow = "Gentle Breeze"
    elif wind >= 13 and wind <= 18:
        wind_blow = "Moderate Breeze"
    elif wind >= 19 and wind <= 24:
        wind_blow = "Fresh Breeze"
    elif wind >= 25 and wind <= 31:
        wind_blow = "Strong Breeze"
    elif wind >= 32 and wind <= 38:
        wind_blow = "Near Gale"
    elif wind >= 39 and wind <= 46:
        wind_blow = "Gale"
    elif wind >= 47 and wind <= 54:
        wind_blow = "Strong Gale"
    elif wind >= 55 and wind <= 63:
        wind_blow = "Storm"
    elif wind >= 64 and wind <= 72:
        wind_blow = "Violent Storm"
    else:
        wind_blow = "Hurricane"
    return wind_blow

def get_degrees(degrees):
    deg= ""
    if degrees <= 0:
        deg = "North"
    elif degrees >= 1 and degrees <= 89:
        deg= "North-East"
    elif degrees == 90:
        deg= "East"
    elif degrees >= 91 and degrees <= 179:
        deg= "South-East"
    elif degrees == 180:
        deg= "South"
    elif degrees >= 181 and degrees <= 269:
        deg= "South-Weast"
    elif degrees == 270:
        deg= "Weast"
    elif degrees >= 271 and degrees <= 359:
        deg= "North-Weast"
    else:
        deg= "Wrong server response"
    return deg



@app.route('/weather')
#@cached(cache)
def weather_shower():
    
    city = request.args.get('city')
    country = request.args.get('country')
    url = ""
    if city != None and country != None:
       url = f"{OW_URL}q={city},{country}&appid={API_KEY}"

    elif city != None:
        
        url = f'{OW_URL}appid={API_KEY}&q={city}'    
        
    else:
        wrong= "Make a request"

        return wrong
    
   
    response = requests.get(url).json()

    print(response)      
    try:
        context = {"location_name": f'{response["name"]}, {response["sys"]["country"]}',
                "temperature in celsius": f"{temp_to_celsius(response['main']['temp'])} °C,",
                "temperature in fahrenhait": f"{temp_to_fahrenheit(response['main']['temp'])}°F",
                "wind": f"{get_wind(response['wind']['speed'])}, {response['wind']['speed']} m/s, {get_degrees(response['wind']['deg'])}",
                "cloudiness": response['weather'][0]['description'],
                "pressure": f"{response['main']['pressure']} hpa",
                "humidity": f"{response['main']['humidity']}%",
                "sunrise": unix_to_timestamp(response['sys']['sunrise']),
                "sunset": unix_to_timestamp(response['sys']['sunset']),
                "geo_coordinates": f"Lon: {response['coord']['lon']}, Lat: {response['coord']['lat']} ",
                "requested_time": dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        }
    except:
        return "Wrong request"

    return context
  
        

