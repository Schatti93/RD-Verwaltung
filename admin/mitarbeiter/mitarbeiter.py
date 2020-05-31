from admin.mitarbeiter.mitarbeiter_data import Mitarbeiter_Data
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from admin.mpg.mpg_geraete import Mpg_Geraete
from admin.mpg.einweisungen import Einweisungen

class Mitarbeiter():
    def __init__(self, ui):
        self.ui = ui
        self.data = Mitarbeiter_Data()
        self.mitarbeiter_tabelle_laden()
        self.ma_loeschen_combo_fuellen()
        self.ui.ma_neu_speichern_btn.clicked.connect(self.neuer_mitarbeiter)
        self.ui.ma_loeschen_btn.clicked.connect(self.ma_loeschen)

    def mitarbeiter_tabelle_laden(self):
        self.ui.ma_tabelle.setRowCount(0)
        liste_der_eintraege = self.data.alle_ma_abfragen()
        for element in range(0, len(liste_der_eintraege)):
            rows = self.ui.ma_tabelle.rowCount()
            self.ui.ma_tabelle.insertRow(rows)
            for eintrag in range(0, len(liste_der_eintraege[element])):
                einzusetzen = QtWidgets.QTableWidgetItem(str(liste_der_eintraege[element][eintrag]))
                einzusetzen.setTextAlignment(Qt.AlignCenter)
                self.ui.ma_tabelle.setItem(rows, eintrag, QtWidgets.QTableWidgetItem(
                    einzusetzen))

    def ma_loeschen_combo_fuellen(self):
        self.ui.ma_loeschen_combo.clear()
        liste_der_daten = self.data.alle_ma_abfragen()
        combo_eintraege = ["---"]
        for element in range(0, len(liste_der_daten)):
            eintrag = str(liste_der_daten[element][1]) + ", " + str(liste_der_daten[element][2]) \
            + " / " + str(liste_der_daten[element][0])
            combo_eintraege.append(eintrag)
        self.ui.ma_loeschen_combo.addItems(combo_eintraege)

    def neuer_mitarbeiter(self):
        vorname = self.ui.ma_neu_vorname_text.text()
        nachname = self.ui.ma_neu_nachname_text.text()
        self.data.neuer_mitarbeiter_speichern(vorname, nachname)
        self.mitarbeiter_tabelle_laden()
        self.ma_loeschen_combo_fuellen()
        self.ui.ma_neu_vorname_text.setText("")
        self.ui.ma_neu_nachname_text.setText("")
        Einweisungen(self.ui).combos_ma_fuellen()
        Einweisungen(self.ui).tabellen_filter_ma_combo_fuellen()

    def ma_loeschen(self):
        ma_id = self.ui.ma_loeschen_combo.currentText().split("/ ")[1]
        self.data.ma_loeschen(ma_id)
        self.mitarbeiter_tabelle_laden()
        self.ma_loeschen_combo_fuellen()
        Einweisungen(self.ui).combos_ma_fuellen()
        Einweisungen(self.ui).tabellen_filter_ma_combo_fuellen()


