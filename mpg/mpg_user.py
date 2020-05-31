from mpg.mpg_user_data import Mpg_User_Data
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5 import QtCore


class Mpg_User():
    def __init__(self, ui):
        self.ui = ui
        self.data = Mpg_User_Data()
        self.standort_combo_fuellen()
        self.ui.mpg_Fahrzeuge_combo.currentTextChanged.connect(self.geraete_fahrzeug_tabelle_fuellen)
        self.ui.mpg_user_geraete_barcode.returnPressed.connect(self.standorte_sortiert_combo_fuellen)
        self.ui.mpg_user_geraete_aufrufen_btn.clicked.connect(self.standorte_sortiert_combo_fuellen)
        self.ui.mpg_user_geraete_speichern_btn.clicked.connect(self.neuen_standort_von_geraet_speichern)

    def standort_combo_fuellen(self):
        self.ui.mpg_Fahrzeuge_combo.clear()
        standorte = self.data.standorte_abfragen()
        liste_der_eintraege = ["---"]
        for element in range(0, len(standorte)):
            if standorte[element][0] in liste_der_eintraege:
                pass
            else:
                liste_der_eintraege.append(standorte[element][0])
        self.ui.mpg_Fahrzeuge_combo.addItems(liste_der_eintraege)

    def geraete_fahrzeug_tabelle_fuellen(self):
        self.ui.mpg_geraete_tabelle_fahrzeug.setRowCount(0)
        standort = self.ui.mpg_Fahrzeuge_combo.currentText()
        if standort == "---":
            pass
        else:
            liste_der_geraete = self.data.geraete_auf_standort_abfragen(standort)
            for element in range(0, len(liste_der_geraete)):
                count = 0
                rows = self.ui.mpg_geraete_tabelle_fahrzeug.rowCount()
                self.ui.mpg_geraete_tabelle_fahrzeug.insertRow(rows)
                for eigenschaft in range(0, len(liste_der_geraete[element])):
                    einzusetzen = QtWidgets.QTableWidgetItem(liste_der_geraete[element][eigenschaft])
                    einzusetzen.setTextAlignment(Qt.AlignCenter)
                    self.ui.mpg_geraete_tabelle_fahrzeug.setItem(rows, count, QtWidgets.QTableWidgetItem(einzusetzen))
                    count += 1
        self.ui.mpg_geraete_tabelle_fahrzeug.horizontalHeader().setSectionResizeMode(1)

    def standorte_sortiert_combo_fuellen(self):
        inventarnummer = self.ui.mpg_user_geraete_barcode.text()
        standort = self.data.standort_von_geraet_abfragen(inventarnummer)
        if len(standort) > 0:
            standort = standort[0][0]
            self.ui.mpg_user_geraete_standort_combo.clear()
            fahrzeuge = self.data.fahrzeuge_abfragen()
            liste_der_eintraege = []
            for element in range(0, len(fahrzeuge)):
                if fahrzeuge[element][0] in liste_der_eintraege:
                    pass
                else:
                    liste_der_eintraege.append(fahrzeuge[element][0])

            wachen = self.data.wachen_abfragen()
            for element in range(0, len(wachen)):
                if wachen[element][0] in liste_der_eintraege:
                    pass
                else:
                    liste_der_eintraege.append(wachen[element][0])

            self.ui.mpg_user_geraete_standort_combo.addItems(liste_der_eintraege)

            index = self.ui.mpg_user_geraete_standort_combo.findText(standort, QtCore.Qt.MatchFixedString)
            self.ui.mpg_user_geraete_standort_combo.setCurrentIndex(index)



    def neuen_standort_von_geraet_speichern(self):
        neuer_standort = self.ui.mpg_user_geraete_standort_combo.currentText()
        inventarnummer = self.ui.mpg_user_geraete_barcode.text()
        bemerkung = self.ui.mpg_user_bemerkung.text()
        bemerkung_datenbank = self.data.bemerkung_abfragen(inventarnummer)[0][0]
        if bemerkung == "":
            neue_bemerkung = bemerkung_datenbank
        else:
            neue_bemerkung = bemerkung_datenbank + "; " + bemerkung

        self.data.update_standort_von_geraet(neuer_standort, inventarnummer, neue_bemerkung)
        self.ui.mpg_user_geraete_barcode.setText("")
        self.ui.mpg_user_bemerkung.setText("")
        self.ui.mpg_user_geraete_standort_combo.clear()
        self.update()

    def fahrzeug_combo_erneut_fuellen(self):
        standort = self.ui.mpg_Fahrzeuge_combo.currentText()
        self.ui.mpg_Fahrzeuge_combo.clear()
        self.standort_combo_fuellen()
        index = self.ui.mpg_Fahrzeuge_combo.findText(standort, QtCore.Qt.MatchFixedString)
        self.ui.mpg_Fahrzeuge_combo.setCurrentIndex(index)

    def update(self):
        self.fahrzeug_combo_erneut_fuellen()
        self.standort_combo_fuellen()
        self.geraete_fahrzeug_tabelle_fuellen()