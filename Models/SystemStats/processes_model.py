from PyQt5 import QtGui, QtCore, QtWidgets


class Process(object):
    def __init__(self, pid, name, memory_percent, status):
        self.pid = pid
        self.name = name
        self.memory_percent = memory_percent
        self.status = status


class ProcessModel(QtCore.QAbstractTableModel):
    def __init__(self, processInformation=[[]], parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._processInformation = processInformation

    def columnCount(self, parent):
        return len(self._processInformation[0])

    def rowCount(self, parent):
        return len(self._processInformation)

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
            value = self._processInformation[row][col]
            return value
