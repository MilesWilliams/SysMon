from PyQt5 import QtGui, QtCore, QtWidgets


class SystemModel(QtCore.QAbstractTableModel):
    def __init__(self, systemInformation=[[]], parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._systemInformation = systemInformation

    def columnCount(self, parent):
        return len(self._systemInformation[0])
        pass

    def rowCount(self, parent):
        return len(self._systemInformation)

    def flags(self, parent):
        return QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled

    def data(self, index, role):
        icon = QtGui.QIcon('icons/settings.png')
        if role == QtCore.Qt.TextAlignmentRole:
            row = index.row()
            col = index.column()
            if self._systemInformation[row][col] == "CPU :" or self._systemInformation[row][col] == "RAM :" or self._systemInformation[row][col] == "Avail. Memory :" or self._systemInformation[row][col] == "Free Swap :" or self._systemInformation[row][col] == "Hdd  :":
                return int(QtCore.Qt.AlignLeft)
            else:
                return int(QtCore.Qt.AlignRight)

        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            col = index.column()
            value = self._systemInformation[row][col]
            return value

