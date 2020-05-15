from fahrzeuge.fahrzeug_data import Data_Fahrzeug
from fahrzeuge.fahrzeuge_uebersicht import Fahrzeuge_Uebersicht
from PyQt5 import QtCore


class Fahrzeug_Mitarbeiter():
    def __init__(self, ui):
        self.ui = ui
        self.daten_fuer_comboboxen_kennzeichen()
        self.daten_fuer_combobox_zustand()
        self.ui.button_fahrzeuge.clicked.connect(self.fahrzeug_zustand_aendern)
        self.data_fahrzeug = Data_Fahrzeug()
        self.ui.combo_rtw.currentTextChanged.connect(self.daten_fuer_combobox_zustand)
        self.fahrzeuge = {}
        self.fahrzeug_ansicht_initialisieren()

    def fahrzeug_ansicht_initialisieren(self):
        self.fahrzeuge = Fahrzeuge_Uebersicht(self.ui).anzeige()



    #erstellt die daten für die combobox fahrzeug auswahl wo die MA den Fahrzeug status aendern koennen
    def daten_fuer_comboboxen_kennzeichen(self):
        fahrzeuge = Data_Fahrzeug().daten_combo_fahrzeug_mitarbeiter()
        out = [item for t in fahrzeuge for item in t]
        self.ui.combo_rtw.addItems(out)

    def fahrzeug_zustand_aendern(self):
        zustand = self.ui.combo_zustand.currentText()
        fahrzeug = self.ui.combo_rtw.currentText()
        bemerkung = self.ui.fahrzeug_textedit.toPlainText()
        
        self.data_fahrzeug.fahrzeug_zustand_aendern_sql(fahrzeug, zustand, bemerkung) # speichert die daten ueber den fahrzeug zustand
        self.fahrzeuge[fahrzeug].itemAtPosition(1, 3).widget().setText(zustand)
        if zustand == "Im Dienst":
            self.fahrzeuge[fahrzeug].itemAtPosition(1, 3).widget().setStyleSheet("color:#ffffff; font-size:13pt; border: 1px solid #00FF00; border-radius: 5px")
        if zustand == "Außer Dienst":
            self.fahrzeuge[fahrzeug].itemAtPosition(1, 3).widget().setStyleSheet("color:#ffffff; font-size:13pt; border: 1px solid orange; border-radius: 5px")
        if zustand == "Nicht Einsatzbereit":
            self.fahrzeuge[fahrzeug].itemAtPosition(1, 3).widget().setStyleSheet("color:#ffffff; font-size:13pt; border: 1px solid red; border-radius: 5px")

        if bemerkung == "":
            if self.fahrzeuge[fahrzeug].itemAtPosition(3, 0).widget().text() == "":
                pass
            else:
                self.fahrzeuge[fahrzeug].itemAtPosition(3, 0).widget().setText("")
                self.fahrzeuge[fahrzeug].itemAtPosition(3, 0).widget().setMaximumSize(QtCore.QSize(0, 0))

        if bemerkung != "":
            self.fahrzeuge[fahrzeug].itemAtPosition(3, 0).widget().setText("<html><head/><body><p><span style=\" color:#ffffff;\">" + "Bemerkung: " + bemerkung + "</span></p></body></html>")
            self.fahrzeuge[fahrzeug].itemAtPosition(3, 0).widget().setMaximumSize(QtCore.QSize(16677, 16677))
            self.ui.fahrzeug_textedit.clear()
       
    def daten_fuer_combobox_zustand(self):
        self.ui.combo_zustand.clear() # leert die combobox um nue eintraege an zu nehmen
        fahrzeug_aktiv = self.ui.combo_rtw.currentText() #holt sich das zur zeit ausgewaelte fahrzeug aus der Combobox
        status = Data_Fahrzeug().daten_combo_status_rtw(fahrzeug_aktiv)
        if status[0][0] == "Nicht Einsatzbereit":
            self.ui.combo_zustand.addItems(["Nicht Einsatzbereit", "Im Dienst", "Außer Dienst"])
        if status[0][0] == "Im Dienst":
            self.ui.combo_zustand.addItems(["Im Dienst", "Außer Dienst", "Nicht Einsatzbereit"])
        if status[0][0] == "Außer Dienst":
            self.ui.combo_zustand.addItems(["Außer Dienst", "Nicht Einsatzbereit", "Im Dienst"])
