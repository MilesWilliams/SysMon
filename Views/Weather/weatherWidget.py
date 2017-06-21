from PyQt5 import QtGui, QtCore, QtWidgets
import sys
import math
import requests
from Models.Weather.weather import Weather


class ItemDelegate(QtWidgets.QStyledItemDelegate):
    def paint(self, painter, option, index):
        option.decorationPosition = QtWidgets.QStyleOptionViewItem.Right
        super(ItemDelegate, self).paint(painter, option, index)


class WeatherView(QtWidgets.QWidget):
    def __init__(self, parent):
        super(WeatherView, self).__init__(parent)
        self.cust_time = False
        self.setupUI()
        self.show()

    def setupUI(self):
        self.time = 10000
        self.widget_Hlayout = QtWidgets.QHBoxLayout(self)
        self.forecats_layout = QtWidgets.QHBoxLayout(self)
        self.widget_Vlayout = QtWidgets.QVBoxLayout(self)
        self.currentTemp = QtWidgets.QLabel(self)
        self.currentTemp.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.delegate = ItemDelegate()
        self.currentTempStatsListView = QtWidgets.QListWidget(self)
        self.currentTempStatsListView.setItemDelegate(self.delegate)
        self.currentTempStatsListView.setObjectName('currentTempStatsListView')
        self.currentTempStatsListView.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.currentTempStatsListView.setAttribute(QtCore.Qt.WA_MacShowFocusRect, False)
        self.widget_Hlayout.setContentsMargins(0, 0, 0, 0)
        self.forecats_layout.setContentsMargins(0, 0, 0, 0)
        self.currentTemp.setObjectName('currentTemp')
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.on_data_ready)
        if self.cust_time is False:
            print("false")
        else:
            print("true")
        if self.cust_time is False:
            print("false")
            timer.setInterval(1000)
            self.cust_time = True
        elif self.cust_time is True:
            print("true")
            timer.setInterval(2000)
        timer.setSingleShot(True)
        timer.start()
        self.time = 10000
        self.widget_Hlayout.addWidget(self.currentTemp)
        self.widget_Hlayout.addWidget(self.currentTempStatsListView)

    def on_data_ready(self):
        self.cust_time = True
        self.api_key = "37f62a82c7aacb78d49bc9e18d8529a0"
        self.units = "units=si"
        self.lon = "-33.9249"
        self.lat = "18.4241"
        self.url = "https://api.darksky.net/forecast/" + self.api_key + "/" + self.lat + "," + self.lon + "?" + self.units

        weather_data = Weather(self.url)

        self.currentTemp.setText(weather_data.get_current_temp())
        rainChance = QtWidgets.QListWidgetItem()
        rainChance.setTextAlignment(QtCore.Qt.AlignRight)
        rainChance.setText(weather_data.get_rain_chance())
        umbrellaIcon = QtGui.QIcon("icons/umbrella.png")
        rainChance.setIcon(umbrellaIcon)
        pressurePercent = QtWidgets.QListWidgetItem()
        barometerIcon = QtGui.QIcon("icons/barometer.png")
        pressurePercent.setTextAlignment(QtCore.Qt.AlignRight)
        pressurePercent.setText(weather_data.get_pressure())
        pressurePercent.setIcon(barometerIcon)
        wind = QtWidgets.QListWidgetItem()
        windIcon = QtGui.QIcon("icons/wind.png")
        wind.setTextAlignment(QtCore.Qt.AlignRight)
        wind.setText(weather_data.get_wind_conditions())
        wind.setIcon(windIcon)
        self.currentTempStatsListView.addItem(pressurePercent)
        self.currentTempStatsListView.addItem(rainChance)
        self.currentTempStatsListView.addItem(wind)
