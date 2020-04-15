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
        status_anzeige = ""

        rows = self.ui.uebersicht_lager_table.rowCount()
        for i in range(0, rows):
            self.ui.uebersicht_lager_table.removeRow(0)

        for i in range(0, len(liste)):
            if liste[i][2] < liste[i][3]:
                if liste[i][8] == "NULL":
                    Database_Lagerverwaltung().update_status(liste[i][1], "Bestand zu gering")
                    status = QtWidgets.QTableWidgetItem("Bestand zu gering")
                    status.setTextAlignment(Qt.AlignCenter)
                    status_anzeige = "Bestand zu gering"
                else:
                    if liste[i][8] == "Bestand zu gering":
                        status_anzeige = "Bestand zu gering"
                    status = QtWidgets.QTableWidgetItem(str(liste[i][8]))
                    status.setTextAlignment(Qt.AlignCenter)


                count = count + 1
                row = self.ui.uebersicht_lager_table.rowCount()
                self.ui.uebersicht_lager_table.insertRow(row)
                print(status_anzeige)
                #### daten modelieren - umwandeln in widget fuer die tabelle und anschließend mittig ausrichtig (align center)
                produkt = QtWidgets.QTableWidgetItem(liste[i][1])
                produkt.setTextAlignment(Qt.AlignCenter)
                vorhanden = QtWidgets.QTableWidgetItem(str(liste[i][2]))
                vorhanden.setTextAlignment(Qt.AlignCenter)
                mindest = QtWidgets.QTableWidgetItem(str(liste[i][3]))
                mindest.setTextAlignment(Qt.AlignCenter)
                ####
                self.ui.uebersicht_lager_table.setItem(row, 0, produkt)
                self.ui.uebersicht_lager_table.setItem(row, 1, vorhanden)
                self.ui.uebersicht_lager_table.setItem(row, 2, mindest)
                self.ui.uebersicht_lager_table.setItem(row, 3, status)
                self.ui.uebersicht_lager_table.horizontalHeader().setSectionResizeMode(1)


            else:
                continue
        if count == 0:
            self.ui.label_uebersicht_lager.setText("Lager ist Voll")
            self.ui.label_uebersicht_lager.setStyleSheet("color:#ffffff; font-size:13pt; border: 1px solid #00FF00; border-radius: 5px")
            self.ui.uebersicht_lager_table.setVisible(False)
        elif status_anzeige == "Bestand zu gering":
            self.ui.label_uebersicht_lager.setText("Fehlendes Material")
            self.ui.label_uebersicht_lager.setStyleSheet(
                "color:#ffffff; font-size:13pt; border: 1px solid red; border-radius: 5px")
        else:
            self.ui.label_uebersicht_lager.setText("Bestellt / Nicht Lieferbar / wird bestellt")
            self.ui.label_uebersicht_lager.setStyleSheet(
                "color:#ffffff; font-size:13pt; border: 1px solid orange; border-radius: 5px")



