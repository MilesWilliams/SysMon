import sys
import math
from PyQt5 import QtWidgets, QtCore, QtGui
import requests


class WeatherWidget(object):

    def __init__(self, parent=None):
        super(WeatherWidget, self).__init__(parent)
        self.startDownload()
        # self.setupUI()
        # self.show()

    def startDownload(self):
        url = "https://query.yahooapis.com/v1/public/yql?q=select * from weather.forecast where woeid= 1591691 and u='c'&format=json"
        self.threads = []
        print('start downloading weather')
        download = YahooApi(url)
        # timer = QtCore.QTimer(self)
        # timer.timeout.connect(self.on_data_ready)
        # timer.start(500)
        download.data_downloaded.connect(self.on_data_ready)
        self.threads.append(download)
        download.start()

    def on_data_ready(self, data):
        content = data
        currentDay = content['query']['results']['channel']['item']['condition']
        location = content['query']['results']['channel']['location']
        forecast = content['query']['results']['channel']['item']['forecast']
        wind = content['query']['results']['channel']['wind']
        print(content)

        # return [currentDay, location, forecast, wind]


class YahooApi(QtCore.QThread):
    data_downloaded = QtCore.pyqtSignal(object)

    def __init__(self, url):
        QtCore.QThread.__init__(self)
        self.url = url

    def run(self):
        info = requests.get(self.url)
        content = info.json()
        print(content)
        self.data_downloaded.emit(content)
