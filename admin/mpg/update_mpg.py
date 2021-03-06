from admin.mpg.mpg_data import Mpg_Data
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from dateutil.relativedelta import relativedelta
import datetime
from datetime import date
from PyQt5 import QtGui
from PyQt5 import QtCore

class Update_Mpg():
    def __init__(self, ui):
        self.ui = ui
        self.data = Mpg_Data()

    def update_tabellen_und_combos(self):
        self.einweisung_geraete_combos_fuellen()
        self.geraete_inventarnummer_combos_fuellen()
        self.geraete_tabelle_fuellen()
        self.standort_combo_fuellen()

    def standort_combo_fuellen(self):
        self.ui.geraete_verwalten_standort_combo.clear()
        alle_fahrzeuge = self.data.fahrzeuge_abfragen()
        liste_der_eintraege = ["---"]
        for element in range(0, len(alle_fahrzeuge)):
            liste_der_eintraege.append(alle_fahrzeuge[element][2])

        standorte = self.data.standorte_abfragen()
        for element in range(0, len(standorte)):
            liste_der_eintraege.append(standorte[element][0])
        self.ui.geraete_verwalten_standort_combo.addItems(liste_der_eintraege)

    def einweisung_geraete_combos_fuellen(self):
        self.ui.einweisung_geraete_combo.clear()
        self.ui.einweisung_geraete_combo_standard.clear()
        self.ui.einweisung_tabelle_filtern_geraet_combo.clear()
        geraete = self.data.geraete_abfragen()
        liste_der_eintraege = ["---"]
        for element in range(0, len(geraete)):
            if geraete[element][1] in liste_der_eintraege:
                pass
            else:
                liste_der_eintraege.append(geraete[element][1])
        self.ui.einweisung_geraete_combo.addItems(liste_der_eintraege)
        self.ui.einweisung_geraete_combo_standard.addItems(liste_der_eintraege)
        self.ui.einweisung_tabelle_filtern_geraet_combo.addItems(liste_der_eintraege)

    def geraete_inventarnummer_combos_fuellen(self):
        self.ui.verwertet_geraete_combo.clear()
        geraete = self.data.geraete_abfragen()
        liste_der_eintraege = ["---"]
        for element in range(0, len(geraete)):
            liste_der_eintraege.append(geraete[element][1] + " / " + geraete[element][2])
        self.ui.verwertet_geraete_combo.addItems(liste_der_eintraege)

    def geraete_tabelle_fuellen(self):
        self.ui.mpg_geraete_tabelle.setRowCount(0)
        geraete = self.data.geraete_abfragen()

        for element in range(0, len(geraete)):
            count = 0
            feld = 0
            rows = self.ui.mpg_geraete_tabelle.rowCount()
            self.ui.mpg_geraete_tabelle.insertRow(rows)
            for eigenschaft in range(0, len(geraete[element])):
                if count == 8:
                    einzusetzen = QtWidgets.QTableWidgetItem()
                    einzusetzen.setTextAlignment(Qt.AlignCenter)
                    einzusetzen.setData(QtCore.Qt.EditRole, geraete[element][eigenschaft])
                    self.ui.mpg_geraete_tabelle.setItem(rows, feld, einzusetzen)

                    feld += 1
                    pruefdatum_splitted = geraete[element][7].split(".")
                    datum = datetime.date(int(pruefdatum_splitted[2]), int(pruefdatum_splitted[1]),
                                          int(pruefdatum_splitted[0]))
                    naechste_pruefung = datum + relativedelta(months=int(geraete[element]
                                                                         [eigenschaft]))
                    today = date.today()
                    kritisch = naechste_pruefung - today

                    naechste_pruefung = str(naechste_pruefung.strftime("%d.%m.%Y"))

                    entry = QtWidgets.QTableWidgetItem(naechste_pruefung)
                    if int(kritisch.days) <= 60:
                        entry.setForeground(QtGui.QColor(255, 0, 0))
                    entry.setTextAlignment(Qt.AlignCenter)

                    self.ui.mpg_geraete_tabelle.setItem(rows, feld, entry)
                    count += 1
                    feld += 1
                else:
                    einzusetzen = QtWidgets.QTableWidgetItem(str(geraete[element][eigenschaft]))
                    einzusetzen.setTextAlignment(Qt.AlignCenter)
                    if eigenschaft == 0:
                        einzusetzen.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.ui.mpg_geraete_tabelle.setItem(rows, feld, einzusetzen)
                    feld += 1
                    count += 1
        self.ui.mpg_geraete_tabelle.horizontalHeader().setSectionResizeMode(1)
