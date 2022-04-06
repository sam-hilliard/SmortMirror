"""
Contains methods for fetching weather data from
an api to be used for the smart mirror.
"""

from matplotlib.pyplot import get
import requests
import json
import os
import sys
# from dotenv import load_dotenv

# load_dotenv()

API_KEY = ""

BASE_URL = "https://weatherbit-v1-mashape.p.rapidapi.com/"

HEADERS = {
	"X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com",
	"X-RapidAPI-Key": f"{API_KEY}"
}

class WeatherAPI:

    def __init__(self, city, state, country):
        self.querystring = {"city":f"{city},{state}","country":f"{country}", "units":"I"}

    # gets the temperature and weather description of a specified location
    def fetch_cur(self):
        response = requests.request("GET", BASE_URL + "current", headers=HEADERS, params=self.querystring)
        data = json.loads(response.text)["data"][0]

        return data["temp"], data["weather"]

    # gets the low, high, and weather description of 5 concurrent days
    def fetch_forecast(self):
        response = requests.request("GET", BASE_URL + "forecast/3hourly", headers=HEADERS, params=self.querystring)
        data = json.loads(response.text)["data"]

        week_forecast = []
        high_temp = False
        low_temp = False
        weather_descs = {}
        prev_date = data[0]["datetime"].split(":")[0]
        for hourly_data in data:

            # update week_forecast with the day's high, low, and description of the weather
            cur_date = hourly_data["datetime"].split(":")[0]
            if (cur_date != prev_date):
                week_forecast.append({
                    "high": high_temp,
                    "low": low_temp,
                    "date": prev_date,
                    "weather": max(weather_descs, key=weather_descs.get)
                })
                high_temp = False
                low_temp = False
                prev_date = cur_date
                weather_descs = {}

            # keeps track of the count of different weather descriptions for the day
            desc = hourly_data["weather"]["description"]
            if desc in weather_descs:
                weather_descs[desc] += 1
            else:
                weather_descs[desc] = 0

            # determines the current high and low at a given 3-hour block
            temp = hourly_data["temp"]
            if (not high_temp):
                high_temp = temp
            else:
                high_temp = max(temp, high_temp)
            
            if (not low_temp):
                low_temp = temp
            else:
                low_temp = min(temp, low_temp)
        
        return week_forecast

def main():
    weather_api = WeatherAPI("San Diego", "CA", "US")
    cur_weather = weather_api.fetch_cur()

    print(cur_weather)

    forecast = weather_api.fetch_forecast()
    print(forecast)


if __name__ == '__main__':
    main()