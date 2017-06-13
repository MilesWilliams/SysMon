import os
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from Views.MainWindow.main_window import Ui_MainWindow


def run():
    qss_file = open('styles.qss').read()
    app = QtWidgets.QApplication(sys.argv)
    # path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), "Icons/weathericon.png")
    # app.setWindowIcon(QtGui.QIcon(path))

    app.setStyleSheet(qss_file)
    main_window = Ui_MainWindow()
    main_window.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
    main_window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    main_window.setWindowOpacity(0.90)
    main_window.show()

    sys.exit(app.exec_())


run()
