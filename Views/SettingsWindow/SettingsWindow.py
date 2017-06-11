import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from Views.MainWindow import main_window


class SettingsMenu(QtWidgets.QDialog):

    def __init__(self, parent):
        super(SettingsMenu, self).__init__(parent)
        self.setWindowTitle("Settings")
        self.setObjectName("SettingsWindow")
        self.setWindowOpacity(0.90)
        self.setGeometry(150, 100, 250, 100)
        self.menu()
        self.show()

    def menu(self):
        formatTimeRow = QtWidgets.QListWidgetItem()
        shortFormatRadioButton = QtWidgets.QRadioButton(self)
        longFormatRadioButton = QtWidgets.QRadioButton(self)
        shortFormatRadioButton.setChecked(True)
        shortFormatRadioButton.toggled.connect(lambda: self.check_format(shortFormatRadioButton))
        longFormatRadioButton.toggled.connect(lambda: self.check_format(longFormatRadioButton))
        shortFormatRadioButton.setText("Default time format")
        longFormatRadioButton.setText("Show seconds")
        # shortFormatRadioButton.setGeometry(QtCore.QRect(20, 20, 20, 20))
        # longFormatRadioButton.setGeometry(QtCore.QRect(80, 20, 20, 20))
        mainItem = QtWidgets.QListWidgetItem('test')
        settingsLayout = QtWidgets.QVBoxLayout(self)
        settingsLayout.setObjectName('settingsLayout')
        settingsLayout.setContentsMargins(0, 0, 0, 0)
        timeHeading = QtWidgets.QLabel(self)
        timeHeading.setText('Time Widget Settings')
        timeHeading.setObjectName('timeHeading')
        # timeHeading.setGeometry(QtCore.QRect(15, 15, 10, 16))

        timeList = QtWidgets.QListWidget()

        formatTimeRow.setText("Format Time")
        timeList.addItem(formatTimeRow)

        settingsLayout.addWidget(timeHeading)
        settingsLayout.addWidget(shortFormatRadioButton)
        settingsLayout.addWidget(longFormatRadioButton)
        # settingsLayout.addWidget(timeList, 1)

    def check_format(self, b):
        if b.text() == "Default time format":
            if b.isChecked():
                main_window.Timer.timeDisplayFormat = True
            else:
                main_window.Timer.timeDisplayFormat = False

        if b.text() == "Show seconds":
            if b.isChecked():
                main_window.Timer.timeDisplayFormat = False
            else:
                main_window.Timer.timeDisplayFormat = True
