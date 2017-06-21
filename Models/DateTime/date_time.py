from PyQt5 import QtGui, QtCore, QtWidgets


class DateTime(QtCore.QAbstractTableModel):
    def __init__(self, dateTime=[[]], parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._dateTime = dateTime

    def rowCount(self, parent):
        return 1

    def columnCount(self, parent):
        return len(self._dateTime[0])

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            col = index.column()
            value = self._dateTime[row][col]

            return value
