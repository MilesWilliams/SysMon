from PyQt5 import QtGui, QtCore, QtWidgets


class ForecastTable(QtCore.QAbstractTableModel):
    def __init__(self, forecasts=[[]], parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._forecasts = forecasts

    def columnCount(self, parent):
        return len(self._forecasts)
        pass

    def rowCount(self, parent):
        return len(self._forecasts[0])

    def flags(self, parent):
        return QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled

    def data(self, index, role):
        icon = QtGui.QIcon('icons/settings.png')
        if role == QtCore.Qt.TextAlignmentRole:
            row = index.row()
            col = index.row()
            if self._forecasts[col][row]:

                return int(QtCore.Qt.AlignCenter)

        elif role == QtCore.Qt.DecorationRole:
            row = index.row()
            col = index.row()
            # if self._forecasts[col][row] == "":
            #     icon = QtGui.QPixmap("icons/cloud.png")
            if type(self._forecasts[col][row]) != str:
                icon = self._forecasts[col][row].scaled(50, 28)

                return icon

        elif role == QtCore.Qt.DisplayRole:
            row = index.row()
            col = index.column()
            # if self._forecasts[col][row] != "":
            value = self._forecasts[col][row]

            return value
