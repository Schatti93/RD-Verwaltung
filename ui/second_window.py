# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\second_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_second_window(object):
    def setupUi(self, second_window):
        second_window.setObjectName("second_window")
        second_window.resize(1016, 653)
        second_window.setStyleSheet("background-color: rgb(128, 127, 129)")
        self.centralwidget = QtWidgets.QWidget(second_window)
        self.centralwidget.setObjectName("centralwidget")
        self.combobox_standard_url = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_standard_url.setGeometry(QtCore.QRect(20, 30, 311, 31))
        self.combobox_standard_url.setStyleSheet("QComboBox\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    selection-background-color: #111;\n"
"    selection-color: white;\n"
"    color: white;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"}\n"
"\n"
"\n"
"QComboBox:hover, QPushButton:hover\n"
"{\n"
"    border: 1px solid teal;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: red;\n"
"    color: pink;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 0px;\n"
"    padding-left: 0px;\n"
"    color: white;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: rgb(67, 131, 202);\n"
"}\n"
"\n"
"QComboBox:!on\n"
"{\n"
"    color: white;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #666, stop: 0.1 #555, stop: 0.5 #555, stop: 0.9 #444, stop: 1 #333);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    color: black;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #111, stop: 1 #333);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"     color: white;\n"
"     border-left-width: 1px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
"     padding-left: 10px;\n"
" }\n"
"\n"
"\n"
"")
        self.combobox_standard_url.setObjectName("combobox_standard_url")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 40, 131, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(760, 570, 112, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(880, 570, 112, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        second_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(second_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1016, 22))
        self.menubar.setObjectName("menubar")
        second_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(second_window)
        self.statusbar.setObjectName("statusbar")
        second_window.setStatusBar(self.statusbar)

        self.retranslateUi(second_window)
        QtCore.QMetaObject.connectSlotsByName(second_window)

    def retranslateUi(self, second_window):
        _translate = QtCore.QCoreApplication.translate
        second_window.setWindowTitle(_translate("second_window", "MainWindow"))
        self.label.setText(_translate("second_window", "Standard URL"))
        self.pushButton.setText(_translate("second_window", "Speichern"))
        self.pushButton_2.setText(_translate("second_window", "Abbrechen"))
