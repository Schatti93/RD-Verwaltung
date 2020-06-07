from admin.lager.admin_lager_data import Admin_Lager_Data
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from admin.lager.update_lager import Update_Lager

class Material_einpflegen():
    def __init__(self, ui):
        self.ui = ui
        self.data = Admin_Lager_Data()
        self.update = Update_Lager(self.ui)
        # return actions
        self.ui.admin_material_speichern_barcode.returnPressed.connect(self.bestellung_einpflegen_barcode_enter)
        self.ui.admin_material_speichern_anzahl.returnPressed.connect(self.bestellung_einpflegen_tabelle)

        # button actions
        self.ui.admin_material_speichern_button.clicked.connect(self.bestellung_einpflegen)

    def combobox_bestellung_einpflegen(self):
        self.ui.admin_material_speichern_combo.clear()
        liste_der_daten = self.data.get_liste()
        liste_der_eintraege = ["---"]
        for eintrag in liste_der_daten:
            liste_der_eintraege.append(eintrag[1])
        self.ui.admin_material_speichern_combo.addItems(liste_der_eintraege)

    def bestellung_einpflegen_barcode_enter(self):
        barcode = self.ui.admin_material_speichern_barcode.text()
        produkt = self.data.produkt_abfrage(barcode)
        index = self.ui.admin_material_speichern_combo.findText(produkt[0][0])
        self.ui.admin_material_speichern_combo.setCurrentIndex(index)
        self.ui.admin_material_speichern_anzahl.setFocus()

    def bestellung_einpflegen_tabelle(self):
        produkt = self.ui.admin_material_speichern_combo.currentText()
        if produkt == "---":
            produkt = self.ui.admin_material_speichern_barcode.text()
        anzahl = self.ui.admin_material_speichern_anzahl.text()
        rows = self.ui.admin_material_speichern_table.rowCount()
        self.ui.admin_material_speichern_table.insertRow(rows)
        self.ui.admin_material_speichern_table.setItem(rows, 0, QtWidgets.QTableWidgetItem(produkt))
        self.ui.admin_material_speichern_table.setItem(rows, 1, QtWidgets.QTableWidgetItem(anzahl))

    def bestellung_einpflegen(self):
        rows = self.ui.admin_material_speichern_table.rowCount()
        for eintrag in range(0, rows):
            produkt = self.ui.admin_material_speichern_table.item(0, 0).text()
            anzahl = int(self.ui.admin_material_speichern_table.item(0, 1).text())
            vorhanden = self.data.produkt_abfrage(produkt)
            if len(vorhanden) > 0:
                self.data.auffuellen(produkt, anzahl)
                self.ui.admin_material_speichern_table.removeRow(0)
            else:
                print("nicht vorhanden")
        self.update.update()

    def status_speichern(self):
        rows = self.ui.table_bestellt.rowCount()
        for i in reversed(range(0, rows)):
            name = self.ui.table_bestellt.item(i, 0).text()
            status = self.ui.table_bestellt.item(i, 1).text()
            self.data.update_status(name, status)
            self.ui.table_bestellt.removeRow(i)
        self.update.update()