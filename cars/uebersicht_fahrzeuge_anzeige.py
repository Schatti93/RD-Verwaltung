from PyQt5 import QtCore, QtWidgets

class Fahrzeug_Anzeige():
    def __init__(self, ui):
        self.ui = ui


    def anzeige(self, kennung, kennzeichen, ort, status, bemerkung, counter):

        if counter <= 8:
            count = QtWidgets.QGridLayout()
            count.setObjectName("count")
            kenn_wert = QtWidgets.QLabel(self.ui.tab_4)
            kenn_wert.setMaximumSize(QtCore.QSize(16777215, 30))
            kenn_wert.setObjectName("kenn_wert")
            kenn_wert.setMinimumSize(QtCore.QSize(120, 0))
            count.addWidget(kenn_wert, 1, 1, 1, 1)
            line_anzeige = QtWidgets.QFrame(self.ui.tab_4)
            line_anzeige.setFrameShape(QtWidgets.QFrame.HLine)
            line_anzeige.setFrameShadow(QtWidgets.QFrame.Sunken)
            line_anzeige.setObjectName("line_anzeige")
            count.addWidget(line_anzeige, 4, 0, 1, 4)
            status_wert = QtWidgets.QLabel(self.ui.tab_4)
            status_wert.setObjectName("status_wert")
            status_wert.setMaximumSize(QtCore.QSize(16777215, 30))
            count.addWidget(status_wert, 1, 3, 1, 1)
            status_label = QtWidgets.QLabel(self.ui.tab_4)
            status_label.setObjectName("status_label")
            count.addWidget(status_label, 1, 2, 1, 1)
            kenn_label = QtWidgets.QLabel(self.ui.tab_4)
            kenn_label.setObjectName("kenn_label")
            count.addWidget(kenn_label, 1, 0, 1, 1)
            ort_wert = QtWidgets.QLabel(self.ui.tab_4)
            ort_wert.setMaximumSize(QtCore.QSize(16777215, 30))
            ort_wert.setObjectName("ort_wert")
            ort_wert.setMinimumSize(QtCore.QSize(155, 0))
            count.addWidget(ort_wert, 0, 3, 1, 1)
            ort_label = QtWidgets.QLabel(self.ui.tab_4)
            ort_label.setObjectName("ort_label")
            count.addWidget(ort_label, 0, 2, 1, 1)
            bemerkung_label = QtWidgets.QLabel(self.ui.tab_4)
            bemerkung_label.setMaximumSize(QtCore.QSize(16777215, 30))
            bemerkung_label.setObjectName("bemerkung_label")
            count.addWidget(bemerkung_label, 3, 0, 1, 4)
            funk_label = QtWidgets.QLabel(self.ui.tab_4)
            funk_label.setObjectName("funk_label")
            count.addWidget(funk_label, 0, 0, 1, 1)
            funk_wert = QtWidgets.QLabel(self.ui.tab_4)
            funk_wert.setObjectName("funk_wert")
            count.addWidget(funk_wert, 0, 1, 1, 1)
            spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.ui.verticalLayout.addLayout(count)
            self.ui.verticalLayout.addItem(spacerItem)

            kenn_label.setText("<html><head/><body><p><span style=\" color:#ffffff;\">Kennzeichen: </span></p></body></html>")
            kenn_wert.setText("<html><head/><body><p><span style=\" color:#ffffff;\">" + kennzeichen + "</span></p></body></html>")
            status_label.setText("<html><head/><body><p><span style=\" color:#ffffff;\">Status:</span></p></body></html>")
            ort_wert.setText("<html><head/><body><p><span style=\" color:#ffffff;\">" + ort + "</span></p></body></html>")
            ort_label.setText("<html><head/><body><p><span style=\" color:#ffffff;\">Ort:</span></p></body></html>")
            if bemerkung == "":
                bemerkung_label.setText("")
                bemerkung_label.setMaximumSize(QtCore.QSize(0, 0))
            else:
                bemerkung_label.setText("<html><head/><body><p><span style=\" color:#ffffff;\">" + "Bemerkung: " + bemerkung + "</span></p></body></html>")
            funk_label.setText("<html><head/><body><p><span style=\" color:#ffffff;\">Funkkenner:</span></p></body></html>")
            funk_wert.setText("<html><head/><body><p><span style=\" color:#ffffff;\">" + kennung + "</span></p></body></html>")
            if status == "Im Dienst":
                status_wert.setText(status)
                status_wert.setStyleSheet("color:#ffffff; border: 1px solid #00FF00; border-radius: 5px")
            elif status == "Außer Dienst":
                status_wert.setText(status)
                status_wert.setStyleSheet("color:#ffffff; border: 1px solid orange; border-radius: 5px")
            else:
                status_wert.setText(status)
                status_wert.setStyleSheet("color:#ffffff; border: 1px solid red; border-radius: 5px")
            return count

        elif counter > 8 and counter < 18:
            count = QtWidgets.QGridLayout()
            count.setObjectName("count")
            kenn_wert = QtWidgets.QLabel(self.ui.tab_4)
            kenn_wert.setObjectName("kenn_wert")
            kenn_wert.setMinimumSize(QtCore.QSize(120, 0))
            count.addWidget(kenn_wert, 1, 1, 1, 1)
            line_anzeige = QtWidgets.QFrame(self.ui.tab_4)
            line_anzeige.setFrameShape(QtWidgets.QFrame.HLine)
            line_anzeige.setFrameShadow(QtWidgets.QFrame.Sunken)
            line_anzeige.setObjectName("line_anzeige")
            count.addWidget(line_anzeige, 4, 0, 1, 4)
            status_wert = QtWidgets.QLabel(self.ui.tab_4)
            status_wert.setObjectName("status_wert")
            count.addWidget(status_wert, 1, 3, 1, 1)
            status_label = QtWidgets.QLabel(self.ui.tab_4)
            status_label.setObjectName("status_label")
            count.addWidget(status_label, 1, 2, 1, 1)
            kenn_label = QtWidgets.QLabel(self.ui.tab_4)
            kenn_label.setObjectName("kenn_label")
            count.addWidget(kenn_label, 1, 0, 1, 1)
            ort_wert = QtWidgets.QLabel(self.ui.tab_4)
            ort_wert.setObjectName("ort_wert")
            ort_wert.setMinimumSize(QtCore.QSize(155, 0))
            count.addWidget(ort_wert, 0, 3, 1, 1)
            ort_label = QtWidgets.QLabel(self.ui.tab_4)
            ort_label.setObjectName("ort_label")
            count.addWidget(ort_label, 0, 2, 1, 1)
            bemerkung_label = QtWidgets.QLabel(self.ui.tab_4)
            bemerkung_label.setObjectName("bemerkung_label")
            count.addWidget(bemerkung_label, 3, 0, 1, 4)
            funk_label = QtWidgets.QLabel(self.ui.tab_4)
            funk_label.setObjectName("funk_label")
            count.addWidget(funk_label, 0, 0, 1, 1)
            funk_wert = QtWidgets.QLabel(self.ui.tab_4)
            funk_wert.setObjectName("funk_wert")
            count.addWidget(funk_wert, 0, 1, 1, 1)
            spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.ui.verticalLayout2.addLayout(count)
            self.ui.verticalLayout2.addItem(spacerItem)

            kenn_label.setText(
                "<html><head/><body><p><span style=\" color:#ffffff;\">Kennzeichen: </span></p></body></html>")
            kenn_wert.setText(
                "<html><head/><body><p><span style=\" color:#ffffff;\">" + kennzeichen + "</span></p></body></html>")
            status_label.setText(
                "<html><head/><body><p><span style=\" color:#ffffff;\">Status:</span></p></body></html>")
            ort_wert.setText(
                "<html><head/><body><p><span style=\" color:#ffffff;\">" + ort + "</span></p></body></html>")
            ort_label.setText("<html><head/><body><p><span style=\" color:#ffffff;\">Ort:</span></p></body></html>")
            if bemerkung == "":
                bemerkung_label.setText("")
                bemerkung_label.setMaximumSize(QtCore.QSize(0, 0))
            else:
                bemerkung_label.setText(
                    "<html><head/><body><p><span style=\" color:#ffffff;\">" + "Bemerkung: " + bemerkung + "</span></p></body></html>")
            funk_label.setText(
                "<html><head/><body><p><span style=\" color:#ffffff;\">Funkkenner:</span></p></body></html>")
            funk_wert.setText(
                "<html><head/><body><p><span style=\" color:#ffffff;\">" + kennung + "</span></p></body></html>")
            if status == "Im Dienst":
                status_wert.setText(status)
                status_wert.setStyleSheet(
                    "color:#ffffff; border: 1px solid #00FF00; border-radius: 5px")
            elif status == "Außer Dienst":
                status_wert.setText(status)
                status_wert.setStyleSheet("color:#ffffff; border: 1px solid orange; border-radius: 5px")
            else:
                status_wert.setText(status)
                status_wert.setStyleSheet("color:#ffffff; border: 1px solid red; border-radius: 5px")

