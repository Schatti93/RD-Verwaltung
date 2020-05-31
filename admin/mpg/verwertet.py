from admin.mpg.mpg_data import Mpg_Data
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from mpg.mpg_user import Mpg_User
from admin.mpg.update_mpg import Update_Mpg
class Verwertet():
    def __init__(self, ui):
        self.data = Mpg_Data()
        self.ui = ui
        self.ui.verwertet_speichern_button.clicked.connect \
            (self.geraet_verwerten)

    def verwertet_tabelle_fuellen(self):
        self.ui.verwertet_tabelle.setRowCount(0)
        verwertete_geraete = self.data.verwertete_geraete_abfragen()
        for element in range(0, len(verwertete_geraete)):
            count = 0
            rows = self.ui.verwertet_tabelle.rowCount()
            self.ui.verwertet_tabelle.insertRow(rows)
            for eigenschaft in range(1, len(verwertete_geraete[element])):
                einzusetzen = QtWidgets.QTableWidgetItem(verwertete_geraete[element][eigenschaft])
                einzusetzen.setTextAlignment(Qt.AlignCenter)
                self.ui.verwertet_tabelle.setItem(rows, count, QtWidgets.QTableWidgetItem(einzusetzen))
                count += 1
        self.ui.verwertet_tabelle.horizontalHeader().setSectionResizeMode(1)

    def geraete_inventarnummer_combos_fuellen(self):
        self.ui.verwertet_geraete_combo.clear()
        geraete = self.data.geraete_abfragen()
        liste_der_eintraege = ["---"]
        for element in range(0, len(geraete)):
            liste_der_eintraege.append(geraete[element][1] + " / " + geraete[element][2])
        self.ui.verwertet_geraete_combo.addItems(liste_der_eintraege)

    def geraet_verwerten(self):
        geraet = self.ui.verwertet_geraete_combo.currentText()
        datum = self.ui.verwertet_datum.text()
        geraetenummer = str(geraet).split("/ ")[1]
        bemerkung = self.ui.verwertet_bemerkung.text()
        self.data.geraet_verwerten(geraet, datum, geraetenummer, bemerkung)
        rows = self.ui.verwertet_tabelle.rowCount()
        self.ui.verwertet_tabelle.insertRow(rows)
        Update_Mpg(self.ui).update_tabellen_und_combos()
        Mpg_User(self.ui).update()
        self.ui.verwertet_geraete_combo.setCurrentIndex(0)
        self.ui.verwertet_datum.setText("")
        self.ui.verwertet_bemerkung.setText("")