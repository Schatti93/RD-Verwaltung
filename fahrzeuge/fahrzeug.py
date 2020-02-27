from fahrzeuge.fahrzeug_data import Data_Fahrzeug
from fahrzeuge.fahrzeuge_uebersicht import Fahrzeuge_Uebersicht
from uebersicht.grid_fahrzeuge import Grid_Fahrzeuge


class Fahrzeug_Mitarbeiter():
    def __init__(self, ui):
        self.ui = ui
        self.daten_fuer_comboboxen_kennzeichen()
        self.daten_fuer_combobox_zustand()
        self.ui.button_fahrzeuge.clicked.connect(self.fahrzeug_zustand_aendern)
        self.data_fahrzeug = Data_Fahrzeug()
        self.ui.combo_rtw.currentTextChanged.connect(self.daten_fuer_combobox_zustand)



    #erstellt die daten für die combobox fahrzeug auswahl wo die MA den Fahrzeug status aendern koennen
    def daten_fuer_comboboxen_kennzeichen(self):
        fahrzeuge = Data_Fahrzeug().daten_combo_fahrzeug_mitarbeiter()
        out = [item for t in fahrzeuge for item in t]
        self.ui.combo_rtw.addItems(out)

    def fahrzeug_zustand_aendern(self):
        zustand = text = self.ui.combo_zustand.currentText()
        fahrzeug = self.ui.combo_rtw.currentText()
        bemerkung = self.ui.fahrzeug_textedit.toPlainText()
        self.ui.verticalLayoutWidget.setParent(None) #löscht das grid für neu aufbau
        Grid_Fahrzeuge(self.ui).grid_fahrzeug_anzeige() #erstellt das grid neu
        self.data_fahrzeug.fahrzeug_zustand_aendern_sql(fahrzeug, zustand, bemerkung) # speichert die daten ueber den fahrzeug zustand
        Fahrzeuge_Uebersicht(self.ui).anzeige() # baut den inhalt der uebersicht neu auf

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