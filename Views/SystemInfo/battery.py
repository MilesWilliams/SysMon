import os
import psutil
from PyQt5 import QtGui, QtCore, QtWidgets
from Controllers.BatteryConnection.battery import InternalBattery
from Models.BatteryConnection.battery_model import BatteryTableModel


class Batteryformation(QtWidgets.QWidget):
    def __init__(self, parent):
        super(Batteryformation, self).__init__(parent)

        self.setupUI()
        self.show()

    def setupUI(self):
        widget_layout = QtWidgets.QVBoxLayout(self)
        widget_layout.setContentsMargins(0, 0, 0, 0)
        heading = QtWidgets.QLabel('Battery')
        heading.setObjectName('batterHeader')
        heading.sizeHint()
        self.batterTable = QtWidgets.QTableView(self)
        self.batterTable.setObjectName('batterTable')
        self.batterTable.setShowGrid(False)
        self.batterTable.setGridStyle(QtCore.Qt.NoPen)
        self.batterTable.horizontalHeader().setVisible(False)
        self.batterTable.horizontalHeader().setHighlightSections(False)
        self.batterTable.verticalHeader().setVisible(False)
        self.batterTable.verticalHeader().setHighlightSections(False)
        self.chargingLabel = QtWidgets.QLabel(self)

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.get_battery_information)
        timer.start(1000)
        widget_layout.addWidget(heading)
        widget_layout.addWidget(self.batterTable)
        # widget_layout.addStretch(0)

    def get_battery_information(self):
        internalBattery = InternalBattery()
        model = BatteryTableModel([['Battery Life :', internalBattery.current_capacity()], ['Status :', internalBattery.is_charging()]])
        self.batterTable.setModel(model)
