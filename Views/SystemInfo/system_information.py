import os
import psutil
from PyQt5 import QtGui, QtCore, QtWidgets
from Models.SystemStats.system_stats import cpu_usage, ram_usage, available_memory, free_swap, total_hdd, free_hdd, get_open_apps, bytes2human


class SystemInformation(QtWidgets.QWidget):
    def __init__(self, parent):
        super(SystemInformation, self).__init__(parent)

        self.setupUI()
        self.show()

    def setupUI(self):
        widget_layout = QtWidgets.QVBoxLayout(self)
        widget_layout.setContentsMargins(0, 20, 0, 0)
        self.heading = QtWidgets.QLabel(self)
        self.heading.setText('System')
        self.processHeading = QtWidgets.QLabel(self)
        self.processHeading.setText('Top 3 Running Process')
        self.cpuLabel = QtWidgets.QLabel(self)
        self.ramLabel = QtWidgets.QLabel(self)
        self.availableMemoryLabel = QtWidgets.QLabel(self)
        self.freeSwapLabel = QtWidgets.QLabel(self)
        self.topProcessLabel1 = QtWidgets.QLabel(self)
        self.topProcessLabel2 = QtWidgets.QLabel(self)
        self.topProcessLabel3 = QtWidgets.QLabel(self)
        self.freeHddLabel = QtWidgets.QLabel(self)
        self.lineSeperator = QtWidgets.QFrame()
        self.lineSeperator.setObjectName('lineSeperator')
        self.lineSeperator.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineSeperator.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineSeperator.setGeometry(QtCore.QRect(20, 10, 8, 3))
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.cpu_percent)
        timer.timeout.connect(self.ram_usage)
        timer.timeout.connect(self.available_memory)
        timer.timeout.connect(self.swap_space)
        timer.timeout.connect(self.hdd_stats)
        timer.timeout.connect(self.get_top_usuage_process)
        timer.start(1000)
        widget_layout.addWidget(self.heading)
        widget_layout.addWidget(self.lineSeperator)
        widget_layout.addWidget(self.cpuLabel)
        widget_layout.addWidget(self.ramLabel)
        widget_layout.addWidget(self.availableMemoryLabel)
        widget_layout.addWidget(self.freeSwapLabel)
        widget_layout.addWidget(self.freeHddLabel)
        widget_layout.addWidget(self.processHeading)
        widget_layout.addWidget(self.topProcessLabel1)
        widget_layout.addWidget(self.topProcessLabel2)
        widget_layout.addWidget(self.topProcessLabel3)

    def cpu_percent(self):
        self.cpuLabel.setText('CPU : {}%'.format(cpu_usage()))

    def ram_usage(self):
        self.ramLabel.setText('RAM : {}%'.format(ram_usage()))

    def available_memory(self):
        self.availableMemoryLabel.setText('Avail. VMemory : {}'.format(available_memory()))

    def swap_space(self):
        self.freeSwapLabel.setText('Free Swap : {}'.format(free_swap()))

    def hdd_stats(self):
        self.freeSwapLabel.setText('Hdd  : {}'.format(free_hdd()) + ' / {}'.format(total_hdd()))

    def get_top_usuage_process(self):
        processList = get_open_apps()
        self.topProcessLabel1.setText(processList[0].name + ' {}%'.format(round(processList[0].memory_percent, 2)))
        self.topProcessLabel2.setText(processList[1].name + ' {}%'.format(round(processList[1].memory_percent, 2)))
        self.topProcessLabel3.setText(processList[2].name + ' {}%'.format(round(processList[2].memory_percent, 2)))
