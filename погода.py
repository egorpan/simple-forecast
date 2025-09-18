import requests

CITY_NAME = "Tashkent"
API = "59a3955521c146fa9e9132721251709"
URL = f"http://api.weatherapi.com/v1/current.json?key={API}&q={CITY_NAME}"

print(requests.get(URL).json()['current']['temp_c'])

forecast = {
    "temperature" : requests.get(URL).json()['current']['temp_c'],
    "feels like" : requests.get(URL).json()['current']['feelslike_c'],
}

class City:
    def __init__(self,name,forecast):
        self.name = name
        self.forecast= forecast

    def __str__(self):
        return(f"in {self.name} temperature is {self.forecast["temperature"]}, feels like {self.forecast["feels like"]}")

city_forecast = City(CITY_NAME,forecast)
print(city_forecast)