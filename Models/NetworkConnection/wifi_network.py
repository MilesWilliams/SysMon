from PyQt5 import QtGui, QtCore, QtWidgets


class WifiConnectionsModel(QtCore.QAbstractTableModel):
    def __init__(self, wifiInformation=[[]], parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._wifiInformation = wifiInformation

    def columnCount(self, parent):
        return len(self._wifiInformation[0])

    def rowCount(self, parent):
        return len(self._wifiInformation)

    def flags(self, parent):
        return QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled

    def data(self, index, role):
        if role == QtCore.Qt.TextAlignmentRole:
            row = index.row()
            col = index.column()
            if col == 0:
                return int(QtCore.Qt.AlignLeft)
            else:
                return int(QtCore.Qt.AlignRight)

        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            col = index.column()
            value = self._wifiInformation[row][col]
            return value
