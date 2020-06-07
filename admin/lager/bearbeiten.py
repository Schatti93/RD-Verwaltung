from admin.lager.admin_lager_data import Admin_Lager_Data
from admin.lager.update_lager import Update_Lager
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

class Bearbeiten():
    def __init__(self, ui):
        self.ui = ui
        self.data = Admin_Lager_Data()
        self.update = Update_Lager(self.ui)
        self.ui.admin_produkte_update.clicked.connect(self.produkte_aendern)

    def produkte_aendern(self):
        rows = self.ui.admin_lager_alle_produkte.rowCount()
        for element in range(0, rows):
            id = self.ui.admin_lager_alle_produkte.item(element, 0).text()
            produkt = self.ui.admin_lager_alle_produkte.item(element, 1).text()
            bestand = self.ui.admin_lager_alle_produkte.item(element, 2).text()
            minimal = self.ui.admin_lager_alle_produkte.item(element, 3).text()
            maximal = self.ui.admin_lager_alle_produkte.item(element, 4).text()
            barcode = self.ui.admin_lager_alle_produkte.item(element, 5).text()
            inhalt = self.ui.admin_lager_alle_produkte.item(element, 6).text()
            artikelnr = self.ui.admin_lager_alle_produkte.item(element, 7).text()
            self.data.update_alle_produkte(id, produkt, bestand, minimal, maximal, barcode, inhalt, artikelnr)
        self.update.update()

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