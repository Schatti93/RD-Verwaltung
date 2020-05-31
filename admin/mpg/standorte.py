from admin.mpg.mpg_data import Mpg_Data
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from mpg.mpg_user import Mpg_User
from admin.mpg.update_mpg import Update_Mpg
class Standorte():
    def __init__(self, ui):
        self.ui = ui
        self.data = Mpg_Data()
        self.ui.mpg_standort_speichern_btn.clicked.connect(self.mpg_standort_hinzufuegen)
        self.ui.mpg_standorte_loeschen_btn.clicked.connect(self.standort_loeschen)

    def standorte_tabelle_fuellen(self):
        self.ui.mpg_standorte_tabelle.setRowCount(0)
        standorte = self.data.standorte_abfragen()
        for element in range(0, len(standorte)):
            rows = self.ui.mpg_standorte_tabelle.rowCount()
            self.ui.mpg_standorte_tabelle.insertRow(rows)
            einzusetzen = QtWidgets.QTableWidgetItem(standorte[element][0])
            einzusetzen.setTextAlignment(Qt.AlignCenter)
            self.ui.mpg_standorte_tabelle.setItem(rows, 0, QtWidgets.QTableWidgetItem(einzusetzen))

        self.ui.mpg_standorte_tabelle.horizontalHeader().setSectionResizeMode(1)

    def mpg_standort_hinzufuegen(self):
        name = self.ui.mpg_standort_text.text()
        self.data.neuen_standort_anlegen(name)
        self.standorte_tabelle_fuellen()
        self.standort_loeschen_combo_fuellen()
        Update_Mpg(self.ui).update_tabellen_und_combos()
        self.ui.mpg_standort_text.setText("")
        Mpg_User(self.ui).update()

    def standort_loeschen_combo_fuellen(self):
        self.ui.mpg_standorte_combo.clear()
        standorte = self.data.standorte_abfragen()
        liste_der_eintraege = ["---"]
        for element in range(0, len(standorte)):
            liste_der_eintraege.append(standorte[element][0])
        self.ui.mpg_standorte_combo.addItems(liste_der_eintraege)

    def standort_loeschen(self):
        name = self.ui.mpg_standorte_combo.currentText()
        self.data.standort_loeschen(name)
        self.standorte_tabelle_fuellen()
        self.standort_loeschen_combo_fuellen()
        Update_Mpg(self.ui).update_tabellen_und_combos()
        Mpg_User(self.ui).update()