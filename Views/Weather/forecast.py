from PyQt5 import QtGui, QtCore, QtWidgets
import sys
import math
import requests
from Models.Weather.weather import Weather
from Models.Weather.current_weather_list import ForecastTable


class ItemDelegate(QtWidgets.QStyledItemDelegate):
    def paint(self, painter, option, index):
        option.decorationPosition = QtWidgets.QStyleOptionViewItem.Middle

        super(ItemDelegate, self).paint(painter, option, index)


class ForecastView(QtWidgets.QWidget):
    def __init__(self, parent):
        super(ForecastView, self).__init__(parent)
        self.cust_time = False
        self.setupUI()
        self.show()

    def setupUI(self):
        self.time = 10000
        self.forecats_layout = QtWidgets.QHBoxLayout(self)
        self.forecats_layout.setContentsMargins(0, 0, 0, 0)
        self.setGeometry(QtCore.QRect(0, 0, 244, 65))
        self.delegate = ItemDelegate()
        self.forecast_table = QtWidgets.QTableView(self)
        self.forecast_table.setItemDelegate(self.delegate)
        self.forecast_table.setGeometry(QtCore.QRect(0, 0, 244, 65))
        self.forecast_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.forecast_table.setObjectName('forecastTable')
        self.forecast_table.setShowGrid(False)
        self.forecast_table.setGridStyle(QtCore.Qt.NoPen)
        self.forecast_table.horizontalHeader().setVisible(False)
        self.forecast_table.horizontalHeader().setHighlightSections(False)
        self.forecast_table.verticalHeader().setVisible(False)
        self.forecast_table.verticalHeader().setHighlightSections(False)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.on_data_ready)
        if self.cust_time is False:
            timer.setInterval(1000)
            self.cust_time = True
        elif self.cust_time is True:
            timer.setInterval(2000)
        timer.setSingleShot(True)
        timer.start()
        self.time = 10000
        self.forecats_layout.addWidget(self.forecast_table)

    def on_data_ready(self):
        self.cust_time = True
        self.api_key = "37f62a82c7aacb78d49bc9e18d8529a0"
        self.units = "units=si"
        self.lon = "-33.9249"
        self.lat = "18.4241"
        self.url = "https://api.darksky.net/forecast/" + self.api_key + "/" + self.lat + "," + self.lon + "?" + self.units

        weather_data = Weather(self.url)
        model = ForecastTable(weather_data.get_forecast())
        self.forecast_table.setModel(model)
