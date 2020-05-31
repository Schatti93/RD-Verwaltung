# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1388, 883)
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
        self.uebersicht_lager_table.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        self.uebersicht_lager_table.setDragDropOverwriteMode(False)
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
        self.uebersicht_lager_table.horizontalHeader().setStretchLastSection(True)
        self.uebersicht_lager_table.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.uebersicht_lager_table, 4, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addLayout(self.verticalLayout, 4, 2, 1, 1)
        self.line_11 = QtWidgets.QFrame(self.tab_4)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.gridLayout.addWidget(self.line_11, 2, 0, 1, 5)
        self.label_19 = QtWidgets.QLabel(self.tab_4)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 0, 0, 1, 1)
        self.verticalLayout2 = QtWidgets.QVBoxLayout()
        self.verticalLayout2.setObjectName("verticalLayout2")
        self.gridLayout.addLayout(self.verticalLayout2, 4, 4, 1, 1)
        self.line_10 = QtWidgets.QFrame(self.tab_4)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout.addWidget(self.line_10, 4, 1, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.tab_4)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 4, 3, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.tab_4)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 0, 2, 1, 1)
        self.label_uebersicht_lager = QtWidgets.QLabel(self.tab_4)
        self.label_uebersicht_lager.setMaximumSize(QtCore.QSize(500, 30))
        self.label_uebersicht_lager.setObjectName("label_uebersicht_lager")
        self.gridLayout.addWidget(self.label_uebersicht_lager, 3, 0, 1, 1)
        self.line_9 = QtWidgets.QFrame(self.tab_4)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout.addWidget(self.line_9, 1, 1, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_13.setObjectName("gridLayout_13")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem, 1, 0, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_einsatznummer = QtWidgets.QLabel(self.tab_3)
        self.label_einsatznummer.setObjectName("label_einsatznummer")
        self.gridLayout_4.addWidget(self.label_einsatznummer, 4, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 5, 0, 1, 1)
        self.combobox_lager = QtWidgets.QComboBox(self.tab_3)
        self.combobox_lager.setStyleSheet("QComboBox\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    selection-background-color: #111;\n"
"    selection-color: white;\n"
"\n"
"    background-color: #464646;\n"
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
"\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: red;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 0px;\n"
"    padding-left: 0px;\n"
"\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: rgb(67, 131, 202);\n"
"}\n"
"\n"
"QComboBox:!on\n"
"{\n"
"\n"
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
"\n"
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
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 5)
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
        self.gridLayout_4.addWidget(self.lager_textfeld_einsatz, 4, 1, 1, 6)
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 11, 0, 1, 1)
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
        self.lager_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lager_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
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
        self.lager_table.horizontalHeader().setStretchLastSection(True)
        self.lager_table.verticalHeader().setVisible(False)
        self.lager_table.verticalHeader().setCascadingSectionResizes(True)
        self.gridLayout_4.addWidget(self.lager_table, 7, 1, 1, 6)
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
        self.gridLayout_4.addWidget(self.label_15, 11, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 0, 6, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.tab_3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_4.addWidget(self.line_3, 2, 0, 1, 1)
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
        self.gridLayout_4.addWidget(self.lager_btn, 10, 2, 1, 3)
        self.lager_uebernehmen_btn = QtWidgets.QPushButton(self.tab_3)
        self.lager_uebernehmen_btn.setStyleSheet("QPushButton{\n"
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
        self.lager_uebernehmen_btn.setObjectName("lager_uebernehmen_btn")
        self.gridLayout_4.addWidget(self.lager_uebernehmen_btn, 6, 2, 1, 3)
        self.lager_error_label = QtWidgets.QLabel(self.tab_3)
        self.lager_error_label.setText("")
        self.lager_error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.lager_error_label.setObjectName("lager_error_label")
        self.gridLayout_4.addWidget(self.lager_error_label, 9, 1, 1, 6)
        self.lager_eintrag_loeschen = QtWidgets.QPushButton(self.tab_3)
        self.lager_eintrag_loeschen.setStyleSheet("QPushButton{\n"
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
        self.lager_eintrag_loeschen.setObjectName("lager_eintrag_loeschen")
        self.gridLayout_4.addWidget(self.lager_eintrag_loeschen, 10, 5, 1, 1)
        self.lager_tabelle_leeren = QtWidgets.QPushButton(self.tab_3)
        self.lager_tabelle_leeren.setStyleSheet("QPushButton{\n"
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
"}\n"
"")
        self.lager_tabelle_leeren.setObjectName("lager_tabelle_leeren")
        self.gridLayout_4.addWidget(self.lager_tabelle_leeren, 10, 6, 1, 1)
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
"\n"
"    background-color: #464646;\n"
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
"\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: red;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 0px;\n"
"    padding-left: 0px;\n"
"\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: rgb(67, 131, 202);\n"
"}\n"
"\n"
"QComboBox:!on\n"
"{\n"
"\n"
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
"\n"
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
"background-color: rgb(107, 109, 108);\n"
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
"\n"
"    background-color: #464646;\n"
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
"\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: red;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 0px;\n"
"    padding-left: 0px;\n"
"\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: rgb(67, 131, 202);\n"
"}\n"
"\n"
"QComboBox:!on\n"
"{\n"
"\n"
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
"\n"
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
        self.tab_17 = QtWidgets.QWidget()
        self.tab_17.setObjectName("tab_17")
        self.gridLayout_30 = QtWidgets.QGridLayout(self.tab_17)
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.label_92 = QtWidgets.QLabel(self.tab_17)
        self.label_92.setObjectName("label_92")
        self.gridLayout_30.addWidget(self.label_92, 4, 4, 1, 1)
        self.mpg_user_geraete_aufrufen_btn = QtWidgets.QPushButton(self.tab_17)
        self.mpg_user_geraete_aufrufen_btn.setStyleSheet("QPushButton{\n"
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
        self.mpg_user_geraete_aufrufen_btn.setObjectName("mpg_user_geraete_aufrufen_btn")
        self.gridLayout_30.addWidget(self.mpg_user_geraete_aufrufen_btn, 3, 3, 1, 1)
        self.label_91 = QtWidgets.QLabel(self.tab_17)
        self.label_91.setStyleSheet("")
        self.label_91.setObjectName("label_91")
        self.gridLayout_30.addWidget(self.label_91, 2, 1, 1, 1)
        self.mpg_Fahrzeuge_combo = QtWidgets.QComboBox(self.tab_17)
        self.mpg_Fahrzeuge_combo.setStyleSheet("QComboBox\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    selection-background-color: #111;\n"
"    selection-color: white;\n"
"\n"
"    background-color: #464646;\n"
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
"\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: red;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 0px;\n"
"    padding-left: 0px;\n"
"\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: rgb(67, 131, 202);\n"
"}\n"
"\n"
"QComboBox:!on\n"
"{\n"
"\n"
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
"\n"
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
        self.mpg_Fahrzeuge_combo.setObjectName("mpg_Fahrzeuge_combo")
        self.gridLayout_30.addWidget(self.mpg_Fahrzeuge_combo, 2, 0, 1, 1)
        self.mpg_geraete_tabelle_fahrzeug = QtWidgets.QTableWidget(self.tab_17)
        self.mpg_geraete_tabelle_fahrzeug.setStyleSheet("QTableView {\n"
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
        self.mpg_geraete_tabelle_fahrzeug.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.mpg_geraete_tabelle_fahrzeug.setObjectName("mpg_geraete_tabelle_fahrzeug")
        self.mpg_geraete_tabelle_fahrzeug.setColumnCount(3)
        self.mpg_geraete_tabelle_fahrzeug.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.mpg_geraete_tabelle_fahrzeug.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.mpg_geraete_tabelle_fahrzeug.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.mpg_geraete_tabelle_fahrzeug.setHorizontalHeaderItem(2, item)
        self.mpg_geraete_tabelle_fahrzeug.horizontalHeader().setCascadingSectionResizes(True)
        self.mpg_geraete_tabelle_fahrzeug.horizontalHeader().setStretchLastSection(True)
        self.mpg_geraete_tabelle_fahrzeug.verticalHeader().setVisible(False)
        self.mpg_geraete_tabelle_fahrzeug.verticalHeader().setHighlightSections(True)
        self.gridLayout_30.addWidget(self.mpg_geraete_tabelle_fahrzeug, 3, 0, 5, 1)
        self.line_32 = QtWidgets.QFrame(self.tab_17)
        self.line_32.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_32.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_32.setObjectName("line_32")
        self.gridLayout_30.addWidget(self.line_32, 1, 3, 1, 1)
        self.label_88 = QtWidgets.QLabel(self.tab_17)
        self.label_88.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_88.setObjectName("label_88")
        self.gridLayout_30.addWidget(self.label_88, 0, 0, 1, 1)
        self.mpg_user_geraete_speichern_btn = QtWidgets.QPushButton(self.tab_17)
        self.mpg_user_geraete_speichern_btn.setStyleSheet("QPushButton{\n"
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
        self.mpg_user_geraete_speichern_btn.setObjectName("mpg_user_geraete_speichern_btn")
        self.gridLayout_30.addWidget(self.mpg_user_geraete_speichern_btn, 6, 3, 1, 1)
        self.line_30 = QtWidgets.QFrame(self.tab_17)
        self.line_30.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_30.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_30.setObjectName("line_30")
        self.gridLayout_30.addWidget(self.line_30, 1, 0, 1, 1)
        self.label_89 = QtWidgets.QLabel(self.tab_17)
        self.label_89.setObjectName("label_89")
        self.gridLayout_30.addWidget(self.label_89, 2, 4, 1, 1)
        self.label_90 = QtWidgets.QLabel(self.tab_17)
        self.label_90.setObjectName("label_90")
        self.gridLayout_30.addWidget(self.label_90, 0, 3, 1, 1)
        self.mpg_user_geraete_standort_combo = QtWidgets.QComboBox(self.tab_17)
        self.mpg_user_geraete_standort_combo.setStyleSheet("QComboBox\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    selection-background-color: #111;\n"
"    selection-color: white;\n"
"\n"
"    background-color: #464646;\n"
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
"\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: red;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 0px;\n"
"    padding-left: 0px;\n"
"\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: rgb(67, 131, 202);\n"
"}\n"
"\n"
"QComboBox:!on\n"
"{\n"
"\n"
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
"\n"
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
        self.mpg_user_geraete_standort_combo.setObjectName("mpg_user_geraete_standort_combo")
        self.gridLayout_30.addWidget(self.mpg_user_geraete_standort_combo, 4, 3, 1, 1)
        self.mpg_user_geraete_barcode = QtWidgets.QLineEdit(self.tab_17)
        self.mpg_user_geraete_barcode.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.mpg_user_geraete_barcode.setObjectName("mpg_user_geraete_barcode")
        self.gridLayout_30.addWidget(self.mpg_user_geraete_barcode, 2, 3, 1, 1)
        self.line_31 = QtWidgets.QFrame(self.tab_17)
        self.line_31.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_31.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_31.setObjectName("line_31")
        self.gridLayout_30.addWidget(self.line_31, 1, 2, 7, 1)
        self.mpg_user_bemerkung = QtWidgets.QLineEdit(self.tab_17)
        self.mpg_user_bemerkung.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.mpg_user_bemerkung.setObjectName("mpg_user_bemerkung")
        self.gridLayout_30.addWidget(self.mpg_user_bemerkung, 5, 3, 1, 1)
        self.label_95 = QtWidgets.QLabel(self.tab_17)
        self.label_95.setObjectName("label_95")
        self.gridLayout_30.addWidget(self.label_95, 5, 4, 1, 1)
        self.tabWidget.addTab(self.tab_17, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 1, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 2, 3, 1, 1)
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
        self.klamotten_tabelle.horizontalHeader().setStretchLastSection(True)
        self.klamotten_tabelle.verticalHeader().setVisible(False)
        self.klamotten_tabelle.verticalHeader().setDefaultSectionSize(30)
        self.gridLayout_3.addWidget(self.klamotten_tabelle, 3, 1, 1, 1)
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
        self.kleidung_zurueck_tabelle.horizontalHeader().setStretchLastSection(True)
        self.kleidung_zurueck_tabelle.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.kleidung_zurueck_tabelle, 3, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 1, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.tab)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_3.addWidget(self.line_6, 1, 1, 1, 3)
        self.line_2 = QtWidgets.QFrame(self.tab)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 2, 2, 2, 1)
        self.gridLayout_15.addLayout(self.gridLayout_3, 0, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
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
        self.gridLayout_2.addWidget(self.klamotten_button, 5, 1, 1, 2)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 5, 0, 1, 1)
        self.aufnahme = QtWidgets.QTableWidget(self.tab)
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
        self.aufnahme.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.aufnahme.setObjectName("aufnahme")
        self.aufnahme.setColumnCount(1)
        self.aufnahme.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.aufnahme.setHorizontalHeaderItem(0, item)
        self.aufnahme.horizontalHeader().setDefaultSectionSize(400)
        self.aufnahme.horizontalHeader().setStretchLastSection(True)
        self.aufnahme.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.aufnahme, 4, 0, 1, 4)
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
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setStyleSheet("color: white;")
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 3, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem9, 5, 3, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.tab)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_2.addWidget(self.line_8, 2, 0, 1, 1)
        self.gridLayout_15.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.admin_login = QtWidgets.QGridLayout()
        self.admin_login.setObjectName("admin_login")
        spacerItem10 = QtWidgets.QSpacerItem(40, 1, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.admin_login.addItem(spacerItem10, 1, 3, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.admin_login.addItem(spacerItem11, 7, 1, 1, 1)
        self.admin_logout_btn = QtWidgets.QPushButton(self.tab_5)
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
        self.admin_login.addWidget(self.admin_logout_btn, 4, 3, 1, 1)
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
        spacerItem12 = QtWidgets.QSpacerItem(40, 1, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.admin_login.addItem(spacerItem12, 1, 0, 1, 1)
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
        self.passwort_label = QtWidgets.QLabel(self.tab_5)
        self.passwort_label.setObjectName("passwort_label")
        self.admin_login.addWidget(self.passwort_label, 2, 2, 1, 1)
        self.login_label = QtWidgets.QLabel(self.tab_5)
        self.login_label.setObjectName("login_label")
        self.admin_login.addWidget(self.login_label, 0, 1, 1, 2)
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
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem13, 15, 1, 1, 1)
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
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem14, 15, 3, 1, 1)
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
        self.admin_new_prod_table.horizontalHeader().setStretchLastSection(True)
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
        self.admin_del_prod_table.horizontalHeader().setStretchLastSection(True)
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
        self.tab_19 = QtWidgets.QWidget()
        self.tab_19.setObjectName("tab_19")
        self.gridLayout_33 = QtWidgets.QGridLayout(self.tab_19)
        self.gridLayout_33.setObjectName("gridLayout_33")
        self.gridLayout_28 = QtWidgets.QGridLayout()
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.line_36 = QtWidgets.QFrame(self.tab_19)
        self.line_36.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_36.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_36.setObjectName("line_36")
        self.gridLayout_28.addWidget(self.line_36, 3, 0, 1, 1)
        self.admin_lager_alle_produkte = QtWidgets.QTableWidget(self.tab_19)
        self.admin_lager_alle_produkte.setStyleSheet("QTableView {\n"
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
        self.admin_lager_alle_produkte.setObjectName("admin_lager_alle_produkte")
        self.admin_lager_alle_produkte.setColumnCount(8)
        self.admin_lager_alle_produkte.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.admin_lager_alle_produkte.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_lager_alle_produkte.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_lager_alle_produkte.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_lager_alle_produkte.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_lager_alle_produkte.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_lager_alle_produkte.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_lager_alle_produkte.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.admin_lager_alle_produkte.setHorizontalHeaderItem(7, item)
        self.admin_lager_alle_produkte.horizontalHeader().setCascadingSectionResizes(True)
        self.admin_lager_alle_produkte.horizontalHeader().setStretchLastSection(True)
        self.admin_lager_alle_produkte.verticalHeader().setVisible(False)
        self.gridLayout_28.addWidget(self.admin_lager_alle_produkte, 1, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.tab_19)
        self.label_14.setObjectName("label_14")
        self.gridLayout_28.addWidget(self.label_14, 0, 0, 1, 1)
        self.admin_produkte_update = QtWidgets.QPushButton(self.tab_19)
        self.admin_produkte_update.setStyleSheet("QPushButton{\n"
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
        self.admin_produkte_update.setObjectName("admin_produkte_update")
        self.gridLayout_28.addWidget(self.admin_produkte_update, 2, 0, 1, 1)
        self.gridLayout_33.addLayout(self.gridLayout_28, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_19, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.tab_10)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_40 = QtWidgets.QLabel(self.tab_10)
        self.label_40.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_40.setObjectName("label_40")
        self.gridLayout_8.addWidget(self.label_40, 0, 0, 1, 1)
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
        self.admin_lager_fehlendes_material.setColumnCount(6)
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
        item = QtWidgets.QTableWidgetItem()
        self.admin_lager_fehlendes_material.setHorizontalHeaderItem(5, item)
        self.admin_lager_fehlendes_material.horizontalHeader().setCascadingSectionResizes(True)
        self.admin_lager_fehlendes_material.horizontalHeader().setDefaultSectionSize(122)
        self.admin_lager_fehlendes_material.horizontalHeader().setMinimumSectionSize(122)
        self.admin_lager_fehlendes_material.horizontalHeader().setStretchLastSection(True)
        self.admin_lager_fehlendes_material.verticalHeader().setVisible(False)
        self.gridLayout_8.addWidget(self.admin_lager_fehlendes_material, 2, 0, 2, 2)
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
        self.gridLayout_8.addWidget(self.pdf_erstellen, 5, 1, 1, 1)
        self.line_17 = QtWidgets.QFrame(self.tab_10)
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.gridLayout_8.addWidget(self.line_17, 1, 0, 1, 1)
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
        self.gridLayout_8.addWidget(self.lager_bestellung, 5, 0, 1, 1)
        self.gridLayout_24.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_10, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.tab_11)
        self.gridLayout_21.setObjectName("gridLayout_21")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_21.addItem(spacerItem15, 0, 2, 1, 1)
        self.gridLayout_20 = QtWidgets.QGridLayout()
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.label_37 = QtWidgets.QLabel(self.tab_11)
        self.label_37.setObjectName("label_37")
        self.gridLayout_20.addWidget(self.label_37, 2, 2, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.tab_11)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.gridLayout_20.addWidget(self.label_43, 0, 1, 1, 1)
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
        self.gridLayout_20.addWidget(self.admin_material_speichern_barcode, 2, 1, 1, 1)
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
        self.gridLayout_20.addWidget(self.admin_material_speichern_anzahl, 3, 1, 1, 1)
        self.admin_material_speichern_combo = QtWidgets.QComboBox(self.tab_11)
        self.admin_material_speichern_combo.setStyleSheet("QComboBox\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    selection-background-color: #111;\n"
"    selection-color: white;\n"
"\n"
"    background-color: #464646;\n"
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
"\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: red;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 0px;\n"
"    padding-left: 0px;\n"
"\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: rgb(67, 131, 202);\n"
"}\n"
"\n"
"QComboBox:!on\n"
"{\n"
"\n"
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
"\n"
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
        self.gridLayout_20.addWidget(self.admin_material_speichern_combo, 4, 1, 1, 1)
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
        self.gridLayout_20.addWidget(self.admin_material_speichern_button, 6, 1, 1, 2)
        self.label_42 = QtWidgets.QLabel(self.tab_11)
        self.label_42.setObjectName("label_42")
        self.gridLayout_20.addWidget(self.label_42, 4, 2, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.tab_11)
        self.label_41.setObjectName("label_41")
        self.gridLayout_20.addWidget(self.label_41, 3, 2, 1, 1)
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
        self.admin_material_speichern_table.horizontalHeader().setStretchLastSection(True)
        self.admin_material_speichern_table.verticalHeader().setVisible(False)
        self.gridLayout_20.addWidget(self.admin_material_speichern_table, 5, 1, 1, 2)
        self.line_5 = QtWidgets.QFrame(self.tab_11)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_20.addWidget(self.line_5, 1, 1, 1, 1)
        self.gridLayout_21.addLayout(self.gridLayout_20, 0, 1, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_21.addItem(spacerItem16, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_11, "")
        self.gridLayout_17.addWidget(self.tabWidget_2, 1, 0, 2, 1)
        self.admin_bereich.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.tab_7)
        self.gridLayout_18.setObjectName("gridLayout_18")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_18.addItem(spacerItem17, 0, 0, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_18.addItem(spacerItem18, 0, 2, 1, 1)
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
        self.gridLayout_18.addLayout(self.gridLayout_7, 0, 1, 1, 1)
        self.admin_bereich.addTab(self.tab_7, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.tab_13)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_13)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.tab_14)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.gridLayout_31 = QtWidgets.QGridLayout()
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.geraete_verwalten_geraet = QtWidgets.QLineEdit(self.tab_14)
        self.geraete_verwalten_geraet.setMaximumSize(QtCore.QSize(350, 16777215))
        self.geraete_verwalten_geraet.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"\n"
"")
        self.geraete_verwalten_geraet.setObjectName("geraete_verwalten_geraet")
        self.gridLayout_31.addWidget(self.geraete_verwalten_geraet, 4, 2, 1, 1)
        self.label_59 = QtWidgets.QLabel(self.tab_14)
        self.label_59.setObjectName("label_59")
        self.gridLayout_31.addWidget(self.label_59, 6, 3, 1, 1)
        self.label_56 = QtWidgets.QLabel(self.tab_14)
        self.label_56.setObjectName("label_56")
        self.gridLayout_31.addWidget(self.label_56, 5, 1, 1, 1)
        self.line_23 = QtWidgets.QFrame(self.tab_14)
        self.line_23.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        self.gridLayout_31.addWidget(self.line_23, 11, 0, 1, 1)
        self.label_58 = QtWidgets.QLabel(self.tab_14)
        self.label_58.setObjectName("label_58")
        self.gridLayout_31.addWidget(self.label_58, 5, 3, 1, 1)
        self.geraete_verwalten_inventarnummer = QtWidgets.QLineEdit(self.tab_14)
        self.geraete_verwalten_inventarnummer.setMaximumSize(QtCore.QSize(350, 16777215))
        self.geraete_verwalten_inventarnummer.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.geraete_verwalten_inventarnummer.setObjectName("geraete_verwalten_inventarnummer")
        self.gridLayout_31.addWidget(self.geraete_verwalten_inventarnummer, 4, 0, 1, 1)
        self.geraete_verwalten_speichern_button = QtWidgets.QPushButton(self.tab_14)
        self.geraete_verwalten_speichern_button.setMaximumSize(QtCore.QSize(150, 40))
        self.geraete_verwalten_speichern_button.setStyleSheet("QPushButton{\n"
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
        self.geraete_verwalten_speichern_button.setObjectName("geraete_verwalten_speichern_button")
        self.gridLayout_31.addWidget(self.geraete_verwalten_speichern_button, 9, 1, 1, 1)
        self.geraete_verwalten_ce = QtWidgets.QLineEdit(self.tab_14)
        self.geraete_verwalten_ce.setMaximumSize(QtCore.QSize(350, 16777215))
        self.geraete_verwalten_ce.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.geraete_verwalten_ce.setObjectName("geraete_verwalten_ce")
        self.gridLayout_31.addWidget(self.geraete_verwalten_ce, 6, 0, 1, 1)
        self.label_63 = QtWidgets.QLabel(self.tab_14)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_63.setFont(font)
        self.label_63.setObjectName("label_63")
        self.gridLayout_31.addWidget(self.label_63, 10, 0, 1, 1)
        self.geraete_verwalten_standort_combo = QtWidgets.QComboBox(self.tab_14)
        self.geraete_verwalten_standort_combo.setMaximumSize(QtCore.QSize(350, 16777215))
        self.geraete_verwalten_standort_combo.setStyleSheet("QComboBox\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    selection-background-color: #111;\n"
"    selection-color: white;\n"
"\n"
"    background-color: #464646;\n"
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
"\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: red;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 0px;\n"
"    padding-left: 0px;\n"
"\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: rgb(67, 131, 202);\n"
"}\n"
"\n"
"QComboBox:!on\n"
"{\n"
"\n"
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
"\n"
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
        self.geraete_verwalten_standort_combo.setObjectName("geraete_verwalten_standort_combo")
        self.gridLayout_31.addWidget(self.geraete_verwalten_standort_combo, 8, 2, 1, 1)
        self.geraete_verwalten_geraetenummer = QtWidgets.QLineEdit(self.tab_14)
        self.geraete_verwalten_geraetenummer.setMaximumSize(QtCore.QSize(350, 16777215))
        self.geraete_verwalten_geraetenummer.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.geraete_verwalten_geraetenummer.setObjectName("geraete_verwalten_geraetenummer")
        self.gridLayout_31.addWidget(self.geraete_verwalten_geraetenummer, 5, 0, 1, 1)
        self.label_55 = QtWidgets.QLabel(self.tab_14)
        self.label_55.setObjectName("label_55")
        self.gridLayout_31.addWidget(self.label_55, 4, 3, 1, 1)
        self.geraete_verwalten_aenderung_speichern_btn = QtWidgets.QPushButton(self.tab_14)
        self.geraete_verwalten_aenderung_speichern_btn.setStyleSheet("QPushButton{\n"
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
        self.geraete_verwalten_aenderung_speichern_btn.setObjectName("geraete_verwalten_aenderung_speichern_btn")
        self.gridLayout_31.addWidget(self.geraete_verwalten_aenderung_speichern_btn, 13, 1, 1, 1)
        self.label_61 = QtWidgets.QLabel(self.tab_14)
        self.label_61.setObjectName("label_61")
        self.gridLayout_31.addWidget(self.label_61, 8, 3, 1, 1)
        self.mpg_geraete_tabelle = QtWidgets.QTableWidget(self.tab_14)
        self.mpg_geraete_tabelle.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.mpg_geraete_tabelle.setStyleSheet("QTableView {\n"
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
        self.mpg_geraete_tabelle.setObjectName("mpg_geraete_tabelle")
        self.mpg_geraete_tabelle.setColumnCount(12)
        self.mpg_geraete_tabelle.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.mpg_geraete_tabelle.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.mpg_geraete_tabelle.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.mpg_geraete_tabelle.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.mpg_geraete_tabelle.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.mpg_geraete_tabelle.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.mpg_geraete_tabelle.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.mpg_geraete_tabelle.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.mpg_geraete_tabelle.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.mpg_geraete_tabelle.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.mpg_geraete_tabelle.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.mpg_geraete_tabelle.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.mpg_geraete_tabelle.setHorizontalHeaderItem(11, item)
        self.mpg_geraete_tabelle.horizontalHeader().setCascadingSectionResizes(True)
        self.mpg_geraete_tabelle.horizontalHeader().setStretchLastSection(True)
        self.mpg_geraete_tabelle.verticalHeader().setVisible(False)
        self.mpg_geraete_tabelle.verticalHeader().setCascadingSectionResizes(False)
        self.mpg_geraete_tabelle.verticalHeader().setHighlightSections(False)
        self.gridLayout_31.addWidget(self.mpg_geraete_tabelle, 12, 0, 1, 4)
        self.label_57 = QtWidgets.QLabel(self.tab_14)
        self.label_57.setObjectName("label_57")
        self.gridLayout_31.addWidget(self.label_57, 4, 1, 1, 1)
        self.label_83 = QtWidgets.QLabel(self.tab_14)
        self.label_83.setObjectName("label_83")
        self.gridLayout_31.addWidget(self.label_83, 2, 0, 1, 1)
        self.geraete_verwalten_prueffrist = QtWidgets.QLineEdit(self.tab_14)
        self.geraete_verwalten_prueffrist.setMaximumSize(QtCore.QSize(350, 16777215))
        self.geraete_verwalten_prueffrist.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.geraete_verwalten_prueffrist.setInputMethodHints(QtCore.Qt.ImhNone)
        self.geraete_verwalten_prueffrist.setObjectName("geraete_verwalten_prueffrist")
        self.gridLayout_31.addWidget(self.geraete_verwalten_prueffrist, 6, 2, 1, 1)
        self.label_62 = QtWidgets.QLabel(self.tab_14)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_62.setFont(font)
        self.label_62.setObjectName("label_62")
        self.gridLayout_31.addWidget(self.label_62, 0, 0, 1, 1)
        self.label_82 = QtWidgets.QLabel(self.tab_14)
        self.label_82.setObjectName("label_82")
        self.gridLayout_31.addWidget(self.label_82, 6, 1, 1, 1)
        self.geraete_verwalten_pruefdatum = QtWidgets.QLineEdit(self.tab_14)
        self.geraete_verwalten_pruefdatum.setMaximumSize(QtCore.QSize(350, 16777215))
        self.geraete_verwalten_pruefdatum.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.geraete_verwalten_pruefdatum.setObjectName("geraete_verwalten_pruefdatum")
        self.gridLayout_31.addWidget(self.geraete_verwalten_pruefdatum, 5, 2, 1, 1)
        self.line_24 = QtWidgets.QFrame(self.tab_14)
        self.line_24.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_24.setObjectName("line_24")
        self.gridLayout_31.addWidget(self.line_24, 1, 0, 1, 1)
        self.geraete_verwalten_artikelnr = QtWidgets.QLineEdit(self.tab_14)
        self.geraete_verwalten_artikelnr.setMaximumSize(QtCore.QSize(350, 16777215))
        self.geraete_verwalten_artikelnr.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"\n"
"")
        self.geraete_verwalten_artikelnr.setObjectName("geraete_verwalten_artikelnr")
        self.gridLayout_31.addWidget(self.geraete_verwalten_artikelnr, 7, 2, 1, 1)
        self.geraet_label = QtWidgets.QLabel(self.tab_14)
        self.geraet_label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.geraet_label.setObjectName("geraet_label")
        self.gridLayout_31.addWidget(self.geraet_label, 7, 3, 1, 1)
        self.geraete_verwalten_bemerkung = QtWidgets.QLineEdit(self.tab_14)
        self.geraete_verwalten_bemerkung.setMaximumSize(QtCore.QSize(350, 16777215))
        self.geraete_verwalten_bemerkung.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.geraete_verwalten_bemerkung.setObjectName("geraete_verwalten_bemerkung")
        self.gridLayout_31.addWidget(self.geraete_verwalten_bemerkung, 7, 0, 1, 1)
        self.label_60 = QtWidgets.QLabel(self.tab_14)
        self.label_60.setObjectName("label_60")
        self.gridLayout_31.addWidget(self.label_60, 7, 1, 1, 1)
        self.geraete_verwalten_anschaffung = QtWidgets.QLineEdit(self.tab_14)
        self.geraete_verwalten_anschaffung.setMaximumSize(QtCore.QSize(350, 16777215))
        self.geraete_verwalten_anschaffung.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.geraete_verwalten_anschaffung.setObjectName("geraete_verwalten_anschaffung")
        self.gridLayout_31.addWidget(self.geraete_verwalten_anschaffung, 8, 0, 1, 1)
        self.label_101 = QtWidgets.QLabel(self.tab_14)
        self.label_101.setObjectName("label_101")
        self.gridLayout_31.addWidget(self.label_101, 8, 1, 1, 1)
        self.gridLayout_22.addLayout(self.gridLayout_31, 2, 1, 1, 1)
        self.line_25 = QtWidgets.QFrame(self.tab_14)
        self.line_25.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_25.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_25.setObjectName("line_25")
        self.gridLayout_22.addWidget(self.line_25, 1, 2, 1, 1)
        self.tabWidget_3.addTab(self.tab_14, "")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.tab_16)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.line_29 = QtWidgets.QFrame(self.tab_16)
        self.line_29.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_29.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_29.setObjectName("line_29")
        self.gridLayout_29.addWidget(self.line_29, 2, 1, 1, 1)
        self.verwertet_datum = QtWidgets.QLineEdit(self.tab_16)
        self.verwertet_datum.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.verwertet_datum.setObjectName("verwertet_datum")
        self.gridLayout_29.addWidget(self.verwertet_datum, 4, 1, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_29.addItem(spacerItem20, 7, 0, 1, 1)
        self.verwertet_geraete_combo = QtWidgets.QComboBox(self.tab_16)
        self.verwertet_geraete_combo.setStyleSheet("QComboBox\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    selection-background-color: #111;\n"
"    selection-color: white;\n"
"\n"
"    background-color: #464646;\n"
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
"\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: red;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 0px;\n"
"    padding-left: 0px;\n"
"\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: rgb(67, 131, 202);\n"
"}\n"
"\n"
"QComboBox:!on\n"
"{\n"
"\n"
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
"\n"
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
        self.verwertet_geraete_combo.setObjectName("verwertet_geraete_combo")
        self.verwertet_geraete_combo.addItem("")
        self.verwertet_geraete_combo.setItemText(0, "")
        self.gridLayout_29.addWidget(self.verwertet_geraete_combo, 3, 1, 1, 1)
        self.label_81 = QtWidgets.QLabel(self.tab_16)
        self.label_81.setObjectName("label_81")
        self.gridLayout_29.addWidget(self.label_81, 4, 2, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_29.addItem(spacerItem21, 4, 3, 1, 1)
        self.verwertet_speichern_button = QtWidgets.QPushButton(self.tab_16)
        self.verwertet_speichern_button.setStyleSheet("QPushButton{\n"
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
        self.verwertet_speichern_button.setObjectName("verwertet_speichern_button")
        self.gridLayout_29.addWidget(self.verwertet_speichern_button, 6, 1, 1, 1)
        self.verwertet_tabelle = QtWidgets.QTableWidget(self.tab_16)
        self.verwertet_tabelle.setStyleSheet("QTableView {\n"
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
        self.verwertet_tabelle.setObjectName("verwertet_tabelle")
        self.verwertet_tabelle.setColumnCount(3)
        self.verwertet_tabelle.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.verwertet_tabelle.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.verwertet_tabelle.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.verwertet_tabelle.setHorizontalHeaderItem(2, item)
        self.verwertet_tabelle.horizontalHeader().setStretchLastSection(False)
        self.verwertet_tabelle.verticalHeader().setVisible(False)
        self.verwertet_tabelle.verticalHeader().setCascadingSectionResizes(True)
        self.verwertet_tabelle.verticalHeader().setHighlightSections(False)
        self.gridLayout_29.addWidget(self.verwertet_tabelle, 7, 1, 1, 2)
        self.label_79 = QtWidgets.QLabel(self.tab_16)
        self.label_79.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_79.setFont(font)
        self.label_79.setObjectName("label_79")
        self.gridLayout_29.addWidget(self.label_79, 0, 1, 1, 1)
        self.label_80 = QtWidgets.QLabel(self.tab_16)
        self.label_80.setObjectName("label_80")
        self.gridLayout_29.addWidget(self.label_80, 3, 2, 1, 1)
        self.verwertet_bemerkung = QtWidgets.QLineEdit(self.tab_16)
        self.verwertet_bemerkung.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.verwertet_bemerkung.setObjectName("verwertet_bemerkung")
        self.gridLayout_29.addWidget(self.verwertet_bemerkung, 5, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.tab_16)
        self.label_21.setObjectName("label_21")
        self.gridLayout_29.addWidget(self.label_21, 5, 2, 1, 1)
        self.tabWidget_3.addTab(self.tab_16, "")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.tab_15)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.line_26 = QtWidgets.QFrame(self.tab_15)
        self.line_26.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_26.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_26.setObjectName("line_26")
        self.gridLayout_27.addWidget(self.line_26, 3, 0, 1, 1)
        self.einweisung_einweisender_standard = QtWidgets.QLineEdit(self.tab_15)
        self.einweisung_einweisender_standard.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.einweisung_einweisender_standard.setObjectName("einweisung_einweisender_standard")
        self.gridLayout_27.addWidget(self.einweisung_einweisender_standard, 8, 3, 1, 1)
        self.label_78 = QtWidgets.QLabel(self.tab_15)
        self.label_78.setObjectName("label_78")
        self.gridLayout_27.addWidget(self.label_78, 11, 3, 1, 1)
        self.label_66 = QtWidgets.QLabel(self.tab_15)
        self.label_66.setObjectName("label_66")
        self.gridLayout_27.addWidget(self.label_66, 5, 1, 1, 1)
        self.label_77 = QtWidgets.QLabel(self.tab_15)
        self.label_77.setObjectName("label_77")
        self.gridLayout_27.addWidget(self.label_77, 9, 4, 1, 1)
        self.label_74 = QtWidgets.QLabel(self.tab_15)
        self.label_74.setObjectName("label_74")
        self.gridLayout_27.addWidget(self.label_74, 6, 4, 1, 1)
        self.label_87 = QtWidgets.QLabel(self.tab_15)
        self.label_87.setObjectName("label_87")
        self.gridLayout_27.addWidget(self.label_87, 13, 0, 1, 1)
        self.einweisung_original_standard = QtWidgets.QLineEdit(self.tab_15)
        self.einweisung_original_standard.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.einweisung_original_standard.setObjectName("einweisung_original_standard")
        self.gridLayout_27.addWidget(self.einweisung_original_standard, 9, 3, 1, 1)
        self.label_75 = QtWidgets.QLabel(self.tab_15)
        self.label_75.setObjectName("label_75")
        self.gridLayout_27.addWidget(self.label_75, 7, 4, 1, 1)
        self.label_67 = QtWidgets.QLabel(self.tab_15)
        self.label_67.setObjectName("label_67")
        self.gridLayout_27.addWidget(self.label_67, 6, 1, 1, 1)
        self.einweisung_speichern_btn = QtWidgets.QPushButton(self.tab_15)
        self.einweisung_speichern_btn.setStyleSheet("QPushButton{\n"
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
        self.einweisung_speichern_btn.setObjectName("einweisung_speichern_btn")
        self.gridLayout_27.addWidget(self.einweisung_speichern_btn, 10, 0, 1, 1)
        self.einweisung_ma_combo = QtWidgets.QComboBox(self.tab_15)
        self.einweisung_ma_combo.setStyleSheet("QComboBox\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    selection-background-color: #111;\n"
"    selection-color: white;\n"
"\n"
"    background-color: #464646;\n"
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
"\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: red;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 0px;\n"
"    padding-left: 0px;\n"
"\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: rgb(67, 131, 202);\n"
"}\n"
"\n"
"QComboBox:!on\n"
"{\n"
"\n"
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
"\n"
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
        self.einweisung_ma_combo.setObjectName("einweisung_ma_combo")
        self.gridLayout_27.addWidget(self.einweisung_ma_combo, 7, 0, 1, 1)
        self.label_84 = QtWidgets.QLabel(self.tab_15)
        self.label_84.setObjectName("label_84")
        self.gridLayout_27.addWidget(self.label_84, 14, 1, 1, 1)
        self.einweisung_datum_standard = QtWidgets.QLineEdit(self.tab_15)
        self.einweisung_datum_standard.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.einweisung_datum_standard.setObjectName("einweisung_datum_standard")
        self.gridLayout_27.addWidget(self.einweisung_datum_standard, 6, 3, 1, 1)
        self.line_28 = QtWidgets.QFrame(self.tab_15)
        self.line_28.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_28.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_28.setObjectName("line_28")
        self.gridLayout_27.addWidget(self.line_28, 3, 3, 1, 1)
        self.einweisung_einweisender = QtWidgets.QLineEdit(self.tab_15)
        self.einweisung_einweisender.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.einweisung_einweisender.setObjectName("einweisung_einweisender")
        self.gridLayout_27.addWidget(self.einweisung_einweisender, 8, 0, 1, 1)
        self.einweisung_geraete_combo_standard = QtWidgets.QComboBox(self.tab_15)
        self.einweisung_geraete_combo_standard.setStyleSheet("QComboBox\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    selection-background-color: #111;\n"
"    selection-color: white;\n"
"\n"
"    background-color: #464646;\n"
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
"\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: red;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 0px;\n"
"    padding-left: 0px;\n"
"\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: rgb(67, 131, 202);\n"
"}\n"
"\n"
"QComboBox:!on\n"
"{\n"
"\n"
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
"\n"
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
        self.einweisung_geraete_combo_standard.setObjectName("einweisung_geraete_combo_standard")
        self.gridLayout_27.addWidget(self.einweisung_geraete_combo_standard, 4, 3, 1, 1)
        self.line_27 = QtWidgets.QFrame(self.tab_15)
        self.line_27.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_27.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_27.setObjectName("line_27")
        self.gridLayout_27.addWidget(self.line_27, 3, 2, 8, 1)
        self.einweisung_tabelle = QtWidgets.QTableWidget(self.tab_15)
        self.einweisung_tabelle.setStyleSheet("QTableView {\n"
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
        self.einweisung_tabelle.setObjectName("einweisung_tabelle")
        self.einweisung_tabelle.setColumnCount(6)
        self.einweisung_tabelle.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.einweisung_tabelle.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.einweisung_tabelle.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.einweisung_tabelle.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.einweisung_tabelle.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.einweisung_tabelle.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.einweisung_tabelle.setHorizontalHeaderItem(5, item)
        self.einweisung_tabelle.horizontalHeader().setCascadingSectionResizes(True)
        self.einweisung_tabelle.horizontalHeader().setStretchLastSection(True)
        self.einweisung_tabelle.verticalHeader().setVisible(False)
        self.einweisung_tabelle.verticalHeader().setHighlightSections(True)
        self.gridLayout_27.addWidget(self.einweisung_tabelle, 12, 0, 1, 5)
        self.einweisung_standardwerte_loeschen_btn = QtWidgets.QPushButton(self.tab_15)
        self.einweisung_standardwerte_loeschen_btn.setStyleSheet("QPushButton{\n"
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
        self.einweisung_standardwerte_loeschen_btn.setObjectName("einweisung_standardwerte_loeschen_btn")
        self.gridLayout_27.addWidget(self.einweisung_standardwerte_loeschen_btn, 10, 3, 1, 1)
        self.label_69 = QtWidgets.QLabel(self.tab_15)
        self.label_69.setObjectName("label_69")
        self.gridLayout_27.addWidget(self.label_69, 8, 1, 1, 1)
        self.label_72 = QtWidgets.QLabel(self.tab_15)
        self.label_72.setObjectName("label_72")
        self.gridLayout_27.addWidget(self.label_72, 4, 4, 1, 1)
        self.label_76 = QtWidgets.QLabel(self.tab_15)
        self.label_76.setObjectName("label_76")
        self.gridLayout_27.addWidget(self.label_76, 8, 4, 1, 1)
        self.einweisung_datum = QtWidgets.QLineEdit(self.tab_15)
        self.einweisung_datum.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.einweisung_datum.setObjectName("einweisung_datum")
        self.gridLayout_27.addWidget(self.einweisung_datum, 6, 0, 1, 1)
        self.label_71 = QtWidgets.QLabel(self.tab_15)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_71.setFont(font)
        self.label_71.setObjectName("label_71")
        self.gridLayout_27.addWidget(self.label_71, 0, 3, 1, 1)
        self.label_85 = QtWidgets.QLabel(self.tab_15)
        self.label_85.setObjectName("label_85")
        self.gridLayout_27.addWidget(self.label_85, 14, 4, 1, 1)
        self.label_65 = QtWidgets.QLabel(self.tab_15)
        self.label_65.setObjectName("label_65")
        self.gridLayout_27.addWidget(self.label_65, 4, 1, 1, 1)
        self.einweisung_ma_standard_combo = QtWidgets.QComboBox(self.tab_15)
        self.einweisung_ma_standard_combo.setStyleSheet("QComboBox\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    selection-background-color: #111;\n"
"    selection-color: white;\n"
"\n"
"    background-color: #464646;\n"
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
"\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: red;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 0px;\n"
"    padding-left: 0px;\n"
"\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: rgb(67, 131, 202);\n"
"}\n"
"\n"
"QComboBox:!on\n"
"{\n"
"\n"
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
"\n"
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
        self.einweisung_ma_standard_combo.setObjectName("einweisung_ma_standard_combo")
        self.gridLayout_27.addWidget(self.einweisung_ma_standard_combo, 7, 3, 1, 1)
        self.label_64 = QtWidgets.QLabel(self.tab_15)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_64.setFont(font)
        self.label_64.setObjectName("label_64")
        self.gridLayout_27.addWidget(self.label_64, 0, 0, 1, 1)
        self.label_68 = QtWidgets.QLabel(self.tab_15)
        self.label_68.setObjectName("label_68")
        self.gridLayout_27.addWidget(self.label_68, 7, 1, 1, 1)
        self.einweisung_original = QtWidgets.QLineEdit(self.tab_15)
        self.einweisung_original.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.einweisung_original.setObjectName("einweisung_original")
        self.gridLayout_27.addWidget(self.einweisung_original, 9, 0, 1, 1)
        self.einweisung_tabelle_filtern_anzahl = QtWidgets.QLabel(self.tab_15)
        self.einweisung_tabelle_filtern_anzahl.setText("")
        self.einweisung_tabelle_filtern_anzahl.setObjectName("einweisung_tabelle_filtern_anzahl")
        self.gridLayout_27.addWidget(self.einweisung_tabelle_filtern_anzahl, 16, 1, 1, 1)
        self.einweisung_softwareversion_standard = QtWidgets.QLineEdit(self.tab_15)
        self.einweisung_softwareversion_standard.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.einweisung_softwareversion_standard.setObjectName("einweisung_softwareversion_standard")
        self.gridLayout_27.addWidget(self.einweisung_softwareversion_standard, 5, 3, 1, 1)
        self.einweisung_geraete_combo = QtWidgets.QComboBox(self.tab_15)
        self.einweisung_geraete_combo.setStyleSheet("QComboBox{\n"
"subcontrol-origin: padding;\n"
"subcontrol-position: top right;\n"
" selection-background-color: #111;\n"
"selection-color: white;\n"
" color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
" border-style: solid;\n"
" border: 1px solid #1e1e1e;\n"
" border-radius: 5;\n"
" padding: 1px 0px 1px 20px;\n"
"}\n"
"QComboBox:hover, QPushButton:hover\n"
"{\n"
"border: 1px solid teal;\n"
"color: white;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"background: red;\n"
" color: pink;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"padding-top: 0px;\n"
" padding-left: 0px;\n"
" color: white;\n"
" background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"selection-background-color: rgb(67, 131, 202);\n"
"}\n"
"\n"
"QComboBox:!on\n"
"{\n"
"color: white;\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #666, stop: 0.1 #555, stop: 0.5 #555, stop: 0.9 #444, stop: 1 #333);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"border: 2px solid darkgray;\n"
" color: black;\n"
" selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #111, stop: 1 #333);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"subcontrol-origin: padding;\n"
" subcontrol-position: top right;\n"
"width: 15px;\n"
" color: white;\n"
"border-left-width: 1px;\n"
"border-left-color: darkgray;\n"
" border-left-style: solid;\n"
"  border-top-right-radius: 3px; \n"
" border-bottom-right-radius: 3px;\n"
" padding-left: 10px;\n"
" }")
        self.einweisung_geraete_combo.setObjectName("einweisung_geraete_combo")
        self.gridLayout_27.addWidget(self.einweisung_geraete_combo, 4, 0, 1, 1)
        self.einweisung_tabelle_filtern_software_combo = QtWidgets.QComboBox(self.tab_15)
        self.einweisung_tabelle_filtern_software_combo.setStyleSheet("QComboBox\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    selection-background-color: #111;\n"
"    selection-color: white;\n"
"\n"
"    background-color: #464646;\n"
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
"\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: red;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 0px;\n"
"    padding-left: 0px;\n"
"\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: rgb(67, 131, 202);\n"
"}\n"
"\n"
"QComboBox:!on\n"
"{\n"
"\n"
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
"\n"
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
        self.einweisung_tabelle_filtern_software_combo.setObjectName("einweisung_tabelle_filtern_software_combo")
        self.gridLayout_27.addWidget(self.einweisung_tabelle_filtern_software_combo, 14, 3, 1, 1)
        self.einweisung_softwareversion = QtWidgets.QLineEdit(self.tab_15)
        self.einweisung_softwareversion.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.einweisung_softwareversion.setObjectName("einweisung_softwareversion")
        self.gridLayout_27.addWidget(self.einweisung_softwareversion, 5, 0, 1, 1)
        self.label_86 = QtWidgets.QLabel(self.tab_15)
        self.label_86.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_86.setObjectName("label_86")
        self.gridLayout_27.addWidget(self.label_86, 16, 0, 1, 1)
        self.label_73 = QtWidgets.QLabel(self.tab_15)
        self.label_73.setObjectName("label_73")
        self.gridLayout_27.addWidget(self.label_73, 5, 4, 1, 1)
        self.label_70 = QtWidgets.QLabel(self.tab_15)
        self.label_70.setObjectName("label_70")
        self.gridLayout_27.addWidget(self.label_70, 9, 1, 1, 1)
        self.einweisung_tabelle_filtern_geraet_combo = QtWidgets.QComboBox(self.tab_15)
        self.einweisung_tabelle_filtern_geraet_combo.setStyleSheet("QComboBox\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    selection-background-color: #111;\n"
"    selection-color: white;\n"
"\n"
"    background-color: #464646;\n"
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
"\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: red;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 0px;\n"
"    padding-left: 0px;\n"
"\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: rgb(67, 131, 202);\n"
"}\n"
"\n"
"QComboBox:!on\n"
"{\n"
"\n"
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
"\n"
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
        self.einweisung_tabelle_filtern_geraet_combo.setObjectName("einweisung_tabelle_filtern_geraet_combo")
        self.gridLayout_27.addWidget(self.einweisung_tabelle_filtern_geraet_combo, 14, 0, 1, 1)
        self.einweisung_tabelle_filtern_ma_combo = QtWidgets.QComboBox(self.tab_15)
        self.einweisung_tabelle_filtern_ma_combo.setStyleSheet("QComboBox\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    selection-background-color: #111;\n"
"    selection-color: white;\n"
"\n"
"    background-color: #464646;\n"
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
"\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: red;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 0px;\n"
"    padding-left: 0px;\n"
"\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: rgb(67, 131, 202);\n"
"}\n"
"\n"
"QComboBox:!on\n"
"{\n"
"\n"
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
"\n"
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
        self.einweisung_tabelle_filtern_ma_combo.setObjectName("einweisung_tabelle_filtern_ma_combo")
        self.gridLayout_27.addWidget(self.einweisung_tabelle_filtern_ma_combo, 15, 0, 1, 1)
        self.label_106 = QtWidgets.QLabel(self.tab_15)
        self.label_106.setObjectName("label_106")
        self.gridLayout_27.addWidget(self.label_106, 15, 1, 1, 1)
        self.tabWidget_3.addTab(self.tab_15, "")
        self.tab_18 = QtWidgets.QWidget()
        self.tab_18.setObjectName("tab_18")
        self.gridLayout_32 = QtWidgets.QGridLayout(self.tab_18)
        self.gridLayout_32.setObjectName("gridLayout_32")
        self.line_33 = QtWidgets.QFrame(self.tab_18)
        self.line_33.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_33.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_33.setObjectName("line_33")
        self.gridLayout_32.addWidget(self.line_33, 2, 0, 1, 1)
        self.line_34 = QtWidgets.QFrame(self.tab_18)
        self.line_34.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_34.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_34.setObjectName("line_34")
        self.gridLayout_32.addWidget(self.line_34, 3, 2, 3, 1)
        self.mpg_standort_text = QtWidgets.QLineEdit(self.tab_18)
        self.mpg_standort_text.setMaximumSize(QtCore.QSize(550, 16777215))
        self.mpg_standort_text.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.mpg_standort_text.setObjectName("mpg_standort_text")
        self.gridLayout_32.addWidget(self.mpg_standort_text, 3, 0, 1, 1)
        self.mpg_standort_speichern_btn = QtWidgets.QPushButton(self.tab_18)
        self.mpg_standort_speichern_btn.setMaximumSize(QtCore.QSize(550, 16777215))
        self.mpg_standort_speichern_btn.setStyleSheet("QPushButton{\n"
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
        self.mpg_standort_speichern_btn.setObjectName("mpg_standort_speichern_btn")
        self.gridLayout_32.addWidget(self.mpg_standort_speichern_btn, 4, 0, 1, 1)
        self.label_93 = QtWidgets.QLabel(self.tab_18)
        self.label_93.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_93.setStyleSheet("")
        self.label_93.setObjectName("label_93")
        self.gridLayout_32.addWidget(self.label_93, 0, 0, 1, 1)
        self.line_35 = QtWidgets.QFrame(self.tab_18)
        self.line_35.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_35.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_35.setObjectName("line_35")
        self.gridLayout_32.addWidget(self.line_35, 2, 3, 1, 1)
        self.mpg_standorte_combo = QtWidgets.QComboBox(self.tab_18)
        self.mpg_standorte_combo.setStyleSheet("QComboBox\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    selection-background-color: #111;\n"
"    selection-color: white;\n"
"\n"
"    background-color: #464646;\n"
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
"\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: red;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 0px;\n"
"    padding-left: 0px;\n"
"\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: rgb(67, 131, 202);\n"
"}\n"
"\n"
"QComboBox:!on\n"
"{\n"
"\n"
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
"\n"
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
        self.mpg_standorte_combo.setObjectName("mpg_standorte_combo")
        self.gridLayout_32.addWidget(self.mpg_standorte_combo, 3, 3, 1, 1)
        self.mpg_standorte_tabelle = QtWidgets.QTableWidget(self.tab_18)
        self.mpg_standorte_tabelle.setMaximumSize(QtCore.QSize(550, 16777215))
        self.mpg_standorte_tabelle.setStyleSheet("QTableView {\n"
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
        self.mpg_standorte_tabelle.setObjectName("mpg_standorte_tabelle")
        self.mpg_standorte_tabelle.setColumnCount(1)
        self.mpg_standorte_tabelle.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.mpg_standorte_tabelle.setHorizontalHeaderItem(0, item)
        self.mpg_standorte_tabelle.horizontalHeader().setCascadingSectionResizes(True)
        self.mpg_standorte_tabelle.horizontalHeader().setStretchLastSection(True)
        self.mpg_standorte_tabelle.verticalHeader().setVisible(False)
        self.gridLayout_32.addWidget(self.mpg_standorte_tabelle, 5, 0, 1, 1)
        self.mpg_standorte_loeschen_btn = QtWidgets.QPushButton(self.tab_18)
        self.mpg_standorte_loeschen_btn.setStyleSheet("QPushButton{\n"
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
        self.mpg_standorte_loeschen_btn.setObjectName("mpg_standorte_loeschen_btn")
        self.gridLayout_32.addWidget(self.mpg_standorte_loeschen_btn, 4, 3, 1, 1)
        self.label_94 = QtWidgets.QLabel(self.tab_18)
        self.label_94.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_94.setObjectName("label_94")
        self.gridLayout_32.addWidget(self.label_94, 3, 1, 1, 1)
        self.label_97 = QtWidgets.QLabel(self.tab_18)
        self.label_97.setObjectName("label_97")
        self.gridLayout_32.addWidget(self.label_97, 0, 3, 1, 1)
        self.tabWidget_3.addTab(self.tab_18, "")
        self.gridLayout_26.addWidget(self.tabWidget_3, 0, 0, 1, 1)
        self.admin_bereich.addTab(self.tab_13, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.tab_12)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.pw_aendern_altes_pw = QtWidgets.QLineEdit(self.tab_12)
        self.pw_aendern_altes_pw.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.pw_aendern_altes_pw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pw_aendern_altes_pw.setObjectName("pw_aendern_altes_pw")
        self.gridLayout_25.addWidget(self.pw_aendern_altes_pw, 4, 0, 1, 1)
        self.label_53 = QtWidgets.QLabel(self.tab_12)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_53.setFont(font)
        self.label_53.setObjectName("label_53")
        self.gridLayout_25.addWidget(self.label_53, 1, 6, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.tab_12)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.gridLayout_25.addWidget(self.label_44, 1, 0, 1, 1)
        self.neuer_admin_speichern = QtWidgets.QPushButton(self.tab_12)
        self.neuer_admin_speichern.setStyleSheet("QPushButton{\n"
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
        self.neuer_admin_speichern.setObjectName("neuer_admin_speichern")
        self.gridLayout_25.addWidget(self.neuer_admin_speichern, 8, 3, 1, 1)
        self.line_21 = QtWidgets.QFrame(self.tab_12)
        self.line_21.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.gridLayout_25.addWidget(self.line_21, 3, 5, 6, 1)
        self.neuer_admin_pw_wied = QtWidgets.QLineEdit(self.tab_12)
        self.neuer_admin_pw_wied.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.neuer_admin_pw_wied.setEchoMode(QtWidgets.QLineEdit.Password)
        self.neuer_admin_pw_wied.setObjectName("neuer_admin_pw_wied")
        self.gridLayout_25.addWidget(self.neuer_admin_pw_wied, 6, 3, 1, 1)
        self.pw_aendern_neues_pw_wied = QtWidgets.QLineEdit(self.tab_12)
        self.pw_aendern_neues_pw_wied.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.pw_aendern_neues_pw_wied.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pw_aendern_neues_pw_wied.setObjectName("pw_aendern_neues_pw_wied")
        self.gridLayout_25.addWidget(self.pw_aendern_neues_pw_wied, 6, 0, 1, 1)
        self.pw_aendern_speichern = QtWidgets.QPushButton(self.tab_12)
        self.pw_aendern_speichern.setStyleSheet("QPushButton{\n"
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
        self.pw_aendern_speichern.setObjectName("pw_aendern_speichern")
        self.gridLayout_25.addWidget(self.pw_aendern_speichern, 8, 0, 1, 1)
        self.neuer_admin_name = QtWidgets.QLineEdit(self.tab_12)
        self.neuer_admin_name.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.neuer_admin_name.setObjectName("neuer_admin_name")
        self.gridLayout_25.addWidget(self.neuer_admin_name, 4, 3, 1, 1)
        self.neuer_admin_pw = QtWidgets.QLineEdit(self.tab_12)
        self.neuer_admin_pw.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.neuer_admin_pw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.neuer_admin_pw.setObjectName("neuer_admin_pw")
        self.gridLayout_25.addWidget(self.neuer_admin_pw, 5, 3, 1, 1)
        self.label_54 = QtWidgets.QLabel(self.tab_12)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_54.setFont(font)
        self.label_54.setObjectName("label_54")
        self.gridLayout_25.addWidget(self.label_54, 10, 3, 1, 1)
        self.admin_loeschen_pw = QtWidgets.QLineEdit(self.tab_12)
        self.admin_loeschen_pw.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.admin_loeschen_pw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.admin_loeschen_pw.setObjectName("admin_loeschen_pw")
        self.gridLayout_25.addWidget(self.admin_loeschen_pw, 5, 6, 1, 1)
        self.admin_loeschen_combo = QtWidgets.QComboBox(self.tab_12)
        self.admin_loeschen_combo.setStyleSheet("QComboBox\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    selection-background-color: #111;\n"
"    selection-color: white;\n"
"\n"
"    background-color: #464646;\n"
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
"\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: red;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 0px;\n"
"    padding-left: 0px;\n"
"\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: rgb(67, 131, 202);\n"
"}\n"
"\n"
"QComboBox:!on\n"
"{\n"
"\n"
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
"\n"
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
        self.admin_loeschen_combo.setObjectName("admin_loeschen_combo")
        self.gridLayout_25.addWidget(self.admin_loeschen_combo, 4, 6, 1, 1)
        self.label_48 = QtWidgets.QLabel(self.tab_12)
        self.label_48.setObjectName("label_48")
        self.gridLayout_25.addWidget(self.label_48, 4, 4, 1, 1)
        self.line_19 = QtWidgets.QFrame(self.tab_12)
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.gridLayout_25.addWidget(self.line_19, 3, 6, 1, 1)
        self.label_52 = QtWidgets.QLabel(self.tab_12)
        self.label_52.setObjectName("label_52")
        self.gridLayout_25.addWidget(self.label_52, 5, 7, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.tab_12)
        self.label_45.setObjectName("label_45")
        self.gridLayout_25.addWidget(self.label_45, 4, 1, 1, 1)
        self.label_49 = QtWidgets.QLabel(self.tab_12)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.gridLayout_25.addWidget(self.label_49, 1, 3, 1, 1)
        self.label_50 = QtWidgets.QLabel(self.tab_12)
        self.label_50.setObjectName("label_50")
        self.gridLayout_25.addWidget(self.label_50, 5, 4, 1, 1)
        self.line_20 = QtWidgets.QFrame(self.tab_12)
        self.line_20.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.gridLayout_25.addWidget(self.line_20, 3, 2, 6, 1)
        self.line_22 = QtWidgets.QFrame(self.tab_12)
        self.line_22.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.gridLayout_25.addWidget(self.line_22, 9, 3, 1, 1)
        self.label_51 = QtWidgets.QLabel(self.tab_12)
        self.label_51.setObjectName("label_51")
        self.gridLayout_25.addWidget(self.label_51, 6, 4, 1, 1)
        self.pw_aendern_neues_pw = QtWidgets.QLineEdit(self.tab_12)
        self.pw_aendern_neues_pw.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.pw_aendern_neues_pw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pw_aendern_neues_pw.setObjectName("pw_aendern_neues_pw")
        self.gridLayout_25.addWidget(self.pw_aendern_neues_pw, 5, 0, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.tab_12)
        self.label_47.setObjectName("label_47")
        self.gridLayout_25.addWidget(self.label_47, 6, 1, 1, 1)
        self.line_16 = QtWidgets.QFrame(self.tab_12)
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.gridLayout_25.addWidget(self.line_16, 3, 3, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_25.addItem(spacerItem22, 12, 0, 1, 1)
        self.label_46 = QtWidgets.QLabel(self.tab_12)
        self.label_46.setObjectName("label_46")
        self.gridLayout_25.addWidget(self.label_46, 5, 1, 1, 1)
        self.tabelle_alle_admins = QtWidgets.QTableWidget(self.tab_12)
        self.tabelle_alle_admins.setStyleSheet("QTableView {\n"
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
        self.tabelle_alle_admins.setObjectName("tabelle_alle_admins")
        self.tabelle_alle_admins.setColumnCount(1)
        self.tabelle_alle_admins.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabelle_alle_admins.setHorizontalHeaderItem(0, item)
        self.tabelle_alle_admins.horizontalHeader().setCascadingSectionResizes(True)
        self.tabelle_alle_admins.horizontalHeader().setStretchLastSection(True)
        self.tabelle_alle_admins.verticalHeader().setVisible(False)
        self.tabelle_alle_admins.verticalHeader().setHighlightSections(False)
        self.gridLayout_25.addWidget(self.tabelle_alle_admins, 11, 3, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.tab_12)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_25.addWidget(self.line_7, 3, 0, 1, 1)
        self.pw_aendern_label = QtWidgets.QLabel(self.tab_12)
        self.pw_aendern_label.setText("")
        self.pw_aendern_label.setObjectName("pw_aendern_label")
        self.gridLayout_25.addWidget(self.pw_aendern_label, 7, 0, 1, 1)
        self.neuer_admin_label = QtWidgets.QLabel(self.tab_12)
        self.neuer_admin_label.setText("")
        self.neuer_admin_label.setObjectName("neuer_admin_label")
        self.gridLayout_25.addWidget(self.neuer_admin_label, 7, 3, 1, 1)
        self.admin_loeschen_label = QtWidgets.QLabel(self.tab_12)
        self.admin_loeschen_label.setText("")
        self.admin_loeschen_label.setObjectName("admin_loeschen_label")
        self.gridLayout_25.addWidget(self.admin_loeschen_label, 6, 6, 1, 1)
        self.admin_loeschen_speichern = QtWidgets.QPushButton(self.tab_12)
        self.admin_loeschen_speichern.setStyleSheet("QPushButton{\n"
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
        self.admin_loeschen_speichern.setObjectName("admin_loeschen_speichern")
        self.gridLayout_25.addWidget(self.admin_loeschen_speichern, 7, 6, 1, 1)
        self.admin_bereich.addTab(self.tab_12, "")
        self.tab_20 = QtWidgets.QWidget()
        self.tab_20.setObjectName("tab_20")
        self.gridLayout_35 = QtWidgets.QGridLayout(self.tab_20)
        self.gridLayout_35.setObjectName("gridLayout_35")
        self.ma_neu_vorname_text = QtWidgets.QLineEdit(self.tab_20)
        self.ma_neu_vorname_text.setMaximumSize(QtCore.QSize(400, 16777215))
        self.ma_neu_vorname_text.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.ma_neu_vorname_text.setObjectName("ma_neu_vorname_text")
        self.gridLayout_35.addWidget(self.ma_neu_vorname_text, 4, 0, 1, 1)
        self.ma_neu_nachname_text = QtWidgets.QLineEdit(self.tab_20)
        self.ma_neu_nachname_text.setMaximumSize(QtCore.QSize(400, 16777215))
        self.ma_neu_nachname_text.setStyleSheet("QLineEdit{ background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #929394, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"border: 1px inset darkgrey;\n"
"border-radius: 10px;\n"
"padding: 0 8px;\n"
"selection-background-color: darkgray;\n"
"font-size: 13px;\n"
"color: white;\n"
"}\n"
"QLineEdit:focus { background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 0.1 #bababa, stop: 0.5 #919191, stop: 0.9 #7a7a7a, stop: 1 #5b5b5b);}\n"
"")
        self.ma_neu_nachname_text.setObjectName("ma_neu_nachname_text")
        self.gridLayout_35.addWidget(self.ma_neu_nachname_text, 5, 0, 1, 1)
        self.line_38 = QtWidgets.QFrame(self.tab_20)
        self.line_38.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_38.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_38.setObjectName("line_38")
        self.gridLayout_35.addWidget(self.line_38, 4, 2, 3, 1)
        self.label_104 = QtWidgets.QLabel(self.tab_20)
        self.label_104.setObjectName("label_104")
        self.gridLayout_35.addWidget(self.label_104, 5, 1, 1, 1)
        self.line_37 = QtWidgets.QFrame(self.tab_20)
        self.line_37.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_37.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_37.setObjectName("line_37")
        self.gridLayout_35.addWidget(self.line_37, 3, 0, 1, 1)
        self.label_103 = QtWidgets.QLabel(self.tab_20)
        self.label_103.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_103.setObjectName("label_103")
        self.gridLayout_35.addWidget(self.label_103, 4, 1, 1, 1)
        self.ma_neu_speichern_btn = QtWidgets.QPushButton(self.tab_20)
        self.ma_neu_speichern_btn.setStyleSheet("QPushButton{\n"
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
        self.ma_neu_speichern_btn.setObjectName("ma_neu_speichern_btn")
        self.gridLayout_35.addWidget(self.ma_neu_speichern_btn, 6, 0, 1, 1)
        self.label_102 = QtWidgets.QLabel(self.tab_20)
        self.label_102.setObjectName("label_102")
        self.gridLayout_35.addWidget(self.label_102, 0, 0, 1, 1)
        self.ma_loeschen_combo = QtWidgets.QComboBox(self.tab_20)
        self.ma_loeschen_combo.setStyleSheet("QComboBox\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    selection-background-color: #111;\n"
"    selection-color: white;\n"
"\n"
"    background-color: #464646;\n"
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
"\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: red;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 0px;\n"
"    padding-left: 0px;\n"
"\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: rgb(67, 131, 202);\n"
"}\n"
"\n"
"QComboBox:!on\n"
"{\n"
"\n"
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
"\n"
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
        self.ma_loeschen_combo.setObjectName("ma_loeschen_combo")
        self.gridLayout_35.addWidget(self.ma_loeschen_combo, 4, 3, 1, 1)
        self.ma_loeschen_btn = QtWidgets.QPushButton(self.tab_20)
        self.ma_loeschen_btn.setStyleSheet("QPushButton{\n"
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
        self.ma_loeschen_btn.setObjectName("ma_loeschen_btn")
        self.gridLayout_35.addWidget(self.ma_loeschen_btn, 5, 3, 1, 1)
        self.line_39 = QtWidgets.QFrame(self.tab_20)
        self.line_39.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_39.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_39.setObjectName("line_39")
        self.gridLayout_35.addWidget(self.line_39, 3, 3, 1, 1)
        self.label_105 = QtWidgets.QLabel(self.tab_20)
        self.label_105.setObjectName("label_105")
        self.gridLayout_35.addWidget(self.label_105, 0, 3, 1, 1)
        self.ma_tabelle = QtWidgets.QTableWidget(self.tab_20)
        self.ma_tabelle.setStyleSheet("QTableView {\n"
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
        self.ma_tabelle.setObjectName("ma_tabelle")
        self.ma_tabelle.setColumnCount(3)
        self.ma_tabelle.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ma_tabelle.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ma_tabelle.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ma_tabelle.setHorizontalHeaderItem(2, item)
        self.ma_tabelle.horizontalHeader().setCascadingSectionResizes(True)
        self.ma_tabelle.horizontalHeader().setStretchLastSection(True)
        self.ma_tabelle.verticalHeader().setVisible(False)
        self.gridLayout_35.addWidget(self.ma_tabelle, 7, 0, 1, 4)
        self.admin_bereich.addTab(self.tab_20, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.tab_8)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.label_99 = QtWidgets.QLabel(self.tab_8)
        self.label_99.setText("")
        self.label_99.setObjectName("label_99")
        self.gridLayout_19.addWidget(self.label_99, 2, 5, 1, 1)
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
        self.check_uebersicht = QtWidgets.QCheckBox(self.tab_8)
        self.check_uebersicht.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.check_uebersicht.setStyleSheet("color:#ffffff")
        self.check_uebersicht.setObjectName("check_uebersicht")
        self.gridLayout_19.addWidget(self.check_uebersicht, 1, 0, 1, 1)
        self.check_lager = QtWidgets.QCheckBox(self.tab_8)
        self.check_lager.setStyleSheet("color:#ffffff")
        self.check_lager.setObjectName("check_lager")
        self.gridLayout_19.addWidget(self.check_lager, 2, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.tab_8)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_19.addWidget(self.line, 0, 2, 5, 1)
        self.pdf_speicheror_btn = QtWidgets.QPushButton(self.tab_8)
        self.pdf_speicheror_btn.setMaximumSize(QtCore.QSize(300, 16777215))
        self.pdf_speicheror_btn.setStyleSheet("QPushButton{\n"
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
        self.pdf_speicheror_btn.setObjectName("pdf_speicheror_btn")
        self.gridLayout_19.addWidget(self.pdf_speicheror_btn, 2, 3, 1, 1)
        self.label_96 = QtWidgets.QLabel(self.tab_8)
        self.label_96.setText("")
        self.label_96.setObjectName("label_96")
        self.gridLayout_19.addWidget(self.label_96, 2, 4, 1, 1)
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
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_19.addItem(spacerItem23, 2, 7, 1, 1)
        self.check_dienstbekleidung = QtWidgets.QCheckBox(self.tab_8)
        self.check_dienstbekleidung.setStyleSheet("color:#ffffff")
        self.check_dienstbekleidung.setObjectName("check_dienstbekleidung")
        self.gridLayout_19.addWidget(self.check_dienstbekleidung, 4, 0, 1, 1)
        self.check_fahrzeuge = QtWidgets.QCheckBox(self.tab_8)
        self.check_fahrzeuge.setStyleSheet("color:#ffffff")
        self.check_fahrzeuge.setObjectName("check_fahrzeuge")
        self.gridLayout_19.addWidget(self.check_fahrzeuge, 3, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.tab_8)
        self.label_18.setObjectName("label_18")
        self.gridLayout_19.addWidget(self.label_18, 0, 0, 1, 1)
        self.label_98 = QtWidgets.QLabel(self.tab_8)
        self.label_98.setObjectName("label_98")
        self.gridLayout_19.addWidget(self.label_98, 0, 3, 1, 1)
        self.label_100 = QtWidgets.QLabel(self.tab_8)
        self.label_100.setMinimumSize(QtCore.QSize(30, 0))
        self.label_100.setText("")
        self.label_100.setObjectName("label_100")
        self.gridLayout_19.addWidget(self.label_100, 2, 6, 1, 1)
        self.pdf_speicherort_label = QtWidgets.QLabel(self.tab_8)
        self.pdf_speicherort_label.setText("")
        self.pdf_speicherort_label.setObjectName("pdf_speicherort_label")
        self.gridLayout_19.addWidget(self.pdf_speicherort_label, 1, 3, 1, 4)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_19.addItem(spacerItem24, 7, 0, 1, 1)
        self.admin_bereich.addTab(self.tab_8, "")
        self.admin_login.addWidget(self.admin_bereich, 6, 0, 1, 4)
        self.gridLayout_16.addLayout(self.admin_login, 1, 3, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.gridLayout_11.addWidget(self.tabWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1388, 26))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(5)
        self.admin_bereich.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(2)
        self.tabWidget_3.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.admin_text_ben, self.admin_text_pw)
        MainWindow.setTabOrder(self.admin_text_pw, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.uebersicht_lager_table)
        MainWindow.setTabOrder(self.uebersicht_lager_table, self.combobox_lager)
        MainWindow.setTabOrder(self.combobox_lager, self.lager_textfeld_einsatz)
        MainWindow.setTabOrder(self.lager_textfeld_einsatz, self.lager_textfeld_produkt)
        MainWindow.setTabOrder(self.lager_textfeld_produkt, self.lager_uebernehmen_btn)
        MainWindow.setTabOrder(self.lager_uebernehmen_btn, self.lager_table)
        MainWindow.setTabOrder(self.lager_table, self.lager_btn)
        MainWindow.setTabOrder(self.lager_btn, self.lager_eintrag_loeschen)
        MainWindow.setTabOrder(self.lager_eintrag_loeschen, self.lager_tabelle_leeren)
        MainWindow.setTabOrder(self.lager_tabelle_leeren, self.combo_rtw)
        MainWindow.setTabOrder(self.combo_rtw, self.combo_zustand)
        MainWindow.setTabOrder(self.combo_zustand, self.fahrzeug_textedit)
        MainWindow.setTabOrder(self.fahrzeug_textedit, self.button_fahrzeuge)
        MainWindow.setTabOrder(self.button_fahrzeuge, self.mpg_Fahrzeuge_combo)
        MainWindow.setTabOrder(self.mpg_Fahrzeuge_combo, self.mpg_geraete_tabelle_fahrzeug)
        MainWindow.setTabOrder(self.mpg_geraete_tabelle_fahrzeug, self.mpg_user_geraete_barcode)
        MainWindow.setTabOrder(self.mpg_user_geraete_barcode, self.mpg_user_geraete_aufrufen_btn)
        MainWindow.setTabOrder(self.mpg_user_geraete_aufrufen_btn, self.mpg_user_geraete_standort_combo)
        MainWindow.setTabOrder(self.mpg_user_geraete_standort_combo, self.mpg_user_bemerkung)
        MainWindow.setTabOrder(self.mpg_user_bemerkung, self.mpg_user_geraete_speichern_btn)
        MainWindow.setTabOrder(self.mpg_user_geraete_speichern_btn, self.klamotten_textfeld)
        MainWindow.setTabOrder(self.klamotten_textfeld, self.aufnahme)
        MainWindow.setTabOrder(self.aufnahme, self.klamotten_button)
        MainWindow.setTabOrder(self.klamotten_button, self.klamotten_tabelle)
        MainWindow.setTabOrder(self.klamotten_tabelle, self.kleidung_zurueck_tabelle)
        MainWindow.setTabOrder(self.kleidung_zurueck_tabelle, self.admin_bereich)
        MainWindow.setTabOrder(self.admin_bereich, self.tabWidget_2)
        MainWindow.setTabOrder(self.tabWidget_2, self.admin_lager_alle_produkte)
        MainWindow.setTabOrder(self.admin_lager_alle_produkte, self.admin_produkte_update)
        MainWindow.setTabOrder(self.admin_produkte_update, self.admin_new_prod_prod)
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
        MainWindow.setTabOrder(self.admin_del_prod_btn, self.admin_lager_fehlendes_material)
        MainWindow.setTabOrder(self.admin_lager_fehlendes_material, self.lager_bestellung)
        MainWindow.setTabOrder(self.lager_bestellung, self.pdf_erstellen)
        MainWindow.setTabOrder(self.pdf_erstellen, self.admin_material_speichern_barcode)
        MainWindow.setTabOrder(self.admin_material_speichern_barcode, self.admin_material_speichern_anzahl)
        MainWindow.setTabOrder(self.admin_material_speichern_anzahl, self.admin_material_speichern_combo)
        MainWindow.setTabOrder(self.admin_material_speichern_combo, self.admin_material_speichern_table)
        MainWindow.setTabOrder(self.admin_material_speichern_table, self.admin_material_speichern_button)
        MainWindow.setTabOrder(self.admin_material_speichern_button, self.fahrzeug_admin_funkkenn)
        MainWindow.setTabOrder(self.fahrzeug_admin_funkkenn, self.fahrzeug_admin_kennz)
        MainWindow.setTabOrder(self.fahrzeug_admin_kennz, self.fahrzeug_admin_ort)
        MainWindow.setTabOrder(self.fahrzeug_admin_ort, self.fahrzeug_admin_tuev)
        MainWindow.setTabOrder(self.fahrzeug_admin_tuev, self.fahrzeug_admin_save_btn)
        MainWindow.setTabOrder(self.fahrzeug_admin_save_btn, self.tabWidget_3)
        MainWindow.setTabOrder(self.tabWidget_3, self.verwertet_geraete_combo)
        MainWindow.setTabOrder(self.verwertet_geraete_combo, self.verwertet_datum)
        MainWindow.setTabOrder(self.verwertet_datum, self.verwertet_bemerkung)
        MainWindow.setTabOrder(self.verwertet_bemerkung, self.verwertet_speichern_button)
        MainWindow.setTabOrder(self.verwertet_speichern_button, self.verwertet_tabelle)
        MainWindow.setTabOrder(self.verwertet_tabelle, self.einweisung_geraete_combo)
        MainWindow.setTabOrder(self.einweisung_geraete_combo, self.einweisung_softwareversion)
        MainWindow.setTabOrder(self.einweisung_softwareversion, self.einweisung_datum)
        MainWindow.setTabOrder(self.einweisung_datum, self.einweisung_einweisender)
        MainWindow.setTabOrder(self.einweisung_einweisender, self.einweisung_original)
        MainWindow.setTabOrder(self.einweisung_original, self.einweisung_speichern_btn)
        MainWindow.setTabOrder(self.einweisung_speichern_btn, self.einweisung_tabelle)
        MainWindow.setTabOrder(self.einweisung_tabelle, self.einweisung_tabelle_filtern_geraet_combo)
        MainWindow.setTabOrder(self.einweisung_tabelle_filtern_geraet_combo, self.einweisung_tabelle_filtern_software_combo)
        MainWindow.setTabOrder(self.einweisung_tabelle_filtern_software_combo, self.einweisung_geraete_combo_standard)
        MainWindow.setTabOrder(self.einweisung_geraete_combo_standard, self.einweisung_softwareversion_standard)
        MainWindow.setTabOrder(self.einweisung_softwareversion_standard, self.einweisung_datum_standard)
        MainWindow.setTabOrder(self.einweisung_datum_standard, self.einweisung_einweisender_standard)
        MainWindow.setTabOrder(self.einweisung_einweisender_standard, self.einweisung_original_standard)
        MainWindow.setTabOrder(self.einweisung_original_standard, self.einweisung_standardwerte_loeschen_btn)
        MainWindow.setTabOrder(self.einweisung_standardwerte_loeschen_btn, self.mpg_standort_text)
        MainWindow.setTabOrder(self.mpg_standort_text, self.mpg_standort_speichern_btn)
        MainWindow.setTabOrder(self.mpg_standort_speichern_btn, self.mpg_standorte_tabelle)
        MainWindow.setTabOrder(self.mpg_standorte_tabelle, self.mpg_standorte_combo)
        MainWindow.setTabOrder(self.mpg_standorte_combo, self.mpg_standorte_loeschen_btn)
        MainWindow.setTabOrder(self.mpg_standorte_loeschen_btn, self.pw_aendern_altes_pw)
        MainWindow.setTabOrder(self.pw_aendern_altes_pw, self.pw_aendern_neues_pw)
        MainWindow.setTabOrder(self.pw_aendern_neues_pw, self.pw_aendern_neues_pw_wied)
        MainWindow.setTabOrder(self.pw_aendern_neues_pw_wied, self.pw_aendern_speichern)
        MainWindow.setTabOrder(self.pw_aendern_speichern, self.neuer_admin_name)
        MainWindow.setTabOrder(self.neuer_admin_name, self.neuer_admin_pw)
        MainWindow.setTabOrder(self.neuer_admin_pw, self.neuer_admin_pw_wied)
        MainWindow.setTabOrder(self.neuer_admin_pw_wied, self.neuer_admin_speichern)
        MainWindow.setTabOrder(self.neuer_admin_speichern, self.admin_loeschen_combo)
        MainWindow.setTabOrder(self.admin_loeschen_combo, self.admin_loeschen_pw)
        MainWindow.setTabOrder(self.admin_loeschen_pw, self.admin_loeschen_speichern)
        MainWindow.setTabOrder(self.admin_loeschen_speichern, self.tabelle_alle_admins)
        MainWindow.setTabOrder(self.tabelle_alle_admins, self.check_uebersicht)
        MainWindow.setTabOrder(self.check_uebersicht, self.check_lager)
        MainWindow.setTabOrder(self.check_lager, self.check_fahrzeuge)
        MainWindow.setTabOrder(self.check_fahrzeuge, self.check_dienstbekleidung)
        MainWindow.setTabOrder(self.check_dienstbekleidung, self.einstellungen_speichern)
        MainWindow.setTabOrder(self.einstellungen_speichern, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.login_btn)
        MainWindow.setTabOrder(self.login_btn, self.admin_logout_btn)
        MainWindow.setTabOrder(self.admin_logout_btn, self.geraete_verwalten_standort_combo)
        MainWindow.setTabOrder(self.geraete_verwalten_standort_combo, self.geraete_verwalten_speichern_button)
        MainWindow.setTabOrder(self.geraete_verwalten_speichern_button, self.geraete_verwalten_geraet)
        MainWindow.setTabOrder(self.geraete_verwalten_geraet, self.geraete_verwalten_inventarnummer)
        MainWindow.setTabOrder(self.geraete_verwalten_inventarnummer, self.geraete_verwalten_ce)
        MainWindow.setTabOrder(self.geraete_verwalten_ce, self.geraete_verwalten_geraetenummer)
        MainWindow.setTabOrder(self.geraete_verwalten_geraetenummer, self.mpg_geraete_tabelle)
        MainWindow.setTabOrder(self.mpg_geraete_tabelle, self.geraete_verwalten_pruefdatum)
        MainWindow.setTabOrder(self.geraete_verwalten_pruefdatum, self.geraete_verwalten_prueffrist)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.uebersicht_lager_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Produkt"))
        item = self.uebersicht_lager_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Vorhanden"))
        item = self.uebersicht_lager_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mindestbestand"))
        item = self.uebersicht_lager_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Lager Übersicht</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Fahrzeug Übersicht</span></p></body></html>"))
        self.label_uebersicht_lager.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Übersicht"))
        self.label_einsatznummer.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Einsatznummer</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Produkt Barcode</span></p></body></html>"))
        self.combobox_lager.setItemText(0, _translate("MainWindow", "Auffüllen nach Einsatz"))
        self.combobox_lager.setItemText(1, _translate("MainWindow", "Auffüllen wegen Fehlbestand"))
        self.combobox_lager.setItemText(2, _translate("MainWindow", "Falsch Entnahme - wieder zurück geben"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Produkte austragen</span></p></body></html>"))
        item = self.lager_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Produkt"))
        item = self.lager_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Menge"))
        item = self.lager_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Keyword"))
        self.lager_btn.setText(_translate("MainWindow", "Speichern"))
        self.lager_uebernehmen_btn.setText(_translate("MainWindow", "Übernehmen"))
        self.lager_eintrag_loeschen.setText(_translate("MainWindow", "Eintrag löschen"))
        self.lager_tabelle_leeren.setText(_translate("MainWindow", "Tabelle leeren"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Lagerverwaltung"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Status der Fahrzeuge</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Fahrzeug</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "Bemerkung"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Zustand</span></p></body></html>"))
        self.button_fahrzeuge.setText(_translate("MainWindow", "Speichern"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Fahrzeug Status"))
        self.label_92.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Standort</span></p></body></html>"))
        self.mpg_user_geraete_aufrufen_btn.setText(_translate("MainWindow", "Aufrufen"))
        self.label_91.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Fahrzeug / Standort</span></p></body></html>"))
        item = self.mpg_geraete_tabelle_fahrzeug.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Gerät"))
        item = self.mpg_geraete_tabelle_fahrzeug.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Seriennummer"))
        item = self.mpg_geraete_tabelle_fahrzeug.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Barcode"))
        self.label_88.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Medizin Produkte nach Standorten / Fahrzeugen</span></p></body></html>"))
        self.mpg_user_geraete_speichern_btn.setText(_translate("MainWindow", "Speichern"))
        self.label_89.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Barcode</span></p></body></html>"))
        self.label_90.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Medizin Produkte Standort / Fahrzeug wechseln</span></p></body></html>"))
        self.label_95.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Bemerkung</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_17), _translate("MainWindow", "MPG"))
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
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Wäsche, die abgegeben wurde</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Dienstkleidung Eingang und Abgabe</span></p></body></html>"))
        self.klamotten_button.setText(_translate("MainWindow", "Wäsche Speichern"))
        item = self.aufnahme.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Barcode"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">mit Enter bestätigen</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Dienstkleidung"))
        self.admin_logout_btn.setText(_translate("MainWindow", "Logout"))
        self.benutzer_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Benutzername</span></p></body></html>"))
        self.login_btn.setText(_translate("MainWindow", "Login"))
        self.passwort_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Passwort</span></p></body></html>"))
        self.login_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Login</span></p></body></html>"))
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
        self.admin_lager_alle_produkte.setSortingEnabled(True)
        item = self.admin_lager_alle_produkte.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.admin_lager_alle_produkte.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "produkt"))
        item = self.admin_lager_alle_produkte.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "bestand"))
        item = self.admin_lager_alle_produkte.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Mindestbestand"))
        item = self.admin_lager_alle_produkte.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Maximal Bestand"))
        item = self.admin_lager_alle_produkte.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Barcode"))
        item = self.admin_lager_alle_produkte.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Packungs Inhalt"))
        item = self.admin_lager_alle_produkte.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "artikelnnummer"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Produkte</span></p></body></html>"))
        self.admin_produkte_update.setText(_translate("MainWindow", "Update"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_19), _translate("MainWindow", "Produkte Bearbeiten"))
        self.label_40.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Fehlendes Material</span></p></body></html>"))
        item = self.admin_lager_fehlendes_material.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Produkt"))
        item = self.admin_lager_fehlendes_material.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Vorhanden"))
        item = self.admin_lager_fehlendes_material.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Mindestbestand"))
        item = self.admin_lager_fehlendes_material.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Maximal Menge"))
        item = self.admin_lager_fehlendes_material.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Artikelnr"))
        item = self.admin_lager_fehlendes_material.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Status"))
        self.pdf_erstellen.setText(_translate("MainWindow", "PDF erstellen"))
        self.lager_bestellung.setText(_translate("MainWindow", "Bestellung online"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), _translate("MainWindow", "Fehlendes Material"))
        self.label_37.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Barcode</span></p></body></html>"))
        self.label_43.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Eingehendes Material</span></p></body></html>"))
        self.admin_material_speichern_button.setText(_translate("MainWindow", "Speichern"))
        self.label_42.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Produkt</span></p></body></html>"))
        self.label_41.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Anzahl</span></p></body></html>"))
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
        self.admin_bereich.setTabText(self.admin_bereich.indexOf(self.tab_7), _translate("MainWindow", "Fahrzeuge"))
        self.label_59.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Prüffrist in Monaten</span></p></body></html>"))
        self.label_56.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Seriennummer</span></p></body></html>"))
        self.label_58.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">letzte Prüfung</span></p></body></html>"))
        self.geraete_verwalten_speichern_button.setText(_translate("MainWindow", "Speichern"))
        self.label_63.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Geräte</span></p></body></html>"))
        self.label_55.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Gerät</span></p></body></html>"))
        self.geraete_verwalten_aenderung_speichern_btn.setText(_translate("MainWindow", "Änderungen Speichern"))
        self.label_61.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Standort</span></p></body></html>"))
        self.mpg_geraete_tabelle.setSortingEnabled(True)
        item = self.mpg_geraete_tabelle.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.mpg_geraete_tabelle.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Gerät"))
        item = self.mpg_geraete_tabelle.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Seriennummer"))
        item = self.mpg_geraete_tabelle.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Inventarnummer"))
        item = self.mpg_geraete_tabelle.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "CE Kennung"))
        item = self.mpg_geraete_tabelle.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Bemerkung"))
        item = self.mpg_geraete_tabelle.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Anschaffungsdatum"))
        item = self.mpg_geraete_tabelle.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Prüfdatum"))
        item = self.mpg_geraete_tabelle.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Prüffrist"))
        item = self.mpg_geraete_tabelle.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Nächste Prüfung"))
        item = self.mpg_geraete_tabelle.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Standort"))
        item = self.mpg_geraete_tabelle.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Artikel Nr."))
        self.label_57.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Inventarnummer</span></p></body></html>"))
        self.label_83.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Neues Gerät anlegen</span></p></body></html>"))
        self.label_62.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Geräte Verwalten</span></p></body></html>"))
        self.label_82.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">CE Kennung</span></p></body></html>"))
        self.geraet_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Artikel Nr.</span></p><p><br/></p></body></html>"))
        self.label_60.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Bemerkung</span></p></body></html>"))
        self.label_101.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Anschaffungsdatum</span></p></body></html>"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_14), _translate("MainWindow", "Geräte"))
        self.label_81.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Datum</span></p></body></html>"))
        self.verwertet_speichern_button.setText(_translate("MainWindow", "Speichern"))
        item = self.verwertet_tabelle.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Gerät / Seriennummer"))
        item = self.verwertet_tabelle.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Datum"))
        item = self.verwertet_tabelle.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Bemerkung"))
        self.label_79.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Verwerten / Entsorgen</span></p></body></html>"))
        self.label_80.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Gerät / Seriennummer</span></p></body></html>"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Bemerkung</span></p></body></html>"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_16), _translate("MainWindow", "Verwertet / Entsorgt"))
        self.label_78.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Diese Werte werden nach einem Neustart des Programms zurück gesetzt.</span></p><p><span style=\" color:#ffffff;\">Die Werte, die hier eingegeben werden, werden links Automatisch übernommen.</span></p></body></html>"))
        self.label_66.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Softwareversion</span></p></body></html>"))
        self.label_77.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Original Dokument liegt in </span></p></body></html>"))
        self.label_74.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Datum</span></p></body></html>"))
        self.label_87.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Tabelle Filtern</span></p></body></html>"))
        self.label_75.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Eingewiesener</span></p></body></html>"))
        self.label_67.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Datum</span></p></body></html>"))
        self.einweisung_speichern_btn.setText(_translate("MainWindow", "Speichern"))
        self.label_84.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Gerät</span></p></body></html>"))
        item = self.einweisung_tabelle.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Gerät"))
        item = self.einweisung_tabelle.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Softwareversion"))
        item = self.einweisung_tabelle.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Datum"))
        item = self.einweisung_tabelle.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Eingewiesener"))
        item = self.einweisung_tabelle.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Einweisender"))
        item = self.einweisung_tabelle.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Original Doukument"))
        self.einweisung_standardwerte_loeschen_btn.setText(_translate("MainWindow", "Löschen"))
        self.label_69.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Einweisender</span></p></body></html>"))
        self.label_72.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Gerät</span></p></body></html>"))
        self.label_76.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Einweisender</span></p></body></html>"))
        self.label_71.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Standard Werte</span></p></body></html>"))
        self.label_85.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Softwareversion</span></p></body></html>"))
        self.label_65.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Gerät</span></p></body></html>"))
        self.label_64.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Einweisung</span></p></body></html>"))
        self.label_68.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Eingewiesener</span></p></body></html>"))
        self.label_86.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Anzahl Gefilterte Ergebnisse:</span></p></body></html>"))
        self.label_73.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Softwareversion</span></p></body></html>"))
        self.label_70.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Original Dokument liegt in </span></p></body></html>"))
        self.label_106.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Mitarbeiter</span></p></body></html>"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_15), _translate("MainWindow", "Einweisung"))
        self.mpg_standort_speichern_btn.setText(_translate("MainWindow", "Speichern"))
        self.label_93.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Standort hinzufügen</span></p></body></html>"))
        item = self.mpg_standorte_tabelle.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Standorte"))
        self.mpg_standorte_loeschen_btn.setText(_translate("MainWindow", "Speichern"))
        self.label_94.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Name</span></p></body></html>"))
        self.label_97.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Standort Löschen</span></p></body></html>"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_18), _translate("MainWindow", "Standorte"))
        self.admin_bereich.setTabText(self.admin_bereich.indexOf(self.tab_13), _translate("MainWindow", "MPG"))
        self.label_53.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Admin Löschen</span></p></body></html>"))
        self.label_44.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Passwort ändern</span></p></body></html>"))
        self.neuer_admin_speichern.setText(_translate("MainWindow", "Speichern"))
        self.pw_aendern_speichern.setText(_translate("MainWindow", "Speichern"))
        self.label_54.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Alle Admins</span></p></body></html>"))
        self.label_48.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Name</span></p></body></html>"))
        self.label_52.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Passwort</span></p></body></html>"))
        self.label_45.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Altes Passwort</span></p></body></html>"))
        self.label_49.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Neuer Admin</span></p></body></html>"))
        self.label_50.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Passwort</span></p></body></html>"))
        self.label_51.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Passwort Wiederholen</span></p></body></html>"))
        self.label_47.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Neues Passwort Wiederholen</span></p></body></html>"))
        self.label_46.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Neues Passwort</span></p></body></html>"))
        item = self.tabelle_alle_admins.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        self.admin_loeschen_speichern.setText(_translate("MainWindow", "Speichern"))
        self.admin_bereich.setTabText(self.admin_bereich.indexOf(self.tab_12), _translate("MainWindow", "Admin Accounts"))
        self.label_104.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Nachname</span></p></body></html>"))
        self.label_103.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Vorname</span></p></body></html>"))
        self.ma_neu_speichern_btn.setText(_translate("MainWindow", "Speichern"))
        self.label_102.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Mitarbeiter anlegen</span></p></body></html>"))
        self.ma_loeschen_btn.setText(_translate("MainWindow", "Löschen"))
        self.label_105.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Mitarbeiter Löschen</span></p></body></html>"))
        item = self.ma_tabelle.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.ma_tabelle.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Vorname"))
        item = self.ma_tabelle.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nachname"))
        self.admin_bereich.setTabText(self.admin_bereich.indexOf(self.tab_20), _translate("MainWindow", "Mitarbeiter"))
        self.pushButton.setText(_translate("MainWindow", "Abbrechen"))
        self.check_uebersicht.setText(_translate("MainWindow", "Übersicht"))
        self.check_lager.setText(_translate("MainWindow", "Lagerverwaltung"))
        self.pdf_speicheror_btn.setText(_translate("MainWindow", "Ort auswählen"))
        self.einstellungen_speichern.setText(_translate("MainWindow", "Speichern"))
        self.check_dienstbekleidung.setText(_translate("MainWindow", "Dienstkleidung"))
        self.check_fahrzeuge.setText(_translate("MainWindow", "Fahrzeugstatus"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Bereiche Anzeigen oder nicht Anzeigen.</span></p></body></html>"))
        self.label_98.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Bestellungen PDF Speicherort festlegen</span></p></body></html>"))
        self.admin_bereich.setTabText(self.admin_bereich.indexOf(self.tab_8), _translate("MainWindow", "Einstellungen"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Admin"))

