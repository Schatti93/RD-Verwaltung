from lager.data_lagerverwaltung import Database_Lagerverwaltung
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


class Uebersicht():
    def __init__(self, ui):
        self.ui = ui
        self.lager_uebersicht()


    # status bestellt einfuehren / nicht lieferbar / nicht bestellt
    def lager_uebersicht(self):
        liste = Database_Lagerverwaltung().get_liste()
        count = 0

        rows = self.ui.uebersicht_lager_table.rowCount()
        for i in range(0, rows):
            self.ui.uebersicht_lager_table.removeRow(0)

        for i in range(0, len(liste)):
            if liste[i][2] < liste[i][3]:
                count = count + 1
                row = self.ui.uebersicht_lager_table.rowCount()
                self.ui.uebersicht_lager_table.insertRow(row)

                #### daten modelieren - umwandeln in widget fuer die tabelle und anschließend mittig ausrichtig (align center)
                produkt = QtWidgets.QTableWidgetItem(liste[i][1])
                produkt.setTextAlignment(Qt.AlignCenter)
                vorhanden = QtWidgets.QTableWidgetItem(str(liste[i][2]))
                vorhanden.setTextAlignment(Qt.AlignCenter)
                mindest = QtWidgets.QTableWidgetItem(str(liste[i][3]))
                mindest.setTextAlignment(Qt.AlignCenter)
                max = QtWidgets.QTableWidgetItem(str(liste[i][4]))
                max.setTextAlignment(Qt.AlignCenter)
                ####
                self.ui.uebersicht_lager_table.setItem(row, 0, produkt)
                self.ui.uebersicht_lager_table.setItem(row, 1, vorhanden)
                self.ui.uebersicht_lager_table.setItem(row, 2, mindest)
                self.ui.uebersicht_lager_table.setItem(row, 3, max)
                self.ui.uebersicht_lager_table.horizontalHeader().setSectionResizeMode(1)
                self.ui.label_uebersicht_lager.setText("<html><head/><body><p><span style=\" color:#FF0043;\">Fehlendes Material</span></p></body></html>")
            else:
                continue
        if count == 0:
            self.ui.label_uebersicht_lager.setText("<html><head/><body><p><span style=\" color:#00FF00;\">Lager ist Voll</span></p></body></html>")
            self.ui.uebersicht_lager_table.setVisible(False)

