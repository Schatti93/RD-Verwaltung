# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1464, 936)
        MainWindow.setStyleSheet("background-color: rgb(128, 127, 129)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
"    \n"
"    background: white;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:top {\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:bottom {\n"
"    bottom: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:left {\n"
"    right: 1px;\n"
"}\n"
"\n"
"QTabWidget::tab-bar:right {\n"
"    left: 1px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
" border: 1px solid black;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"color: white;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #58AFB3, stop: 0.3 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);\n"
"    color: black;\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover {\n"
"    background: #999;\n"
"}\n"
"\n"
"QTabBar::tab:top:!selected {\n"
"    margin-top: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:!selected {\n"
"    margin-bottom: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:top, QTabBar::tab:bottom {\n"
"    min-width: 8ex;\n"
"    margin-right: -1px;\n"
"    padding: 5px 10px 5px 10px;\n"
"}\n"
"\n"
"QTabBar::tab:top:selected {\n"
"    border-bottom-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:bottom:selected {\n"
"    border-top-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:top:last, QTabBar::tab:bottom:last,\n"
"QTabBar::tab:top:only-one, QTabBar::tab:bottom:only-one {\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QTabBar::tab:left:!selected {\n"
"    margin-right: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:right:!selected {\n"
"    margin-left: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right {\n"
"    min-height: 8ex;\n"
"    margin-bottom: -1px;\n"
"    padding: 10px 5px 10px 5px;\n"
"}\n"
"\n"
"QTabBar::tab:left:selected {\n"
"    border-left-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:right:selected {\n"
"    border-right-color: none;\n"
"}\n"
"\n"
"QTabBar::tab:left:last, QTabBar::tab:right:last,\n"
"QTabBar::tab:left:only-one, QTabBar::tab:right:only-one {\n"
"    margin-bottom: 0;\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 4, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addLayout(self.verticalLayout, 4, 2, 1, 1)
        self.line_10 = QtWidgets.QFrame(self.tab_4)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout.addWidget(self.line_10, 4, 1, 1, 1)
        self.label_uebersicht_lager = QtWidgets.QLabel(self.tab_4)
        self.label_uebersicht_lager.setMaximumSize(QtCore.QSize(250, 30))
        self.label_uebersicht_lager.setObjectName("label_uebersicht_lager")
        self.gridLayout.addWidget(self.label_uebersicht_lager, 3, 0, 1, 1)
        self.uebersicht_lager_table = QtWidgets.QTableWidget(self.tab_4)
        self.uebersicht_lager_table.setMinimumSize(QtCore.QSize(0, 0))
        self.uebersicht_lager_table.setStyleSheet("QTableView {\n"
"border: 1px inset darkgrey;\n"
"border-radius: 5px;\n"
"padding: 0 8px;\n"
"font-size: 13px;\n"
"color: white;\n"
"gridline-color: rgb(164, 164, 165);\n"
"Background-color: rgb(164, 164, 165);\n"
"\n"
"}\n"
"QHeaderView::section{\n"
"\n"
"border-style: none;\n"
"Color: white;\n"
"gridline-color: rgb(164, 164, 165);\n"
"background-color: rgb(164, 164, 165);\n"
"border-bottom: 1px inset black;\n"
"\n"
"}\n"
"QTableView::item{\n"
"border-bottom : 1px inset black;\n"
"gridline-color: rgb(164, 164, 165);\n"
"text-align: center;\n"
"}")
        self.uebersicht_lager_table.setObjectName("uebersicht_lager_table")
        self.uebersicht_lager_table.setColumnCount(4)
        self.uebersicht_lager_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.uebersicht_lager_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.uebersicht_lager_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.uebersicht_lager_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.uebersicht_lager_table.setHorizontalHeaderItem(3, item)
        self.uebersicht_lager_table.horizontalHeader().setCascadingSectionResizes(True)
        self.uebersicht_lager_table.horizontalHeader().setDefaultSectionSize(147)
        self.uebersicht_lager_table.horizontalHeader().setMinimumSectionSize(110)
        self.uebersicht_lager_table.horizontalHeader().setStretchLastSection(False)
        self.uebersicht_lager_table.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.uebersicht_lager_table, 4, 0, 1, 1)
        self.line_11 = QtWidgets.QFrame(self.tab_4)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.gridLayout.addWidget(self.line_11, 2, 0, 1, 5)
        self.label_20 = QtWidgets.QLabel(self.tab_4)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 0, 2, 1, 1)
        self.line_9 = QtWidgets.QFrame(self.tab_4)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout.addWidget(self.line_9, 1, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.tab_4)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 0, 0, 1, 1)
        self.verticalLayout2 = QtWidgets.QVBoxLayout()
        self.verticalLayout2.setObjectName("verticalLayout2")
        self.gridLayout.addLayout(self.verticalLayout2, 4, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 5)
        self.line_4 = QtWidgets.QFrame(self.tab_4)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 4, 3, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 5, 0, 1, 1)
        self.label_einsatznummer = QtWidgets.QLabel(self.tab_3)
        self.label_einsatznummer.setObjectName("label_einsatznummer")
        self.gridLayout_4.addWidget(self.label_einsatznummer, 7, 0, 1, 1)
        self.lager_textfeld_produkt = QtWidgets.QLineEdit(self.tab_3)
        self.lager_textfeld_produkt.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.lager_textfeld_produkt.setObjectName("lager_textfeld_produkt")
        self.gridLayout_4.addWidget(self.lager_textfeld_produkt, 5, 1, 1, 6)
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 12, 2, 1, 1)
        self.lager_table = QtWidgets.QTableWidget(self.tab_3)
        self.lager_table.setStyleSheet("QTableView {\n"
"border: 1px solid black;\n"
"border-radius: 5px;\n"
"padding: 0 8px;\n"
"font-size: 13px;\n"
"color: white;\n"
"gridline-color: #807F81;\n"
"\n"
"}\n"
"QHeaderView::section{\n"
"border-style: none;\n"
"Color: white;\n"
"gridline-color: #807F81;\n"
"background-color: #807F81;\n"
"border-bottom: 1px solid black;\n"
"}\n"
"QTableView::item{\n"
"\n"
"\n"
"border-bottom : 1px solid black;\n"
"gridline-color: #807F81;\n"
"}")
        self.lager_table.setObjectName("lager_table")
        self.lager_table.setColumnCount(3)
        self.lager_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.lager_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lager_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.lager_table.setHorizontalHeaderItem(2, item)
        self.lager_table.horizontalHeader().setCascadingSectionResizes(True)
        self.lager_table.horizontalHeader().setDefaultSectionSize(100)
        self.lager_table.horizontalHeader().setStretchLastSection(False)
        self.lager_table.verticalHeader().setCascadingSectionResizes(True)
        self.gridLayout_4.addWidget(self.lager_table, 8, 1, 1, 6)
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 12, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 6, 0, 1, 1)
        self.lager_textfeld_einsatz = QtWidgets.QLineEdit(self.tab_3)
        self.lager_textfeld_einsatz.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.lager_textfeld_einsatz.setObjectName("lager_textfeld_einsatz")
        self.gridLayout_4.addWidget(self.lager_textfeld_einsatz, 7, 1, 1, 5)
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 0, 6, 1, 1)
        self.label_einsatznummer_enter = QtWidgets.QLabel(self.tab_3)
        self.label_einsatznummer_enter.setObjectName("label_einsatznummer_enter")
        self.gridLayout_4.addWidget(self.label_einsatznummer_enter, 7, 6, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 5)
        self.combobox_lager = QtWidgets.QComboBox(self.tab_3)
        self.combobox_lager.setStyleSheet("QComboBox\n"
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
        self.combobox_lager.setObjectName("combobox_lager")
        self.combobox_lager.addItem("")
        self.combobox_lager.addItem("")
        self.combobox_lager.addItem("")
        self.gridLayout_4.addWidget(self.combobox_lager, 3, 1, 1, 6)
        self.lager_btn = QtWidgets.QPushButton(self.tab_3)
        self.lager_btn.setStyleSheet("QPushButton{\n"
"   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid rgb(59, 204, 179);\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(130, 152, 152);\n"
"      border-style: solid;\n"
"    border: 1px solid #1EFFFF;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"\n"
"}")
        self.lager_btn.setObjectName("lager_btn")
        self.gridLayout_4.addWidget(self.lager_btn, 11, 3, 1, 3)
        self.lager_textfeld_menge = QtWidgets.QLineEdit(self.tab_3)
        self.lager_textfeld_menge.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.lager_textfeld_menge.setObjectName("lager_textfeld_menge")
        self.gridLayout_4.addWidget(self.lager_textfeld_menge, 6, 1, 1, 6)
        self.lager_error_label = QtWidgets.QLabel(self.tab_3)
        self.lager_error_label.setText("")
        self.lager_error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.lager_error_label.setObjectName("lager_error_label")
        self.gridLayout_4.addWidget(self.lager_error_label, 10, 3, 1, 3)
        self.line_3 = QtWidgets.QFrame(self.tab_3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_4.addWidget(self.line_3, 2, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_4, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem2, 1, 2, 1, 1)
        self.gridLayout_13.addLayout(self.gridLayout_10, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem3, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setMouseTracking(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout_9.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_9.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setStyleSheet("color: white")
        self.label_17.setObjectName("label_17")
        self.gridLayout_9.addWidget(self.label_17, 4, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem4, 6, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_9.addWidget(self.label_7, 2, 2, 1, 1)
        self.combo_zustand = QtWidgets.QComboBox(self.tab_2)
        self.combo_zustand.setStyleSheet("QComboBox\n"
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
        self.combo_zustand.setObjectName("combo_zustand")
        self.gridLayout_9.addWidget(self.combo_zustand, 3, 2, 1, 1)
        self.fahrzeug_textedit = QtWidgets.QTextEdit(self.tab_2)
        self.fahrzeug_textedit.setStyleSheet("QTextEdit {\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgb(107, 109, 108), stop: 0.3 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 5px;\n"
"padding: 0 8px;\n"
"font-size: 13px;\n"
"color: white;\n"
"gridline-color: #585759;\n"
"}")
        self.fahrzeug_textedit.setObjectName("fahrzeug_textedit")
        self.gridLayout_9.addWidget(self.fahrzeug_textedit, 5, 0, 1, 3)
        self.line_18 = QtWidgets.QFrame(self.tab_2)
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.gridLayout_9.addWidget(self.line_18, 1, 0, 1, 1)
        self.combo_rtw = QtWidgets.QComboBox(self.tab_2)
        self.combo_rtw.setStyleSheet("QComboBox\n"
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
        self.combo_rtw.setObjectName("combo_rtw")
        self.gridLayout_9.addWidget(self.combo_rtw, 3, 0, 1, 1)
        self.button_fahrzeuge = QtWidgets.QPushButton(self.tab_2)
        self.button_fahrzeuge.setStyleSheet("QPushButton{\n"
"   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid rgb(59, 204, 179);\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(130, 152, 152);\n"
"      border-style: solid;\n"
"    border: 1px solid #1EFFFF;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"\n"
"}")
        self.button_fahrzeuge.setObjectName("button_fahrzeuge")
        self.gridLayout_9.addWidget(self.button_fahrzeuge, 6, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem5, 7, 1, 1, 1)
        self.gridLayout_14.addLayout(self.gridLayout_9, 0, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem6, 0, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem7, 0, 2, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.line_8 = QtWidgets.QFrame(self.tab)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_2.addWidget(self.line_8, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 5, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.tab)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_2.addWidget(self.line_6, 2, 5, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 1, 6, 5, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 7, 1, 1)
        self.klamotten_tabelle = QtWidgets.QTableWidget(self.tab)
        self.klamotten_tabelle.setStyleSheet("QTableView {\n"
"border: 1px inset darkgrey;\n"
"border-radius: 5px;\n"
"padding: 0 8px;\n"
"font-size: 13px;\n"
"color: white;\n"
"gridline-color: rgb(164, 164, 165);\n"
"Background-color: rgb(164, 164, 165);\n"
"\n"
"}\n"
"QHeaderView::section{\n"
"\n"
"border-style: none;\n"
"Color: white;\n"
"gridline-color: rgb(164, 164, 165);\n"
"background-color: rgb(164, 164, 165);\n"
"border-bottom: 1px inset black;\n"
"\n"
"}\n"
"QTableView::item{\n"
"border-bottom : 1px inset black;\n"
"gridline-color: rgb(164, 164, 165);\n"
"text-align: center;\n"
"}")
        self.klamotten_tabelle.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.klamotten_tabelle.setColumnCount(2)
        self.klamotten_tabelle.setObjectName("klamotten_tabelle")
        self.klamotten_tabelle.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.klamotten_tabelle.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.klamotten_tabelle.setHorizontalHeaderItem(1, item)
        self.klamotten_tabelle.horizontalHeader().setCascadingSectionResizes(True)
        self.klamotten_tabelle.horizontalHeader().setDefaultSectionSize(99)
        self.klamotten_tabelle.horizontalHeader().setMinimumSectionSize(19)
        self.klamotten_tabelle.horizontalHeader().setStretchLastSection(False)
        self.klamotten_tabelle.verticalHeader().setVisible(False)
        self.klamotten_tabelle.verticalHeader().setDefaultSectionSize(30)
        self.gridLayout_2.addWidget(self.klamotten_tabelle, 4, 5, 2, 1)
        self.kleidung_zurueck_tabelle = QtWidgets.QTableWidget(self.tab)
        self.kleidung_zurueck_tabelle.setStyleSheet("QTableView {\n"
"border: 1px inset darkgrey;\n"
"border-radius: 5px;\n"
"padding: 0 8px;\n"
"font-size: 13px;\n"
"color: white;\n"
"gridline-color: rgb(164, 164, 165);\n"
"Background-color: rgb(164, 164, 165);\n"
"\n"
"}\n"
"QHeaderView::section{\n"
"\n"
"border-style: none;\n"
"Color: white;\n"
"gridline-color: rgb(164, 164, 165);\n"
"background-color: rgb(164, 164, 165);\n"
"border-bottom: 1px inset black;\n"
"\n"
"}\n"
"QTableView::item{\n"
"border-bottom : 1px inset black;\n"
"gridline-color: rgb(164, 164, 165);\n"
"text-align: center;\n"
"}")
        self.kleidung_zurueck_tabelle.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.kleidung_zurueck_tabelle.setObjectName("kleidung_zurueck_tabelle")
        self.kleidung_zurueck_tabelle.setColumnCount(2)
        self.kleidung_zurueck_tabelle.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.kleidung_zurueck_tabelle.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.kleidung_zurueck_tabelle.setHorizontalHeaderItem(1, item)
        self.kleidung_zurueck_tabelle.horizontalHeader().setCascadingSectionResizes(True)
        self.kleidung_zurueck_tabelle.horizontalHeader().setDefaultSectionSize(99)
        self.kleidung_zurueck_tabelle.horizontalHeader().setHighlightSections(True)
        self.kleidung_zurueck_tabelle.horizontalHeader().setStretchLastSection(False)
        self.kleidung_zurueck_tabelle.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.kleidung_zurueck_tabelle, 4, 7, 2, 1)
        self.klamotten_button = QtWidgets.QPushButton(self.tab)
        self.klamotten_button.setMaximumSize(QtCore.QSize(120, 30))
        self.klamotten_button.setStyleSheet("QPushButton{\n"
"   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid rgb(59, 204, 179);\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(130, 152, 152);\n"
"      border-style: solid;\n"
"    border: 1px solid #1EFFFF;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"\n"
"}")
        self.klamotten_button.setObjectName("klamotten_button")
        self.gridLayout_2.addWidget(self.klamotten_button, 6, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setStyleSheet("color: white;")
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 5, 1, 1)
        self.aufnahme = QtWidgets.QTableWidget(self.tab)
        self.aufnahme.setMinimumSize(QtCore.QSize(0, 0))
        self.aufnahme.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.aufnahme.setStyleSheet("QTableView {\n"
"border: 1px inset darkgrey;\n"
"border-radius: 5px;\n"
"padding: 0 8px;\n"
"font-size: 13px;\n"
"color: white;\n"
"gridline-color: rgb(164, 164, 165);\n"
"Background-color: rgb(164, 164, 165);\n"
"\n"
"}\n"
"QHeaderView::section{\n"
"\n"
"border-style: none;\n"
"Color: white;\n"
"gridline-color: rgb(164, 164, 165);\n"
"background-color: rgb(164, 164, 165);\n"
"border-bottom: 1px inset black;\n"
"\n"
"}\n"
"QTableView::item{\n"
"border-bottom : 1px inset black;\n"
"gridline-color: rgb(164, 164, 165);\n"
"text-align: center;\n"
"}")
        self.aufnahme.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.aufnahme.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.aufnahme.setAutoScroll(False)
        self.aufnahme.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.aufnahme.setObjectName("aufnahme")
        self.aufnahme.setColumnCount(1)
        self.aufnahme.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.aufnahme.setHorizontalHeaderItem(0, item)
        self.aufnahme.horizontalHeader().setCascadingSectionResizes(False)
        self.aufnahme.horizontalHeader().setDefaultSectionSize(320)
        self.aufnahme.horizontalHeader().setStretchLastSection(True)
        self.aufnahme.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.aufnahme, 5, 0, 1, 4)
        self.line_5 = QtWidgets.QFrame(self.tab)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_2.addWidget(self.line_5, 1, 4, 5, 1)
        self.klamotten_textfeld = QtWidgets.QLineEdit(self.tab)
        self.klamotten_textfeld.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.klamotten_textfeld.setObjectName("klamotten_textfeld")
        self.gridLayout_2.addWidget(self.klamotten_textfeld, 3, 0, 1, 3)
        self.gridLayout_15.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.admin_login = QtWidgets.QGridLayout()
        self.admin_login.setObjectName("admin_login")
        self.admin_text_pw = QtWidgets.QLineEdit(self.tab_5)
        self.admin_text_pw.setMaximumSize(QtCore.QSize(300, 16777215))
        self.admin_text_pw.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.admin_text_pw.setObjectName("admin_text_pw")
        self.admin_login.addWidget(self.admin_text_pw, 2, 1, 1, 1)
        self.passwort_label = QtWidgets.QLabel(self.tab_5)
        self.passwort_label.setObjectName("passwort_label")
        self.admin_login.addWidget(self.passwort_label, 2, 2, 1, 1)
        self.admin_text_ben = QtWidgets.QLineEdit(self.tab_5)
        self.admin_text_ben.setMaximumSize(QtCore.QSize(300, 16777215))
        self.admin_text_ben.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.admin_text_ben.setObjectName("admin_text_ben")
        self.admin_login.addWidget(self.admin_text_ben, 1, 1, 1, 1)
        self.admin_bereich = QtWidgets.QTabWidget(self.tab_5)
        self.admin_bereich.setTabPosition(QtWidgets.QTabWidget.North)
        self.admin_bereich.setObjectName("admin_bereich")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_6)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.tab_9)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem8, 15, 1, 1, 1)
        self.admin_new_prod_inhalt_menge = QtWidgets.QLineEdit(self.tab_9)
        self.admin_new_prod_inhalt_menge.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.admin_new_prod_inhalt_menge.setObjectName("admin_new_prod_inhalt_menge")
        self.gridLayout_5.addWidget(self.admin_new_prod_inhalt_menge, 8, 0, 1, 2)
        self.label_35 = QtWidgets.QLabel(self.tab_9)
        self.label_35.setObjectName("label_35")
        self.gridLayout_5.addWidget(self.label_35, 12, 0, 1, 3)
        self.label_24 = QtWidgets.QLabel(self.tab_9)
        self.label_24.setObjectName("label_24")
        self.gridLayout_5.addWidget(self.label_24, 4, 2, 1, 1)
        self.admin_new_prod_label = QtWidgets.QLabel(self.tab_9)
        self.admin_new_prod_label.setText("")
        self.admin_new_prod_label.setObjectName("admin_new_prod_label")
        self.gridLayout_5.addWidget(self.admin_new_prod_label, 14, 2, 1, 1)
        self.label24 = QtWidgets.QLabel(self.tab_9)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label24.setFont(font)
        self.label24.setObjectName("label24")
        self.gridLayout_5.addWidget(self.label24, 1, 0, 1, 1)
        self.admin_new_prod_bes = QtWidgets.QLineEdit(self.tab_9)
        self.admin_new_prod_bes.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.admin_new_prod_bes.setObjectName("admin_new_prod_bes")
        self.gridLayout_5.addWidget(self.admin_new_prod_bes, 4, 0, 1, 2)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem9, 15, 3, 1, 1)
        self.line_12 = QtWidgets.QFrame(self.tab_9)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.gridLayout_5.addWidget(self.line_12, 2, 0, 1, 1)
        self.admin_new_prod_table = QtWidgets.QTableWidget(self.tab_9)
        self.admin_new_prod_table.setStyleSheet("QTableView {\n"
"border: 1px inset darkgrey;\n"
"border-radius: 5px;\n"
"padding: 0 8px;\n"
"font-size: 13px;\n"
"color: white;\n"
"gridline-color: rgb(164, 164, 165);\n"
"Background-color: rgb(164, 164, 165);\n"
"\n"
"}\n"
"QHeaderView::section{\n"
"\n"
"border-style: none;\n"
"Color: white;\n"
"gridline-color: rgb(164, 164, 165);\n"
"background-color: rgb(164, 164, 165);\n"
"border-bottom: 1px solid black;\n"
"\n"
"}\n"
"QTableView::item{\n"
"border-bottom : 1px solid black;\n"
"gridline-color: rgb(164, 164, 165);\n"
"text-align: center;\n"
"}")
        self.admin_new_prod_table.setObjectName("admin_new_prod_table")
        self.admin_new_prod_table.setColumnCount(7)
        self.admin_new_prod_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.admin_new_prod_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_new_prod_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_new_prod_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_new_prod_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_new_prod_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_new_prod_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_new_prod_table.setHorizontalHeaderItem(6, item)
        self.admin_new_prod_table.horizontalHeader().setCascadingSectionResizes(True)
        self.admin_new_prod_table.horizontalHeader().setDefaultSectionSize(135)
        self.admin_new_prod_table.horizontalHeader().setMinimumSectionSize(135)
        self.admin_new_prod_table.horizontalHeader().setStretchLastSection(False)
        self.admin_new_prod_table.verticalHeader().setVisible(False)
        self.gridLayout_5.addWidget(self.admin_new_prod_table, 13, 0, 1, 5)
        self.label_36 = QtWidgets.QLabel(self.tab_9)
        self.label_36.setObjectName("label_36")
        self.gridLayout_5.addWidget(self.label_36, 8, 2, 1, 1)
        self.admin_new_prod_min = QtWidgets.QLineEdit(self.tab_9)
        self.admin_new_prod_min.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.admin_new_prod_min.setObjectName("admin_new_prod_min")
        self.gridLayout_5.addWidget(self.admin_new_prod_min, 5, 0, 1, 2)
        self.admin_new_prod_max = QtWidgets.QLineEdit(self.tab_9)
        self.admin_new_prod_max.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.admin_new_prod_max.setObjectName("admin_new_prod_max")
        self.gridLayout_5.addWidget(self.admin_new_prod_max, 6, 0, 1, 2)
        self.admin_new_prod_prod = QtWidgets.QLineEdit(self.tab_9)
        self.admin_new_prod_prod.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.admin_new_prod_prod.setObjectName("admin_new_prod_prod")
        self.gridLayout_5.addWidget(self.admin_new_prod_prod, 3, 0, 1, 2)
        self.admin_new_prod_bar = QtWidgets.QLineEdit(self.tab_9)
        self.admin_new_prod_bar.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.admin_new_prod_bar.setObjectName("admin_new_prod_bar")
        self.gridLayout_5.addWidget(self.admin_new_prod_bar, 7, 0, 1, 2)
        self.label_27 = QtWidgets.QLabel(self.tab_9)
        self.label_27.setObjectName("label_27")
        self.gridLayout_5.addWidget(self.label_27, 7, 2, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.tab_9)
        self.label_39.setObjectName("label_39")
        self.gridLayout_5.addWidget(self.label_39, 10, 2, 1, 1)
        self.admin_new_prod_btn = QtWidgets.QPushButton(self.tab_9)
        self.admin_new_prod_btn.setStyleSheet("QPushButton{\n"
"   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid rgb(59, 204, 179);\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(130, 152, 152);\n"
"      border-style: solid;\n"
"    border: 1px solid #1EFFFF;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"\n"
"}")
        self.admin_new_prod_btn.setObjectName("admin_new_prod_btn")
        self.gridLayout_5.addWidget(self.admin_new_prod_btn, 15, 2, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.tab_9)
        self.label_23.setObjectName("label_23")
        self.gridLayout_5.addWidget(self.label_23, 3, 2, 1, 1)
        self.admin_new_prod_artikel = QtWidgets.QLineEdit(self.tab_9)
        self.admin_new_prod_artikel.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.admin_new_prod_artikel.setObjectName("admin_new_prod_artikel")
        self.gridLayout_5.addWidget(self.admin_new_prod_artikel, 10, 0, 1, 2)
        self.label_26 = QtWidgets.QLabel(self.tab_9)
        self.label_26.setObjectName("label_26")
        self.gridLayout_5.addWidget(self.label_26, 6, 2, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.tab_9)
        self.label_25.setObjectName("label_25")
        self.gridLayout_5.addWidget(self.label_25, 5, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.tab_9)
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.gridLayout_5.addWidget(self.label_16, 11, 2, 1, 1)
        self.gridLayout_23.addLayout(self.gridLayout_5, 1, 0, 1, 1)
        self.admin_logout_btn = QtWidgets.QPushButton(self.tab_9)
        self.admin_logout_btn.setMaximumSize(QtCore.QSize(100, 30))
        self.admin_logout_btn.setStyleSheet("QPushButton{\n"
"   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid rgb(59, 204, 179);\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(130, 152, 152);\n"
"      border-style: solid;\n"
"    border: 1px solid #1EFFFF;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"\n"
"}")
        self.admin_logout_btn.setObjectName("admin_logout_btn")
        self.gridLayout_23.addWidget(self.admin_logout_btn, 0, 0, 1, 1)
        self.line_15 = QtWidgets.QFrame(self.tab_9)
        self.line_15.setStyleSheet("")
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.gridLayout_23.addWidget(self.line_15, 1, 1, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_29 = QtWidgets.QLabel(self.tab_9)
        self.label_29.setObjectName("label_29")
        self.gridLayout_6.addWidget(self.label_29, 4, 2, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.tab_9)
        self.label_31.setObjectName("label_31")
        self.gridLayout_6.addWidget(self.label_31, 3, 0, 1, 2)
        self.label_30 = QtWidgets.QLabel(self.tab_9)
        self.label_30.setObjectName("label_30")
        self.gridLayout_6.addWidget(self.label_30, 5, 2, 1, 1)
        self.admin_del_prod_bar = QtWidgets.QLineEdit(self.tab_9)
        self.admin_del_prod_bar.setMaximumSize(QtCore.QSize(400, 16777215))
        self.admin_del_prod_bar.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.admin_del_prod_bar.setObjectName("admin_del_prod_bar")
        self.gridLayout_6.addWidget(self.admin_del_prod_bar, 5, 0, 1, 2)
        self.admin_del_prod_table = QtWidgets.QTableWidget(self.tab_9)
        self.admin_del_prod_table.setMaximumSize(QtCore.QSize(500, 16777215))
        self.admin_del_prod_table.setStyleSheet("QTableView {\n"
"border: 1px inset darkgrey;\n"
"border-radius: 5px;\n"
"padding: 0 8px;\n"
"font-size: 13px;\n"
"color: white;\n"
"gridline-color: rgb(164, 164, 165);\n"
"Background-color: rgb(164, 164, 165);\n"
"\n"
"}\n"
"QHeaderView::section{\n"
"\n"
"border-style: none;\n"
"Color: white;\n"
"gridline-color: rgb(164, 164, 165);\n"
"background-color: rgb(164, 164, 165);\n"
"border-bottom: 1px inset black;\n"
"\n"
"}\n"
"QTableView::item{\n"
"border-bottom : 1px inset black;\n"
"gridline-color: rgb(164, 164, 165);\n"
"text-align: center;\n"
"}")
        self.admin_del_prod_table.setObjectName("admin_del_prod_table")
        self.admin_del_prod_table.setColumnCount(2)
        self.admin_del_prod_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.admin_del_prod_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_del_prod_table.setHorizontalHeaderItem(1, item)
        self.admin_del_prod_table.horizontalHeader().setCascadingSectionResizes(True)
        self.admin_del_prod_table.horizontalHeader().setStretchLastSection(False)
        self.admin_del_prod_table.verticalHeader().setVisible(False)
        self.gridLayout_6.addWidget(self.admin_del_prod_table, 7, 0, 1, 3)
        self.label_28 = QtWidgets.QLabel(self.tab_9)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.gridLayout_6.addWidget(self.label_28, 1, 0, 1, 1)
        self.admin_del_prod_prod = QtWidgets.QLineEdit(self.tab_9)
        self.admin_del_prod_prod.setMaximumSize(QtCore.QSize(400, 16777215))
        self.admin_del_prod_prod.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.admin_del_prod_prod.setObjectName("admin_del_prod_prod")
        self.gridLayout_6.addWidget(self.admin_del_prod_prod, 4, 0, 1, 2)
        self.admin_lager_loeschen_error = QtWidgets.QLabel(self.tab_9)
        self.admin_lager_loeschen_error.setText("")
        self.admin_lager_loeschen_error.setObjectName("admin_lager_loeschen_error")
        self.gridLayout_6.addWidget(self.admin_lager_loeschen_error, 6, 1, 1, 1)
        self.admin_del_prod_btn = QtWidgets.QPushButton(self.tab_9)
        self.admin_del_prod_btn.setMinimumSize(QtCore.QSize(172, 0))
        self.admin_del_prod_btn.setMaximumSize(QtCore.QSize(80, 16777215))
        self.admin_del_prod_btn.setStyleSheet("QPushButton{\n"
"   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid rgb(59, 204, 179);\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(130, 152, 152);\n"
"      border-style: solid;\n"
"    border: 1px solid #1EFFFF;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"\n"
"}")
        self.admin_del_prod_btn.setObjectName("admin_del_prod_btn")
        self.gridLayout_6.addWidget(self.admin_del_prod_btn, 9, 1, 1, 1)
        self.admin_del_prod_label = QtWidgets.QLabel(self.tab_9)
        self.admin_del_prod_label.setText("")
        self.admin_del_prod_label.setObjectName("admin_del_prod_label")
        self.gridLayout_6.addWidget(self.admin_del_prod_label, 8, 1, 1, 1)
        self.line_13 = QtWidgets.QFrame(self.tab_9)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.gridLayout_6.addWidget(self.line_13, 2, 0, 1, 1)
        self.gridLayout_23.addLayout(self.gridLayout_6, 1, 2, 1, 1)
        self.tabWidget_2.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.tab_10)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.pdf_erstellen = QtWidgets.QPushButton(self.tab_10)
        self.pdf_erstellen.setStyleSheet("QPushButton{\n"
"   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid rgb(59, 204, 179);\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(130, 152, 152);\n"
"      border-style: solid;\n"
"    border: 1px solid #1EFFFF;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"\n"
"}")
        self.pdf_erstellen.setObjectName("pdf_erstellen")
        self.gridLayout_8.addWidget(self.pdf_erstellen, 10, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.tab_10)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_8.addWidget(self.line, 1, 3, 1, 1)
        self.Bestellung_speichern = QtWidgets.QPushButton(self.tab_10)
        self.Bestellung_speichern.setMinimumSize(QtCore.QSize(172, 0))
        self.Bestellung_speichern.setMaximumSize(QtCore.QSize(150, 16777215))
        self.Bestellung_speichern.setStyleSheet("QPushButton{\n"
"   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid rgb(59, 204, 179);\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(130, 152, 152);\n"
"      border-style: solid;\n"
"    border: 1px solid #1EFFFF;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"\n"
"}")
        self.Bestellung_speichern.setObjectName("Bestellung_speichern")
        self.gridLayout_8.addWidget(self.Bestellung_speichern, 10, 3, 1, 1)
        self.combo_bestell_status = QtWidgets.QComboBox(self.tab_10)
        self.combo_bestell_status.setMinimumSize(QtCore.QSize(200, 0))
        self.combo_bestell_status.setMaximumSize(QtCore.QSize(200, 16777215))
        self.combo_bestell_status.setStyleSheet("QComboBox\n"
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
        self.combo_bestell_status.setObjectName("combo_bestell_status")
        self.gridLayout_8.addWidget(self.combo_bestell_status, 4, 2, 1, 1)
        self.button_bestellung_vor = QtWidgets.QPushButton(self.tab_10)
        self.button_bestellung_vor.setMaximumSize(QtCore.QSize(200, 16777215))
        self.button_bestellung_vor.setStyleSheet("QPushButton{\n"
"   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid rgb(59, 204, 179);\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(130, 152, 152);\n"
"      border-style: solid;\n"
"    border: 1px solid #1EFFFF;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"\n"
"}")
        self.button_bestellung_vor.setObjectName("button_bestellung_vor")
        self.gridLayout_8.addWidget(self.button_bestellung_vor, 5, 2, 1, 1)
        self.lager_bestellung = QtWidgets.QPushButton(self.tab_10)
        self.lager_bestellung.setStyleSheet("QPushButton{\n"
"   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid rgb(59, 204, 179);\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(130, 152, 152);\n"
"      border-style: solid;\n"
"    border: 1px solid #1EFFFF;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"\n"
"}")
        self.lager_bestellung.setObjectName("lager_bestellung")
        self.gridLayout_8.addWidget(self.lager_bestellung, 10, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.tab_10)
        self.label_21.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_21.setObjectName("label_21")
        self.gridLayout_8.addWidget(self.label_21, 0, 3, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.tab_10)
        self.label_40.setObjectName("label_40")
        self.gridLayout_8.addWidget(self.label_40, 0, 0, 1, 1)
        self.button_bestellung_zurueck = QtWidgets.QPushButton(self.tab_10)
        self.button_bestellung_zurueck.setMaximumSize(QtCore.QSize(200, 16777215))
        self.button_bestellung_zurueck.setStyleSheet("QPushButton{\n"
"   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid rgb(59, 204, 179);\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(130, 152, 152);\n"
"      border-style: solid;\n"
"    border: 1px solid #1EFFFF;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"\n"
"}")
        self.button_bestellung_zurueck.setObjectName("button_bestellung_zurueck")
        self.gridLayout_8.addWidget(self.button_bestellung_zurueck, 7, 2, 1, 1)
        self.line_17 = QtWidgets.QFrame(self.tab_10)
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.gridLayout_8.addWidget(self.line_17, 1, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem10, 6, 2, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem11, 2, 2, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem12, 8, 2, 1, 1)
        self.admin_lager_fehlendes_material = QtWidgets.QTableWidget(self.tab_10)
        self.admin_lager_fehlendes_material.setEnabled(True)
        self.admin_lager_fehlendes_material.setMinimumSize(QtCore.QSize(650, 200))
        self.admin_lager_fehlendes_material.setStyleSheet("QTableView {\n"
"border: 1px inset darkgrey;\n"
"border-radius: 5px;\n"
"padding: 0 8px;\n"
"font-size: 13px;\n"
"color: white;\n"
"gridline-color: rgb(164, 164, 165);\n"
"Background-color: rgb(164, 164, 165);\n"
"\n"
"}\n"
"QHeaderView::section{\n"
"\n"
"border-style: none;\n"
"Color: white;\n"
"gridline-color: rgb(164, 164, 165);\n"
"background-color: rgb(164, 164, 165);\n"
"border-bottom: 1px inset black;\n"
"\n"
"}\n"
"QTableView::item{\n"
"border-bottom : 1px inset black;\n"
"gridline-color: rgb(164, 164, 165);\n"
"text-align: center;\n"
"}")
        self.admin_lager_fehlendes_material.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.admin_lager_fehlendes_material.setObjectName("admin_lager_fehlendes_material")
        self.admin_lager_fehlendes_material.setColumnCount(5)
        self.admin_lager_fehlendes_material.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.admin_lager_fehlendes_material.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_lager_fehlendes_material.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_lager_fehlendes_material.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_lager_fehlendes_material.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_lager_fehlendes_material.setHorizontalHeaderItem(4, item)
        self.admin_lager_fehlendes_material.horizontalHeader().setCascadingSectionResizes(True)
        self.admin_lager_fehlendes_material.horizontalHeader().setDefaultSectionSize(122)
        self.admin_lager_fehlendes_material.horizontalHeader().setMinimumSectionSize(122)
        self.admin_lager_fehlendes_material.horizontalHeader().setStretchLastSection(False)
        self.admin_lager_fehlendes_material.verticalHeader().setVisible(False)
        self.gridLayout_8.addWidget(self.admin_lager_fehlendes_material, 2, 0, 7, 2)
        self.table_bestellt = QtWidgets.QTableWidget(self.tab_10)
        self.table_bestellt.setMinimumSize(QtCore.QSize(400, 0))
        self.table_bestellt.setStyleSheet("QTableView {\n"
"border: 1px inset darkgrey;\n"
"border-radius: 5px;\n"
"padding: 0 8px;\n"
"font-size: 13px;\n"
"color: white;\n"
"gridline-color: rgb(164, 164, 165);\n"
"Background-color: rgb(164, 164, 165);\n"
"\n"
"}\n"
"QHeaderView::section{\n"
"\n"
"border-style: none;\n"
"Color: white;\n"
"gridline-color: rgb(164, 164, 165);\n"
"background-color: rgb(164, 164, 165);\n"
"border-bottom: 1px inset black;\n"
"\n"
"}\n"
"QTableView::item{\n"
"border-bottom : 1px inset black;\n"
"gridline-color: rgb(164, 164, 165);\n"
"text-align: center;\n"
"}")
        self.table_bestellt.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_bestellt.setObjectName("table_bestellt")
        self.table_bestellt.setColumnCount(2)
        self.table_bestellt.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_bestellt.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_bestellt.setHorizontalHeaderItem(1, item)
        self.table_bestellt.horizontalHeader().setCascadingSectionResizes(True)
        self.table_bestellt.horizontalHeader().setMinimumSectionSize(180)
        self.table_bestellt.horizontalHeader().setStretchLastSection(False)
        self.table_bestellt.verticalHeader().setVisible(False)
        self.gridLayout_8.addWidget(self.table_bestellt, 2, 3, 7, 1)
        self.gridLayout_24.addLayout(self.gridLayout_8, 0, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_24.addItem(spacerItem13, 0, 2, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_24.addItem(spacerItem14, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_10, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.tab_11)
        self.gridLayout_21.setObjectName("gridLayout_21")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_21.addItem(spacerItem15, 0, 2, 1, 1)
        self.gridLayout_20 = QtWidgets.QGridLayout()
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.label_41 = QtWidgets.QLabel(self.tab_11)
        self.label_41.setObjectName("label_41")
        self.gridLayout_20.addWidget(self.label_41, 1, 3, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.tab_11)
        self.label_37.setObjectName("label_37")
        self.gridLayout_20.addWidget(self.label_37, 0, 3, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.tab_11)
        self.label_42.setObjectName("label_42")
        self.gridLayout_20.addWidget(self.label_42, 2, 3, 1, 1)
        self.admin_material_speichern_button = QtWidgets.QPushButton(self.tab_11)
        self.admin_material_speichern_button.setStyleSheet("QPushButton{\n"
"   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid rgb(59, 204, 179);\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(130, 152, 152);\n"
"      border-style: solid;\n"
"    border: 1px solid #1EFFFF;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"\n"
"}")
        self.admin_material_speichern_button.setObjectName("admin_material_speichern_button")
        self.gridLayout_20.addWidget(self.admin_material_speichern_button, 4, 2, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_20.addItem(spacerItem16, 4, 0, 1, 1)
        self.admin_material_speichern_table = QtWidgets.QTableWidget(self.tab_11)
        self.admin_material_speichern_table.setStyleSheet("QTableView {\n"
"border: 1px inset darkgrey;\n"
"border-radius: 5px;\n"
"padding: 0 8px;\n"
"font-size: 13px;\n"
"color: white;\n"
"gridline-color: rgb(164, 164, 165);\n"
"Background-color: rgb(164, 164, 165);\n"
"\n"
"}\n"
"QHeaderView::section{\n"
"\n"
"border-style: none;\n"
"Color: white;\n"
"gridline-color: rgb(164, 164, 165);\n"
"background-color: rgb(164, 164, 165);\n"
"border-bottom: 1px inset black;\n"
"\n"
"}\n"
"QTableView::item{\n"
"border-bottom : 1px inset black;\n"
"gridline-color: rgb(164, 164, 165);\n"
"text-align: center;\n"
"}")
        self.admin_material_speichern_table.setObjectName("admin_material_speichern_table")
        self.admin_material_speichern_table.setColumnCount(2)
        self.admin_material_speichern_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.admin_material_speichern_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_material_speichern_table.setHorizontalHeaderItem(1, item)
        self.admin_material_speichern_table.horizontalHeader().setCascadingSectionResizes(True)
        self.admin_material_speichern_table.horizontalHeader().setDefaultSectionSize(200)
        self.admin_material_speichern_table.horizontalHeader().setStretchLastSection(False)
        self.admin_material_speichern_table.verticalHeader().setVisible(False)
        self.gridLayout_20.addWidget(self.admin_material_speichern_table, 3, 0, 1, 4)
        self.admin_material_speichern_combo = QtWidgets.QComboBox(self.tab_11)
        self.admin_material_speichern_combo.setStyleSheet("QComboBox\n"
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
        self.admin_material_speichern_combo.setObjectName("admin_material_speichern_combo")
        self.gridLayout_20.addWidget(self.admin_material_speichern_combo, 2, 0, 1, 3)
        self.admin_material_speichern_anzahl = QtWidgets.QLineEdit(self.tab_11)
        self.admin_material_speichern_anzahl.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.admin_material_speichern_anzahl.setObjectName("admin_material_speichern_anzahl")
        self.gridLayout_20.addWidget(self.admin_material_speichern_anzahl, 1, 0, 1, 3)
        self.admin_material_speichern_barcode = QtWidgets.QLineEdit(self.tab_11)
        self.admin_material_speichern_barcode.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.admin_material_speichern_barcode.setObjectName("admin_material_speichern_barcode")
        self.gridLayout_20.addWidget(self.admin_material_speichern_barcode, 0, 0, 1, 3)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_20.addItem(spacerItem17, 4, 3, 1, 1)
        self.gridLayout_21.addLayout(self.gridLayout_20, 0, 1, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_21.addItem(spacerItem18, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_11, "")
        self.gridLayout_17.addWidget(self.tabWidget_2, 0, 0, 2, 1)
        self.admin_bereich.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.tab_7)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.fahrzeug_admin_error_label = QtWidgets.QLabel(self.tab_7)
        self.fahrzeug_admin_error_label.setText("")
        self.fahrzeug_admin_error_label.setObjectName("fahrzeug_admin_error_label")
        self.gridLayout_7.addWidget(self.fahrzeug_admin_error_label, 9, 1, 1, 1)
        self.fahrzeug_admin_kennz = QtWidgets.QLineEdit(self.tab_7)
        self.fahrzeug_admin_kennz.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.fahrzeug_admin_kennz.setObjectName("fahrzeug_admin_kennz")
        self.gridLayout_7.addWidget(self.fahrzeug_admin_kennz, 5, 0, 1, 2)
        self.label_33 = QtWidgets.QLabel(self.tab_7)
        self.label_33.setObjectName("label_33")
        self.gridLayout_7.addWidget(self.label_33, 5, 2, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.tab_7)
        self.label_38.setObjectName("label_38")
        self.gridLayout_7.addWidget(self.label_38, 8, 2, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.tab_7)
        self.label_32.setObjectName("label_32")
        self.gridLayout_7.addWidget(self.label_32, 4, 2, 1, 1)
        self.fahrzeug_admin_ort = QtWidgets.QLineEdit(self.tab_7)
        self.fahrzeug_admin_ort.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.fahrzeug_admin_ort.setObjectName("fahrzeug_admin_ort")
        self.gridLayout_7.addWidget(self.fahrzeug_admin_ort, 6, 0, 1, 2)
        self.label_22 = QtWidgets.QLabel(self.tab_7)
        self.label_22.setObjectName("label_22")
        self.gridLayout_7.addWidget(self.label_22, 2, 0, 1, 1)
        self.line_14 = QtWidgets.QFrame(self.tab_7)
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.gridLayout_7.addWidget(self.line_14, 3, 0, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.tab_7)
        self.label_34.setObjectName("label_34")
        self.gridLayout_7.addWidget(self.label_34, 6, 2, 1, 1)
        self.fahrzeug_admin_tuev = QtWidgets.QLineEdit(self.tab_7)
        self.fahrzeug_admin_tuev.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.fahrzeug_admin_tuev.setObjectName("fahrzeug_admin_tuev")
        self.gridLayout_7.addWidget(self.fahrzeug_admin_tuev, 8, 0, 1, 2)
        self.fahrzeug_admin_funkkenn = QtWidgets.QLineEdit(self.tab_7)
        self.fahrzeug_admin_funkkenn.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.fahrzeug_admin_funkkenn.setObjectName("fahrzeug_admin_funkkenn")
        self.gridLayout_7.addWidget(self.fahrzeug_admin_funkkenn, 4, 0, 1, 2)
        self.fahrzeug_admin_save_btn = QtWidgets.QPushButton(self.tab_7)
        self.fahrzeug_admin_save_btn.setStyleSheet("QPushButton{\n"
"   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid rgb(59, 204, 179);\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(130, 152, 152);\n"
"      border-style: solid;\n"
"    border: 1px solid #1EFFFF;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"\n"
"}")
        self.fahrzeug_admin_save_btn.setObjectName("fahrzeug_admin_save_btn")
        self.gridLayout_7.addWidget(self.fahrzeug_admin_save_btn, 10, 1, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem19, 11, 1, 1, 1)
        self.gridLayout_18.addLayout(self.gridLayout_7, 1, 1, 1, 1)
        self.admin_logout_btn_2 = QtWidgets.QPushButton(self.tab_7)
        self.admin_logout_btn_2.setMaximumSize(QtCore.QSize(100, 30))
        self.admin_logout_btn_2.setStyleSheet("QPushButton{\n"
"   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid rgb(59, 204, 179);\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(130, 152, 152);\n"
"      border-style: solid;\n"
"    border: 1px solid #1EFFFF;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"\n"
"}")
        self.admin_logout_btn_2.setObjectName("admin_logout_btn_2")
        self.gridLayout_18.addWidget(self.admin_logout_btn_2, 0, 0, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_18.addItem(spacerItem20, 1, 0, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_18.addItem(spacerItem21, 1, 2, 1, 1)
        self.admin_bereich.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.tab_8)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.check_lager = QtWidgets.QCheckBox(self.tab_8)
        self.check_lager.setStyleSheet("color:#ffffff")
        self.check_lager.setObjectName("check_lager")
        self.gridLayout_19.addWidget(self.check_lager, 2, 0, 1, 1)
        self.einstellungen_speichern = QtWidgets.QPushButton(self.tab_8)
        self.einstellungen_speichern.setMaximumSize(QtCore.QSize(150, 16777215))
        self.einstellungen_speichern.setStyleSheet("QPushButton{\n"
"   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid rgb(59, 204, 179);\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(130, 152, 152);\n"
"      border-style: solid;\n"
"    border: 1px solid #1EFFFF;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"\n"
"}")
        self.einstellungen_speichern.setObjectName("einstellungen_speichern")
        self.gridLayout_19.addWidget(self.einstellungen_speichern, 6, 0, 1, 1)
        self.check_uebersicht = QtWidgets.QCheckBox(self.tab_8)
        self.check_uebersicht.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.check_uebersicht.setStyleSheet("color:#ffffff")
        self.check_uebersicht.setObjectName("check_uebersicht")
        self.gridLayout_19.addWidget(self.check_uebersicht, 1, 0, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_19.addItem(spacerItem22, 5, 0, 1, 1)
        self.check_fahrzeuge = QtWidgets.QCheckBox(self.tab_8)
        self.check_fahrzeuge.setStyleSheet("color:#ffffff")
        self.check_fahrzeuge.setObjectName("check_fahrzeuge")
        self.gridLayout_19.addWidget(self.check_fahrzeuge, 3, 0, 1, 1)
        self.check_dienstbekleidung = QtWidgets.QCheckBox(self.tab_8)
        self.check_dienstbekleidung.setStyleSheet("color:#ffffff")
        self.check_dienstbekleidung.setObjectName("check_dienstbekleidung")
        self.gridLayout_19.addWidget(self.check_dienstbekleidung, 4, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab_8)
        self.pushButton.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton.setStyleSheet("QPushButton{\n"
"   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid rgb(59, 204, 179);\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(130, 152, 152);\n"
"      border-style: solid;\n"
"    border: 1px solid #1EFFFF;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_19.addWidget(self.pushButton, 6, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.tab_8)
        self.label_18.setObjectName("label_18")
        self.gridLayout_19.addWidget(self.label_18, 0, 0, 1, 1)
        self.admin_bereich.addTab(self.tab_8, "")
        self.admin_login.addWidget(self.admin_bereich, 6, 0, 1, 4)
        spacerItem23 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.admin_login.addItem(spacerItem23, 7, 1, 1, 1)
        self.login_label = QtWidgets.QLabel(self.tab_5)
        self.login_label.setObjectName("login_label")
        self.admin_login.addWidget(self.login_label, 0, 1, 1, 2)
        self.benutzer_label = QtWidgets.QLabel(self.tab_5)
        self.benutzer_label.setObjectName("benutzer_label")
        self.admin_login.addWidget(self.benutzer_label, 1, 2, 1, 1)
        self.login_error_label = QtWidgets.QLabel(self.tab_5)
        self.login_error_label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.login_error_label.setFont(font)
        self.login_error_label.setText("")
        self.login_error_label.setObjectName("login_error_label")
        self.admin_login.addWidget(self.login_error_label, 4, 1, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(40, 1, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.admin_login.addItem(spacerItem24, 1, 0, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(40, 1, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.admin_login.addItem(spacerItem25, 1, 3, 1, 1)
        self.login_btn = QtWidgets.QPushButton(self.tab_5)
        self.login_btn.setMaximumSize(QtCore.QSize(100, 30))
        self.login_btn.setStyleSheet("QPushButton{\n"
"   background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"      border-style: solid;\n"
"    border: 1px solid rgb(59, 204, 179);\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(130, 152, 152);\n"
"      border-style: solid;\n"
"    border: 1px solid #1EFFFF;\n"
"    border-radius: 5;\n"
"    padding: 1px 0px 1px 20px;\n"
"    font: 13px;\n"
"    min-width: 10em;\n"
"    padding: 5px;\n"
"    color: white;\n"
"\n"
"}")
        self.login_btn.setObjectName("login_btn")
        self.admin_login.addWidget(self.login_btn, 4, 2, 1, 1)
        self.gridLayout_16.addLayout(self.admin_login, 1, 3, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.gridLayout_11.addWidget(self.tabWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1464, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        self.admin_bereich.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.lager_textfeld_produkt.returnPressed.connect(self.lager_textfeld_menge.setFocus)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.combobox_lager, self.lager_textfeld_produkt)
        MainWindow.setTabOrder(self.lager_textfeld_produkt, self.lager_textfeld_menge)
        MainWindow.setTabOrder(self.lager_textfeld_menge, self.lager_textfeld_einsatz)
        MainWindow.setTabOrder(self.lager_textfeld_einsatz, self.lager_table)
        MainWindow.setTabOrder(self.lager_table, self.lager_btn)
        MainWindow.setTabOrder(self.lager_btn, self.combo_rtw)
        MainWindow.setTabOrder(self.combo_rtw, self.combo_zustand)
        MainWindow.setTabOrder(self.combo_zustand, self.fahrzeug_textedit)
        MainWindow.setTabOrder(self.fahrzeug_textedit, self.button_fahrzeuge)
        MainWindow.setTabOrder(self.button_fahrzeuge, self.klamotten_textfeld)
        MainWindow.setTabOrder(self.klamotten_textfeld, self.aufnahme)
        MainWindow.setTabOrder(self.aufnahme, self.klamotten_button)
        MainWindow.setTabOrder(self.klamotten_button, self.admin_text_ben)
        MainWindow.setTabOrder(self.admin_text_ben, self.admin_text_pw)
        MainWindow.setTabOrder(self.admin_text_pw, self.admin_new_prod_prod)
        MainWindow.setTabOrder(self.admin_new_prod_prod, self.admin_new_prod_bes)
        MainWindow.setTabOrder(self.admin_new_prod_bes, self.admin_new_prod_min)
        MainWindow.setTabOrder(self.admin_new_prod_min, self.admin_new_prod_max)
        MainWindow.setTabOrder(self.admin_new_prod_max, self.admin_new_prod_bar)
        MainWindow.setTabOrder(self.admin_new_prod_bar, self.admin_new_prod_inhalt_menge)
        MainWindow.setTabOrder(self.admin_new_prod_inhalt_menge, self.admin_new_prod_artikel)
        MainWindow.setTabOrder(self.admin_new_prod_artikel, self.admin_new_prod_table)
        MainWindow.setTabOrder(self.admin_new_prod_table, self.admin_new_prod_btn)
        MainWindow.setTabOrder(self.admin_new_prod_btn, self.admin_del_prod_prod)
        MainWindow.setTabOrder(self.admin_del_prod_prod, self.admin_del_prod_bar)
        MainWindow.setTabOrder(self.admin_del_prod_bar, self.admin_del_prod_table)
        MainWindow.setTabOrder(self.admin_del_prod_table, self.admin_del_prod_btn)
        MainWindow.setTabOrder(self.admin_del_prod_btn, self.fahrzeug_admin_funkkenn)
        MainWindow.setTabOrder(self.fahrzeug_admin_funkkenn, self.fahrzeug_admin_kennz)
        MainWindow.setTabOrder(self.fahrzeug_admin_kennz, self.fahrzeug_admin_ort)
        MainWindow.setTabOrder(self.fahrzeug_admin_ort, self.fahrzeug_admin_tuev)
        MainWindow.setTabOrder(self.fahrzeug_admin_tuev, self.fahrzeug_admin_save_btn)
        MainWindow.setTabOrder(self.fahrzeug_admin_save_btn, self.tabWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_uebersicht_lager.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        item = self.uebersicht_lager_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Produkt"))
        item = self.uebersicht_lager_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Vorhanden"))
        item = self.uebersicht_lager_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mindestbestand"))
        item = self.uebersicht_lager_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Fahrzeug Übersicht</span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Lager Übersicht</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Übersicht"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Produkt Barcode</span></p></body></html>"))
        self.label_einsatznummer.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Einsatznummer</span></p></body></html>"))
        item = self.lager_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Produkt"))
        item = self.lager_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Menge"))
        item = self.lager_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Keyword"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Menge</span></p></body></html>"))
        self.label_einsatznummer_enter.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Mit Enter bestätigen</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Produkte austragen</span></p></body></html>"))
        self.combobox_lager.setItemText(0, _translate("MainWindow", "Auffüllen nach Einsatz"))
        self.combobox_lager.setItemText(1, _translate("MainWindow", "Auffüllen wegen Fehlbestand"))
        self.combobox_lager.setItemText(2, _translate("MainWindow", "Falsch Entnahme - wieder zurück geben"))
        self.lager_btn.setText(_translate("MainWindow", "Speichern"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Lagerverwaltung"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Status der Fahrzeuge</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Fahrzeug</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "Bemerkung"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Zustand</span></p></body></html>"))
        self.button_fahrzeuge.setText(_translate("MainWindow", "Speichern"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Fahrzeug Status"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Übersicht der Ein- und Ausgänge von Dienstkleidung</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Wäsche, die zurückgekommen ist</span></p></body></html>"))
        item = self.klamotten_tabelle.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Barcode"))
        item = self.klamotten_tabelle.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Datum"))
        item = self.kleidung_zurueck_tabelle.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Barcode"))
        item = self.kleidung_zurueck_tabelle.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Datum"))
        self.klamotten_button.setText(_translate("MainWindow", "Wäsche Speichern"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Dienstkleidung Eingang und Abgabe</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">mit Enter bestätigen</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Wäsche, die abgegeben wurde</span></p></body></html>"))
        item = self.aufnahme.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Barcode"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Dienstkleidung"))
        self.passwort_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Passwort</span></p></body></html>"))
        self.label_35.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Mit Enter bestätigen.</span></p></body></html>"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">bestand</span></p></body></html>"))
        self.label24.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Neue Produkte anlegen</span></p></body></html>"))
        item = self.admin_new_prod_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Produkt"))
        item = self.admin_new_prod_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "bestand"))
        item = self.admin_new_prod_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mindestbestand"))
        item = self.admin_new_prod_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Maximal Bestand"))
        item = self.admin_new_prod_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Barcode"))
        item = self.admin_new_prod_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Inahalt"))
        item = self.admin_new_prod_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Artikel Nr."))
        self.label_36.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Inhalt menge</span></p></body></html>"))
        self.label_27.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Barcode</span></p></body></html>"))
        self.label_39.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Artikel-Nr.</span></p></body></html>"))
        self.admin_new_prod_btn.setText(_translate("MainWindow", "Speichern"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Produktname</span></p></body></html>"))
        self.label_26.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Maximal bestand</span></p></body></html>"))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Mindestbestand</span></p></body></html>"))
        self.admin_logout_btn.setText(_translate("MainWindow", "Logout"))
        self.label_29.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Produktname</span></p></body></html>"))
        self.label_31.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Produktname oder Barcode</span></p></body></html>"))
        self.label_30.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Barcode</span></p></body></html>"))
        item = self.admin_del_prod_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Produkt"))
        item = self.admin_del_prod_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Barcode"))
        self.label_28.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Produkte Löschen</span></p></body></html>"))
        self.admin_del_prod_btn.setText(_translate("MainWindow", "Löschen"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), _translate("MainWindow", "Produkt hinzufügen / Löschen"))
        self.pdf_erstellen.setText(_translate("MainWindow", "PDF erstellen"))
        self.Bestellung_speichern.setText(_translate("MainWindow", "Speichern"))
        self.button_bestellung_vor.setText(_translate("MainWindow", ">"))
        self.lager_bestellung.setText(_translate("MainWindow", "Bestellung online"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Bestelltes Material</span></p></body></html>"))
        self.label_40.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Fehlendes Material</span></p></body></html>"))
        self.button_bestellung_zurueck.setText(_translate("MainWindow", "<"))
        item = self.admin_lager_fehlendes_material.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Produkt"))
        item = self.admin_lager_fehlendes_material.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Vorhanden"))
        item = self.admin_lager_fehlendes_material.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mindestbestand"))
        item = self.admin_lager_fehlendes_material.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Maximal Menge"))
        item = self.admin_lager_fehlendes_material.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Status"))
        item = self.table_bestellt.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Produkt"))
        item = self.table_bestellt.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Status"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), _translate("MainWindow", "Fehlendes Material"))
        self.label_41.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Anzahl</span></p></body></html>"))
        self.label_37.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Barcode</span></p></body></html>"))
        self.label_42.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Produkt</span></p></body></html>"))
        self.admin_material_speichern_button.setText(_translate("MainWindow", "Speichern"))
        item = self.admin_material_speichern_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Produkt"))
        item = self.admin_material_speichern_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Anzahl"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_11), _translate("MainWindow", "Material einpflegen"))
        self.admin_bereich.setTabText(self.admin_bereich.indexOf(self.tab_6), _translate("MainWindow", "Lager"))
        self.label_33.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Kennzeichen</span></p></body></html>"))
        self.label_38.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Nächster Tüv</span></p></body></html>"))
        self.label_32.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Funkkennung</span></p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Fahrzeug anlegen</span></p></body></html>"))
        self.label_34.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Ort des Fahrzeuges</span></p></body></html>"))
        self.fahrzeug_admin_save_btn.setText(_translate("MainWindow", "Speichern"))
        self.admin_logout_btn_2.setText(_translate("MainWindow", "Logout"))
        self.admin_bereich.setTabText(self.admin_bereich.indexOf(self.tab_7), _translate("MainWindow", "Fahrzeuge"))
        self.check_lager.setText(_translate("MainWindow", "Lagerverwaltung"))
        self.einstellungen_speichern.setText(_translate("MainWindow", "Speichern"))
        self.check_uebersicht.setText(_translate("MainWindow", "Übersicht"))
        self.check_fahrzeuge.setText(_translate("MainWindow", "Fahrzeugstatus"))
        self.check_dienstbekleidung.setText(_translate("MainWindow", "Dienstkleidung"))
        self.pushButton.setText(_translate("MainWindow", "Abbrechen"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Bereiche Anzeigen oder nicht Anzeigen.</span></p></body></html>"))
        self.admin_bereich.setTabText(self.admin_bereich.indexOf(self.tab_8), _translate("MainWindow", "Einstellungen"))
        self.login_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Login</span></p></body></html>"))
        self.benutzer_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Benutzername</span></p></body></html>"))
        self.login_btn.setText(_translate("MainWindow", "Login"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Admin"))
