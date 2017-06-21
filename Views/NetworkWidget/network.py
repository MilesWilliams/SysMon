import os
import psutil
from PyQt5 import QtGui, QtCore, QtWidgets
from Models.NetworkConnection.wifi_snifer import WiFi
from Models.NetworkConnection.wifi_network import WifiConnectionsModel


class NetworkInormation(QtWidgets.QWidget):

    def __init__(self, parent):
        super(NetworkInormation, self).__init__(parent)

        self.setupUI()
        self.show()

    def setupUI(self):
        widget_layout = QtWidgets.QVBoxLayout(self)
        widget_layout.setContentsMargins(0, 0, 0, 0)
        self.heading = QtWidgets.QLabel(self)
        self.heading.setText('Network')
        self.heading.setObjectName('networkHeading')
        self.network_table = QtWidgets.QTableView(self)
        self.network_table.setObjectName('networkListView')
        self.network_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.network_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.network_table.setShowGrid(False)
        self.network_table.setGridStyle(QtCore.Qt.NoPen)
        self.network_table.horizontalHeader().setVisible(False)
        self.network_table.horizontalHeader().setHighlightSections(False)
        self.network_table.verticalHeader().setVisible(False)
        self.network_table.verticalHeader().setHighlightSections(False)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.get_network_info)
        timer.start(500)

        widget_layout.addWidget(self.heading)
        widget_layout.addWidget(self.network_table)

    def get_network_info(self):
        wifi = WiFi()

        if wifi.get_ssid():
            wifiSsid = str(wifi.get_ssid())

        model = WifiConnectionsModel([
            ["Status", wifi.get_wifistatus()],
            ["WiFi Name :", wifiSsid],
            ["Transfer Rate :", str(wifi.get_transmitrate()) + "kps"]
        ])
        self.network_table.setModel(model)
