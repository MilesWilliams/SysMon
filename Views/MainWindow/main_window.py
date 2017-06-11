import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from time import strftime
import datetime
from Views.SettingsWindow.SettingsWindow import SettingsMenu


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("SysMon")
        self.setGeometry(50, 50, 0, 0)
        self.setCentralWidget(Timer(self))


class Timer(QtWidgets.QWidget):
    timeDisplayFormat = True

    def __init__(self, parent):
        super(Timer, self).__init__(parent)

        self.setupUI()
        self.show()

    def setupUI(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.setSpacing(5)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setObjectName("verticalLayout")
        timer = QtCore.QTimer(self)

        timer.timeout.connect(self.time)
        timer.start(10)

        # Create Main Window
        main_window = QtWidgets.QListWidget()

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
        layout.addWidget(self.settingsIcon)
        layout.addWidget(self.timeLabel)
        layout.addWidget(self.line)
        # layout.addStretch(1)
        layout.addWidget(self.dateLabel)

        # layout.addWidget(main_window)

    def time(self):

        if self.timeDisplayFormat == True:
            self.timeLabel.setText(strftime("%H" + " : " + "%M"))

        else:
            self.timeLabel.setText(strftime("%H" + " : " + "%M" + " : " + "%S"))

    def open_settings_menu(self, event):
        SettingsMenu(self)
