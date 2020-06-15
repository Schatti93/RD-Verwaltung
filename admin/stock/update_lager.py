from overview.overview import Overview
from admin.stock.admin_lager_data import Admin_Lager_Data
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from fill_table import Fill_Table

class Update_Stock():
    def __init__(self, ui):
        self.ui = ui
        self.fill_table = Fill_Table(self.ui)
        self.data = Admin_Lager_Data()

    def update(self):
        Overview(self.ui).stock_overview()
        self.fehlendes_material()
        self.combobox_bestellung_einpflegen()
        self.alle_produkte_anzeigen_table()

    def update_from_fehlendes_material(self):
        self.combobox_bestellung_einpflegen()
        self.alle_produkte_anzeigen_table()
        Overview(self.ui).stock_overview()

    def fehlendes_material(self):
        liste = self.data.get_liste()
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
                list = [liste[i][1], str(liste[i][2]), str(liste[i][3]), str(liste[i][4]), str(liste[i][7]),  status]
                mode = (0, 2, 2, 2, 0, 1)
                self.fill_table.fill_table(list, self.ui.admin_lager_fehlendes_material, mode)

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