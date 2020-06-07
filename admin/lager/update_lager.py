from uebersicht.uebersicht import Uebersicht
from admin.lager.admin_lager_data import Admin_Lager_Data
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

class Update_Lager():
    def __init__(self, ui):
        self.ui = ui
        self.data = Admin_Lager_Data()

    def update(self):
        Uebersicht(self.ui).lager_uebersicht()
        self.fehlendes_material()
        self.combobox_bestellung_einpflegen()
        self.alle_produkte_anzeigen_table()

    def fehlendes_material(self):
        liste = self.data.get_liste()
        count = 0
        self.ui.admin_lager_fehlendes_material.setRowCount(0)

        for i in range(0, len(liste)):
            if liste[i][2] >= liste[i][3]:
                if liste[i][8] == "Ausreichend":
                    pass
                else:
                    self.data.update_status(liste[i][1], "Ausreichend")
            else:
                if liste[i][8] == "NULL":
                    self.data.update_status(liste[i][1], "Bestand zu gering")
                    status = QtWidgets.QTableWidgetItem("Bestand zu gering")
                    status.setTextAlignment(Qt.AlignCenter)
                else:
                    status = "Bestand zu gering"
                status = QtWidgets.QTableWidgetItem(str(liste[i][8]))
                status.setTextAlignment(Qt.AlignCenter)

                produkt = QtWidgets.QTableWidgetItem(liste[i][1])
                produkt.setTextAlignment(Qt.AlignCenter)
                vorhanden = QtWidgets.QTableWidgetItem(str(liste[i][2]))
                vorhanden.setTextAlignment(Qt.AlignCenter)
                mindest = QtWidgets.QTableWidgetItem(str(liste[i][3]))
                mindest.setTextAlignment(Qt.AlignCenter)
                max = QtWidgets.QTableWidgetItem(str(liste[i][4]))
                max.setTextAlignment(Qt.AlignCenter)
                artikelnr = QtWidgets.QTableWidgetItem(str(liste[i][7]))
                artikelnr.setTextAlignment(Qt.AlignCenter)
                count = count + 1

                row = self.ui.admin_lager_fehlendes_material.rowCount()
                self.ui.admin_lager_fehlendes_material.insertRow(row)
                self.ui.admin_lager_fehlendes_material.setItem(row, 0, QtWidgets.QTableWidgetItem(produkt))
                self.ui.admin_lager_fehlendes_material.setItem(row, 1, QtWidgets.QTableWidgetItem(vorhanden))
                self.ui.admin_lager_fehlendes_material.setItem(row, 2, QtWidgets.QTableWidgetItem(mindest))
                self.ui.admin_lager_fehlendes_material.setItem(row, 3, QtWidgets.QTableWidgetItem(max))
                self.ui.admin_lager_fehlendes_material.setItem(row, 4, QtWidgets.QTableWidgetItem(artikelnr))
                self.ui.admin_lager_fehlendes_material.setItem(row, 5, QtWidgets.QTableWidgetItem(status))
                self.ui.admin_lager_fehlendes_material.horizontalHeader().setSectionResizeMode(1)

    def combobox_bestellung_einpflegen(self):
        self.ui.admin_material_speichern_combo.clear()
        liste_der_daten = self.data.get_liste()
        liste_der_eintraege = ["---"]
        for eintrag in liste_der_daten:
            liste_der_eintraege.append(eintrag[1])
        self.ui.admin_material_speichern_combo.addItems(liste_der_eintraege)

    def alle_produkte_anzeigen_table(self):
        self.ui.admin_lager_alle_produkte.setRowCount(0)
        alle_produkte = self.data.get_liste()
        for element in range(0, len(alle_produkte)):
            rows = self.ui.admin_lager_alle_produkte.rowCount()
            count = 0
            self.ui.admin_lager_alle_produkte.insertRow(rows)
            for eigenschaft in range(0, 8):
                einzusetzen = QtWidgets.QTableWidgetItem(str(alle_produkte[element][eigenschaft]))
                einzusetzen.setTextAlignment(Qt.AlignCenter)
                self.ui.admin_lager_alle_produkte.setItem(rows, count, QtWidgets.QTableWidgetItem(einzusetzen))
                count += 1
        self.ui.admin_lager_alle_produkte.horizontalHeader().setSectionResizeMode(1)