import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from time import strftime
import datetime
from Views.Timer.system_clock import Timer
from Views.SettingsWindow.SettingsWindow import SettingsMenu
from Views.SystemInfo.battery import Batteryformation
from Views.SystemInfo.system_information import SystemInformation
from Views.NetworkWidget.network import NetworkInormation
from Views.Devices.device_widget import DeviceWidget
from Views.Weather.weatherWidget import WeatherView
from Views.Weather.forecast import ForecastView


class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setWindowOpacity(0.64)
        self.setWindowTitle("SysMon")
        self.setGeometry(20, 20, 242, 809)
        self.setObjectName('MainWindow')
        self.setStyleSheet("background: rgba(000,000,000,100%)")
        _widget = QtWidgets.QWidget()
        _layout = QtWidgets.QVBoxLayout(_widget)
        _layout.addWidget(Timer(self))
        _layout.addWidget(WeatherView(self))
        _layout.addWidget(ForecastView(self))
        _layout.addWidget(Batteryformation(self))
        _layout.addWidget(SystemInformation(self))
        _layout.addWidget(NetworkInormation(self))
        _layout.addWidget(DeviceWidget(self))
        self.setCentralWidget(_widget)
