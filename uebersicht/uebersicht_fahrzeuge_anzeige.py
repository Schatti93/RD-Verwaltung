from PyQt5 import QtCore, QtGui, QtWidgets

class Fahrzeug_Anzeige():
    def __init__(self, ui):
        self.ui = ui


    def anzeige(self, kennung, kennzeichen, ort, status, bemerkung, counter):

        if counter <= 8:
            count = QtWidgets.QGridLayout()
            count.setObjectName("count")
            kenn_wert = QtWidgets.QLabel(self.ui.verticalLayoutWidget)
            kenn_wert.setObjectName("kenn_wert")
            count.addWidget(kenn_wert, 1, 1, 1, 1)
            line_anzeige = QtWidgets.QFrame(self.ui.verticalLayoutWidget)
            line_anzeige.setFrameShape(QtWidgets.QFrame.HLine)
            line_anzeige.setFrameShadow(QtWidgets.QFrame.Sunken)
            line_anzeige.setObjectName("line_anzeige")
            count.addWidget(line_anzeige, 4, 0, 1, 4)
            status_wert = QtWidgets.QLabel(self.ui.verticalLayoutWidget)
            status_wert.setObjectName("status_wert")
            count.addWidget(status_wert, 1, 3, 1, 1)
            status_label = QtWidgets.QLabel(self.ui.verticalLayoutWidget)
            status_label.setObjectName("status_label")
            count.addWidget(status_label, 1, 2, 1, 1)
            kenn_label = QtWidgets.QLabel(self.ui.verticalLayoutWidget)
            kenn_label.setObjectName("kenn_label")
            count.addWidget(kenn_label, 1, 0, 1, 1)
            ort_wert = QtWidgets.QLabel(self.ui.verticalLayoutWidget)
            ort_wert.setObjectName("ort_wert")
            count.addWidget(ort_wert, 0, 3, 1, 1)
            ort_label = QtWidgets.QLabel(self.ui.verticalLayoutWidget)
            ort_label.setObjectName("ort_label")
            count.addWidget(ort_label, 0, 2, 1, 1)
            bemerkung_label = QtWidgets.QLabel(self.ui.verticalLayoutWidget)
            bemerkung_label.setObjectName("bemerkung_label")
            count.addWidget(bemerkung_label, 3, 0, 1, 4)
            funk_label = QtWidgets.QLabel(self.ui.verticalLayoutWidget)
            funk_label.setObjectName("funk_label")
            count.addWidget(funk_label, 0, 0, 1, 1)
            funk_wert = QtWidgets.QLabel(self.ui.verticalLayoutWidget)
            funk_wert.setObjectName("funk_wert")
            count.addWidget(funk_wert, 0, 1, 1, 1)
            self.ui.fahrzeug_grid.addLayout(count)
            spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            self.ui.fahrzeug_grid.addItem(spacerItem)

            kenn_label.setText("<html><head/><body><p><span style=\" color:#ffffff;\">Kennzeichen: </span></p></body></html>")
            kenn_wert.setText("<html><head/><body><p><span style=\" color:#ffffff;\">" + kennzeichen + "</span></p></body></html>")
            status_label.setText("<html><head/><body><p><span style=\" color:#ffffff;\">Status:</span></p></body></html>")
            ort_wert.setText("<html><head/><body><p><span style=\" color:#ffffff;\">" + ort + "</span></p></body></html>")
            ort_label.setText("<html><head/><body><p><span style=\" color:#ffffff;\">Ort:</span></p></body></html>")
            if bemerkung == "":
                bemerkung_label.setText("")
            else:
                bemerkung_label.setText("<html><head/><body><p><span style=\" color:#ffffff;\">" + "Bemerkung: " + bemerkung + "</span></p></body></html>")
            funk_label.setText("<html><head/><body><p><span style=\" color:#ffffff;\">Funkkenner:</span></p></body></html>")
            funk_wert.setText("<html><head/><body><p><span style=\" color:#ffffff;\">" + kennung + "</span></p></body></html>")

            if status == "Im Dienst":
                status_wert.setText(status)
                status_wert.setStyleSheet("color:#ffffff; font-size:13pt; border: 1px solid #00FF00; border-radius: 5px")
            elif status == "Außer Dienst":
                status_wert.setText(status)
                status_wert.setStyleSheet("color:#ffffff; font-size:13pt; border: 1px solid orange; border-radius: 5px")
            else:
                status_wert.setText(status)
                status_wert.setStyleSheet("color:#ffffff; font-size:13pt; border: 1px solid red; border-radius: 5px")

        elif counter >8 and counter < 18:

            count = QtWidgets.QGridLayout()
            count.setObjectName("count")
            kenn_wert = QtWidgets.QLabel(self.ui.verticalLayoutWidget2)
            kenn_wert.setObjectName("kenn_wert")
            count.addWidget(kenn_wert, 1, 1, 1, 1)
            line_anzeige = QtWidgets.QFrame(self.ui.verticalLayoutWidget2)
            line_anzeige.setFrameShape(QtWidgets.QFrame.HLine)
            line_anzeige.setFrameShadow(QtWidgets.QFrame.Sunken)
            line_anzeige.setObjectName("line_anzeige")
            count.addWidget(line_anzeige, 4, 0, 1, 4)
            status_wert = QtWidgets.QLabel(self.ui.verticalLayoutWidget2)
            status_wert.setObjectName("status_wert")
            count.addWidget(status_wert, 1, 3, 1, 1)
            status_label = QtWidgets.QLabel(self.ui.verticalLayoutWidget2)
            status_label.setObjectName("status_label")
            count.addWidget(status_label, 1, 2, 1, 1)
            kenn_label = QtWidgets.QLabel(self.ui.verticalLayoutWidget2)
            kenn_label.setObjectName("kenn_label")
            count.addWidget(kenn_label, 1, 0, 1, 1)
            ort_wert = QtWidgets.QLabel(self.ui.verticalLayoutWidget2)
            ort_wert.setObjectName("ort_wert")
            count.addWidget(ort_wert, 0, 3, 1, 1)
            ort_label = QtWidgets.QLabel(self.ui.verticalLayoutWidget2)
            ort_label.setObjectName("ort_label")
            count.addWidget(ort_label, 0, 2, 1, 1)
            bemerkung_label = QtWidgets.QLabel(self.ui.verticalLayoutWidget2)
            bemerkung_label.setObjectName("bemerkung_label")
            count.addWidget(bemerkung_label, 3, 0, 1, 4)
            funk_label = QtWidgets.QLabel(self.ui.verticalLayoutWidget2)
            funk_label.setObjectName("funk_label")
            count.addWidget(funk_label, 0, 0, 1, 1)
            funk_wert = QtWidgets.QLabel(self.ui.verticalLayoutWidget2)
            funk_wert.setObjectName("funk_wert")
            count.addWidget(funk_wert, 0, 1, 1, 1)
            self.ui.fahrzeug_grid2.addLayout(count)
            spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                               QtWidgets.QSizePolicy.Expanding)
            self.ui.fahrzeug_grid2.addItem(spacerItem)

            kenn_label.setText(
                "<html><head/><body><p><span style=\" color:#ffffff;\">Kennzeichen: </span></p></body></html>")
            kenn_wert.setText(
                "<html><head/><body><p><span style=\" color:#ffffff;\">" + kennzeichen + "</span></p></body></html>")
            status_label.setText(
                "<html><head/><body><p><span style=\" color:#ffffff;\">Status:</span></p></body></html>")
            ort_wert.setText(
                "<html><head/><body><p><span style=\" color:#ffffff;\">" + ort + "</span></p></body></html>")
            ort_label.setText("<html><head/><body><p><span style=\" color:#ffffff;\">Ort:</span></p></body></html>")
            bemerkung_label.setText(
                "<html><head/><body><p><span style=\" color:#ffffff;\">" + bemerkung + "</span></p></body></html>")
            funk_label.setText(
                "<html><head/><body><p><span style=\" color:#ffffff;\">Funkkenner:</span></p></body></html>")
            funk_wert.setText(
                "<html><head/><body><p><span style=\" color:#ffffff;\">" + kennung + "</span></p></body></html>")

            if status == "Im Dienst":
                status_wert.setText(
                    "<html><head/><body><p><span style=\" color:#00FF00;\">" + status + "</span></p></body></html>")
            elif status == "Außer Dienst":
                status_wert.setText(
                    "<html><head/><body><p><span style=\" color:#F29C36;\">" + status + "</span></p></body></html>")
            else:
                status_wert.setText(
                    "<html><head/><body><p><span style=\" color:#ff0000;\">" + status + "</span></p></body></html>")

