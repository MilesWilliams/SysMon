import os
import psutil
from PyQt5 import QtGui, QtCore, QtWidgets
from Models.NetworkConnection.wifi_snifer import WiFi


class NetworkInormation(QtWidgets.QWidget):

    def __init__(self, parent):
        super(NetworkInormation, self).__init__(parent)

        self.setupUI()
        self.show()

    def setupUI(self):
        widget_layout = QtWidgets.QVBoxLayout(self)
        widget_layout.setContentsMargins(0, 20, 0, 0)
        self.heading = QtWidgets.QLabel(self)
        self.heading.setText('Network')
        self.networkNameLabel = QtWidgets.QLabel(self)
        self.networkSpeedLabel = QtWidgets.QLabel(self)
        self.connectionStatsus = QtWidgets.QLabel(self)
        self.lineSeperator = QtWidgets.QFrame()
        self.lineSeperator.setObjectName('lineSeperator')
        self.lineSeperator.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineSeperator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineSeperator.setGeometry(QtCore.QRect(20, 10, 8, 3))
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.get_network_info)
        timer.start(500)

        widget_layout.addWidget(self.heading)
        widget_layout.addWidget(self.lineSeperator)
        widget_layout.addWidget(self.networkNameLabel)
        widget_layout.addWidget(self.connectionStatsus)
        widget_layout.addWidget(self.networkSpeedLabel)

    def get_network_info(self):
        wifi = WiFi()
        if wifi.get_ssid():
            self.networkNameLabel.setText("WiFi Name : " + wifi.get_ssid())
        self.connectionStatsus.setText(wifi.get_wifistatus())
        self.networkSpeedLabel.setText('Transfer Rate : {}kps'.format(wifi.get_transmitrate()))
