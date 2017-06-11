import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from time import strftime
import datetime


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("SysMon")
        self.setGeometry(50, 50, 0, 0)
        self.setCentralWidget(Timer(self))


class Timer(QtWidgets.QWidget):
    def __init__(self, parent):
        super(Timer, self).__init__(parent)
        self.setupUI()
        self.show()

    def setupUI(self):
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setObjectName("verticalLayout")
        timer = QtCore.QTimer(self)

        timer.timeout.connect(self.Time)
        timer.start(10)

        # Create Main Window
        main_window = QtWidgets.QListWidget()

        # Create settings Icon label
        self.settingsIcon = QtWidgets.QLabel(self)
        self.settingsIcon.setObjectName("settingsIcon")
        image = QtGui.QPixmap()
        image.load('icons/settings.png')
        self.settingsIcon.setPixmap(image)

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

    def Time(self):
        self.timeLabel.setText(strftime("%H" + " : " + "%M"))
