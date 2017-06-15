import os
import psutil
from PyQt5 import QtGui, QtCore, QtWidgets
from Controllers.Devices.device_controller import USBController
from Models.Devices.usb_devices import USBDevice


class DeviceWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(DeviceWidget, self).__init__(parent)
        self.usb1 = False
        self.usb2 = False
        self.usb3 = False
        self.setupUI()
        if self.usb1 is True:
            self.show()
        else:
            self.hide()

    def setupUI(self):
        widget_layout = QtWidgets.QVBoxLayout(self)
        widget_layout.setContentsMargins(0, 20, 0, 0)

        self.heading = QtWidgets.QLabel(self)
        self.heading.setText('Devices')
        self.usbDevice1 = QtWidgets.QLabel(self)
        self.usbDevice2 = QtWidgets.QLabel(self)
        self.usbDevice3 = QtWidgets.QLabel(self)

        self.lineSeperator = QtWidgets.QFrame()
        self.lineSeperator.setObjectName('lineSeperator')
        self.lineSeperator.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineSeperator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineSeperator.setGeometry(QtCore.QRect(20, 10, 8, 3))
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.get_usb_devices)
        timer.start(1000)
        widget_layout.addWidget(self.heading)
        widget_layout.addWidget(self.lineSeperator)
        widget_layout.addWidget(self.usbDevice1)
        if self.usb1 is not True:
            self.usbDevice1.hide()
        if self.usb2 is not False:
            self.usbDevice2.hide()
        if self.usb3 is not False:
            self.usbDevice3.hide()

    def get_usb_devices(self):
        usbDevices = USBController()
        listUsb = USBController().get_all_devices()
        print(len(listUsb))
        if len(listUsb) != 0:
            print(len(listUsb))
            self.show()
            if len(listUsb) == 1:

                for usb in listUsb:
                    if usb is not None:
                        self.usb1 = True
                        self.usbDevice1.show()
                        self.usbDevice1.setText(str(usb.iManufacturer) + " " + str(usb.idProduct) + " " + usb.bcdUSB)
                    else:
                        self.usb1 = False
                        self.usbDevice1.setText('')
                        self.usbDevice1.hide()
        elif len(listUsb) == 0:
            print('empty')
            self.usb1 = False
            self.usbDevice1.setText('')
            self.usbDevice1.hide()
            self.hide()
