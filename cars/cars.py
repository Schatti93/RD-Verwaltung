from cars.cars_data import Cars_Data
from cars.car_overview import Car_Overview
from PyQt5 import QtCore

# TODO insert combox radio_identification and let the user change this
class Cars_Employee():
    def __init__(self, ui):
        self.ui = ui
        self.data = Cars_Data()
        self.init_combo_cars_license_plate()
        self.combo_change_car_status()
        self.ui.cars_save_status_button.clicked.connect(self.fahrzeug_zustand_aendern)
        self.ui.combo_rtw.currentTextChanged.connect(self.combo_change_car_status)
        self.cars = {}
        self.fahrzeug_ansicht_initialisieren()

    def fahrzeug_ansicht_initialisieren(self):
        self.cars = Car_Overview(self.ui).show_car()

    def funkkenner_combo_fuellen(self):
        pass

    def init_combo_cars_license_plate(self):
        self.ui.combo_rtw.clear()
        cars = self.data.datas_for_combobox_cars()
        out = [item for t in cars for item in t]
        self.ui.combo_rtw.addItems(out)

    def fahrzeug_zustand_aendern(self):
        status = self.ui.combo_status.currentText()
        car = self.ui.combo_rtw.currentText()
        comment = self.ui.car_textedit.toPlainText()
        
        self.data.change_car_status(car, status, comment) # speichert die daten ueber den car zustand
        self.cars[car].itemAtPosition(1, 3).widget().setText(status)
        if status == "Im Dienst":
            self.cars[car].itemAtPosition(1, 3).widget().setStyleSheet("color:#ffffff; font-size:13pt; border: 1px solid #00FF00; border-radius: 5px")
        if status == "Außer Dienst":
            self.cars[car].itemAtPosition(1, 3).widget().setStyleSheet("color:#ffffff; font-size:13pt; border: 1px solid orange; border-radius: 5px")
        if status == "Nicht Einsatzbereit":
            self.cars[car].itemAtPosition(1, 3).widget().setStyleSheet("color:#ffffff; font-size:13pt; border: 1px solid red; border-radius: 5px")

        if comment == "":
            if self.cars[car].itemAtPosition(3, 0).widget().text() == "":
                pass
            else:
                self.cars[car].itemAtPosition(3, 0).widget().setText("")
                self.cars[car].itemAtPosition(3, 0).widget().setMaximumSize(QtCore.QSize(0, 0))

        if comment != "":
            self.cars[car].itemAtPosition(3, 0).widget().setText("<html><head/><body><p><span style=\" color:#ffffff;\">" + "Bemerkung: " + comment + "</span></p></body></html>")
            self.cars[car].itemAtPosition(3, 0).widget().setMaximumSize(QtCore.QSize(16677, 16677))
            self.ui.car_textedit.clear()
       
    def combo_change_car_status(self):
        self.ui.combo_status.clear() # leert die combobox um nue eintraege anzunehmen
        fahrzeug_aktiv = self.ui.combo_rtw.currentText() #holt sich das zur zeit ausgewaelte fahrzeug aus der Combobox
        status = self.data.data_combobox_status(fahrzeug_aktiv)
        if status[0][0] == "Nicht Einsatzbereit":
            self.ui.combo_status.addItems(["Nicht Einsatzbereit", "Im Dienst", "Außer Dienst"])
        if status[0][0] == "Im Dienst":
            self.ui.combo_status.addItems(["Im Dienst", "Außer Dienst", "Nicht Einsatzbereit"])
        if status[0][0] == "Außer Dienst":
            self.ui.combo_status.addItems(["Außer Dienst", "Nicht Einsatzbereit", "Im Dienst"])
