import os , requests
from dotenv import load_dotenv
from dataclasses import dataclass 

load_dotenv() ## loads env file variables into main files 
API_key=os.getenv("API_KEY")

@dataclass
class weatherclass :
    icon: str
    main: str
    description: str
    temp: int
    feels_like: int
    name:  str



def getLatLon(city_name,state_code, country_code) :
    
    latlon=requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}").json()
    lat=latlon[0].get('lat') # json is returning list of dictionaries 
    lon=latlon[0].get('lon')
    return lat , lon 

def getweatherUpdates(lat,lon) :
     
    weather=requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric").json()
    data=weatherclass(weather.get("weather")[0].get("icon"),weather.get("weather")[0].get("main"), weather.get("weather")[0].get("description"),int(weather.get("main")["temp"]),int(weather.get("main")["feels_like"]), weather.get("name"))  

    return data

def weather5dayData(lat,lon) :
 
 data2d={}
 j=1
 datanew=requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key}").json()  #requests is used to fetch  data from external sources
 print (datanew)
 
 return datanew



lat,lon=getLatLon("Lahore","PB","PK")
weather5dayData(lat,lon)