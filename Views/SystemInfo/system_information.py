import os
import psutil
from PyQt5 import QtGui, QtCore, QtWidgets
from Models.SystemStats.system_stats import cpu_usage, ram_usage, available_memory, free_swap, total_hdd, free_hdd, get_open_apps, bytes2human
from Models.SystemStats.system_model import SystemModel
from Models.SystemStats.processes_model import ProcessModel
import matplotlib.pyplot as plt


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
        self.heading.setObjectName('systemHeading')
        self.system_table_view = QtWidgets.QTableView(self)
        self.system_table_view.setObjectName('systemTable')
        self.system_table_view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.system_table_view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.system_table_view.setShowGrid(False)
        self.system_table_view.setGridStyle(QtCore.Qt.NoPen)
        self.system_table_view.horizontalHeader().setVisible(False)
        self.system_table_view.horizontalHeader().setHighlightSections(False)
        self.system_table_view.verticalHeader().setVisible(False)
        self.system_table_view.verticalHeader().setHighlightSections(False)
        self.process_table_view = QtWidgets.QTableView(self)
        self.process_table_view.setObjectName('processTable')
        self.process_table_view.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.process_table_view.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.process_table_view.setShowGrid(False)
        self.process_table_view.setGridStyle(QtCore.Qt.NoPen)
        self.process_table_view.horizontalHeader().setVisible(False)
        self.process_table_view.horizontalHeader().setHighlightSections(False)
        self.process_table_view.verticalHeader().setVisible(False)
        self.process_table_view.verticalHeader().setHighlightSections(False)
        self.processHeading = QtWidgets.QLabel(self)
        self.processHeading.setObjectName('processHeading')
        self.processHeading.setText('Top 3 Running Process')
        self.cpuLabel = QtWidgets.QLabel(self)
        self.ramLabel = QtWidgets.QLabel(self)
        self.availableMemoryLabel = QtWidgets.QLabel(self)
        self.freeSwapLabel = QtWidgets.QLabel(self)
        self.topProcessLabel1 = QtWidgets.QLabel(self)
        self.topProcessLabel2 = QtWidgets.QLabel(self)
        self.topProcessLabel3 = QtWidgets.QLabel(self)
        self.freeHddLabel = QtWidgets.QLabel(self)
        QtGui.QFont.PreferFullHinting
        font = QtGui.QFont("Helvetica")
        font.setLetterSpacing(QtGui.QFont.PercentageSpacing, 400)
        # QtGui.QFont.setLetterSpacing(self, QtGui.QFont.SemiExpanded, 10.00)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.get_information)
        timer.timeout.connect(self.get_top_usuage_process)
        timer.start(500)
        widget_layout.addWidget(self.heading)
        widget_layout.addWidget(self.system_table_view)
        widget_layout.addWidget(self.processHeading)
        widget_layout.addWidget(self.process_table_view)

    def get_information(self):
        model = SystemModel([
            ['CPU :', cpu_usage()],
            ['RAM :', ram_usage()],
            ['Avail. Memory :', available_memory()],
            ['Free Swap :', free_swap()],
            ['Hdd  :', total_hdd()]
        ])

        self.system_table_view.setModel(model)

    def get_top_usuage_process(self):
        processList = get_open_apps()
        model = ProcessModel([
            [processList[0].name, str(round(processList[0].memory_percent, 2)) + '%'],
            [processList[1].name, str(round(processList[1].memory_percent, 2)) + '%'],
            [processList[2].name, str(round(processList[2].memory_percent, 2)) + '%']
        ])
        self.process_table_view.setModel(model)
