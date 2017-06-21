from PyQt5 import QtGui, QtCore, QtWidgets


class BatteryTableModel(QtCore.QAbstractTableModel):
    def __init__(self, batteryInformation=[[]], parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._batteryInformation = batteryInformation

    def columnCount(self, parent):
        return len(self._batteryInformation[0])
        pass

    def rowCount(self, parent):
        return len(self._batteryInformation)

    def flags(self, parent):
        return QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled

    def data(self, index, role):
        icon = QtGui.QIcon('icons/settings.png')
        if role == QtCore.Qt.TextAlignmentRole:
            row = index.row()
            col = index.column()
            if self._batteryInformation[row][col] == "Battery Life :" or self._batteryInformation[row][col] == "Status :":
                return int(QtCore.Qt.AlignLeft)
            else:
                return int(QtCore.Qt.AlignRight)

        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            col = index.column()
            value = self._batteryInformation[row][col]
            return value
