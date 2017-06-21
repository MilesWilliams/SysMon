import sys
import math
from PyQt5 import QtWidgets, QtCore, QtGui
import requests
import time


class Weather(object):

    def __init__(self, url=""):
        self.url = url
        self.data = self.get_data(self.url)

    def get_data(self, url):

        try:
            print(url)
            info = requests.get(url)
            content = info.json()
            info.raise_for_status()
            print("success")
            return content
        except requests.exceptions.ConnectionError as e:
            # catastrophic error. bail.
            content = "Could not retrieve forecasts"
            print(e, "fail")
            sys.exit(1)
            return content

    def get_current_temp(self):

        currentDay = str(round(self.data['currently']['temperature'])) + "˚"

        return currentDay

    def get_forecast(self):
        if self.data is None:
            forecast = "Could not retrieve forecasts"
            return forecast
        else:
            forecast_array = self.data['daily']['data']
            weekly_forecast = []
            for day in forecast_array[1:]:
                forecast = [time.strftime('%a', time.localtime(day["time"])), QtGui.QPixmap("icons/cloud.png"), str(round(day["temperatureMin"])) + "˚/ " + str(round(day["temperatureMax"])) + "˚"]
                weekly_forecast.append(forecast)

            return weekly_forecast

    def get_location(self):
        location = self.data['query']['results']['channel']['location']
        return location

    def get_wind_conditions(self):
        mpsTokmh = 3.6
        wind = str(round(self.data['currently']['windSpeed'] * mpsTokmh, 2)) + " km/h"
        return wind

    def get_rain_chance(self):
        rainPercent = str(int(self.data['currently']['precipProbability'] * 100)) + " %"
        return rainPercent

    def get_pressure(self):
        pressurePercent = str(self.data['currently']['pressure'])
        return pressurePercent
