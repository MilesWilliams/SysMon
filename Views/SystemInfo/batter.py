import os
import psutil
from PyQt5 import QtGui, QtCore, QtWidgets
from Models.BatteryConnection.battery import InternalBattery


class Batteryformation(QtWidgets.QWidget):
    def __init__(self, parent):
        super(Batteryformation, self).__init__(parent)

        self.setupUI()
        self.show()

    def setupUI(self):
        widget_layout = QtWidgets.QVBoxLayout(self)
        widget_layout.setContentsMargins(0, 0, 0, 0)
        self.heading = QtWidgets.QLabel(self)
        self.heading.setText('Battery')
        self.remainingBatteryLifeLabel = QtWidgets.QLabel(self)
        self.chargingLabel = QtWidgets.QLabel(self)
        self.lineSeperator = QtWidgets.QFrame()
        self.lineSeperator.setObjectName('lineSeperator')
        self.lineSeperator.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineSeperator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineSeperator.setGeometry(QtCore.QRect(20, 10, 8, 3))
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.get_battery_information)
        timer.start(1000)
        widget_layout.addWidget(self.heading, 0)
        widget_layout.addWidget(self.lineSeperator, 0)
        widget_layout.addWidget(self.remainingBatteryLifeLabel, 0)
        widget_layout.addWidget(self.chargingLabel, 0)
        # widget_layout.addStretch(0)

    def get_battery_information(self):
        internalBattery = InternalBattery()
        self.remainingBatteryLifeLabel.setText('Battery Life : {}%'.format(internalBattery.current_capacity()))
        if internalBattery.is_charging() == True:
            self.chargingLabel.setText('Battery Charging')
        elif internalBattery.is_charging() == False:
            self.chargingLabel.setText('Laptop Unplugged')
