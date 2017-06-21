from PyQt5 import QtGui, QtCore, QtWidgets
from time import strftime
from Views.SettingsWindow.SettingsWindow import SettingsMenu
from Models.DateTime.date_time import DateTime
import datetime


class Timer(QtWidgets.QWidget):
    timeDisplayFormat = True

    def __init__(self, parent):
        super(Timer, self).__init__(parent)

        self.setupUI()
        self.show()

    def setupUI(self):
        layout = QtWidgets.QHBoxLayout(self)
        layout.setSpacing(5)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setObjectName("verticalLayout")
        timer = QtCore.QTimer(self)

        timer.timeout.connect(self.time)
        timer.start(10)

        # Create settings Icon label

        self.settingsIcon = QtWidgets.QLabel(self)
        self.settingsIcon.setObjectName("settingsIcon")
        image = QtGui.QPixmap()
        image.load('icons/settings.png')
        self.settingsIcon.setPixmap(image)
        self.settingsIcon.mousePressEvent = self.open_settings_menu
        # Create time label
        self.timeLabel = QtWidgets.QLabel(self)
        self.timeLabel.setObjectName('timeLabel')

        # Create line seperator
        self.line = QtWidgets.QFrame()
        self.line.setObjectName('line')
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setGeometry(QtCore.QRect(20, 10, 8, 3))

        # Create date label
        self.dateLabel = QtWidgets.QLabel(self)
        self.dateLabel.setObjectName('dateLabel')
        self.dateLabel.setText(datetime.datetime.now().strftime('%d %B, %Y'))

        # Add all created widgets
        # layout.addWidget(self.settingsIcon, 100)

        layout.addWidget(self.dateLabel, 1)

        layout.addWidget(self.timeLabel, 1)
        # layout.addStretch(0)
        # layout.addWidget(main_window)

    def time(self):

        if self.timeDisplayFormat is True:
            self.timeLabel.setText(strftime("%H" + " : " + "%M"))

        else:
            self.timeLabel.setText(strftime("%H" + " : " + "%M" + " : " + "%S"))

        self.dateLabel.setText(datetime.datetime.now().strftime('%d %B, %Y'))

    def open_settings_menu(self, event):
        SettingsMenu(self)


# class Timer(QtWidgets.QWidget):
#     timeDisplayFormat = True

#     def __init__(self, parent):
#         super(Timer, self).__init__(parent)

#         self.setupUI()
#         self.show()

#     def setupUI(self):
#         layout = QtWidgets.QVBoxLayout(self)
#         layout.setSpacing(5)
#         layout.setContentsMargins(0, 0, 0, 0)
#         layout.setObjectName("verticalLayout")
#         self.tableView = QtWidgets.QTableView(self)
#         self.tableView.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
#         self.tableView.setAttribute(QtCore.Qt.WA_MacShowFocusRect, False)
#         self.tableView.setGeometry(QtCore.QRect(0, 0, 218, 20))
#         self.tableView.setObjectName('tableView')
#         self.tableView.setShowGrid(False)
#         self.tableView.setGridStyle(QtCore.Qt.NoPen)
#         self.tableView.horizontalHeader().setVisible(False)
#         self.tableView.horizontalHeader().setDefaultSectionSize(111)
#         self.tableView.horizontalHeader().setHighlightSections(False)
#         self.tableView.verticalHeader().setVisible(False)
#         self.tableView.verticalHeader().setHighlightSections(False)
#         timer = QtCore.QTimer(self)

#         timer.timeout.connect(self.time)
#         timer.start(10)

#         # Create settings Icon label

#         self.settingsIcon = QtWidgets.QLabel(self)
#         self.settingsIcon.setObjectName("settingsIcon")
#         image = QtGui.QPixmap()
#         image.load('icons/settings.png')
#         self.settingsIcon.setPixmap(image)
#         self.settingsIcon.mousePressEvent = self.open_settings_menu

#         # Create line seperator
#         self.line = QtWidgets.QFrame()
#         self.line.setObjectName('line')
#         self.line.setFrameShape(QtWidgets.QFrame.HLine)
#         self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
#         self.line.setGeometry(QtCore.QRect(20, 10, 8, 3))

#         # Add all created widgets
#         layout.addWidget(self.settingsIcon)
#         layout.addWidget(self.tableView)
#         layout.addWidget(self.line)

#     def time(self):

#         if self.timeDisplayFormat == True:
#             date = str(datetime.datetime.now().strftime('%d %B, %Y'))
#             time = str(strftime('%H' + ' : ' + '%M'))

#             model = [[date, time]]
#         else:
#             date = str(datetime.datetime.now().strftime('%d %B, %Y'))
#             time = str(strftime("%H" + " : " + "%M" + " : " + "%S"))
#             model = [[date, time]]
#             # self.timeLabel.show()

#         self.tableView.setModel(DateTime(model))

#     def open_settings_menu(self, event):
#         SettingsMenu(self)
