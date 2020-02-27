# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/einstellungen_lager.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Einstellungen_Lager(object):
    def setupUi(self, Einstellungen_Lager):
        Einstellungen_Lager.setObjectName("Einstellungen_Lager")
        Einstellungen_Lager.resize(814, 634)
        self.buttonBox = QtWidgets.QDialogButtonBox(Einstellungen_Lager)
        self.buttonBox.setGeometry(QtCore.QRect(460, 590, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Einstellungen_Lager)
        self.buttonBox.accepted.connect(Einstellungen_Lager.accept)
        self.buttonBox.rejected.connect(Einstellungen_Lager.reject)
        QtCore.QMetaObject.connectSlotsByName(Einstellungen_Lager)

    def retranslateUi(self, Einstellungen_Lager):
        _translate = QtCore.QCoreApplication.translate
        Einstellungen_Lager.setWindowTitle(_translate("Einstellungen_Lager", "Dialog"))
