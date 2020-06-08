from admin.lager.admin_lager_data import Admin_Lager_Data
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from admin.pdf_bestellung.pdf_bestellung import Pdf_Bestellung
from uebersicht.uebersicht import Uebersicht
from admin.lager.update_lager import Update_Lager
from admin.lager.online_bestellung import Online_Bestellung
from PyQt5 import QtCore

class Fehlendes_Material():
    def __init__(self, ui):
        self.ui = ui
        self.data = Admin_Lager_Data()
        self.ui.pdf_erstellen.clicked.connect(Pdf_Bestellung(self.ui).pdf_erstellen)
        self.update = Update_Lager(self.ui)
        self.bestellen = Online_Bestellung()
        #self.ui.lager_bestellung.clicked.connect(self.bestellen.nachbestellen)

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
                    status = "Bestand zu gering"
                else:
                    status = "Bestand zu gering"
                status = QtWidgets.QTableWidgetItem(status)
                status.setTextAlignment(Qt.AlignCenter)
                status.setFlags(QtCore.Qt.ItemIsEnabled)

                produkt = QtWidgets.QTableWidgetItem(liste[i][1])
                produkt.setTextAlignment(Qt.AlignCenter)
                produkt.setFlags(QtCore.Qt.ItemIsEnabled)
                vorhanden = QtWidgets.QTableWidgetItem()
                vorhanden.setTextAlignment(Qt.AlignCenter)
                vorhanden.setData(QtCore.Qt.EditRole, liste[i][2])
                mindest = QtWidgets.QTableWidgetItem()
                mindest.setTextAlignment(Qt.AlignCenter)
                mindest.setData(QtCore.Qt.EditRole, liste[i][3])
                max = QtWidgets.QTableWidgetItem()
                max.setTextAlignment(Qt.AlignCenter)
                max.setData(QtCore.Qt.EditRole, liste[i][4])
                artikelnr = QtWidgets.QTableWidgetItem(str(liste[i][7]))
                artikelnr.setTextAlignment(Qt.AlignCenter)


                row = self.ui.admin_lager_fehlendes_material.rowCount()
                self.ui.admin_lager_fehlendes_material.insertRow(row)
                self.ui.admin_lager_fehlendes_material.setItem(row, 0, produkt)
                self.ui.admin_lager_fehlendes_material.setItem(row, 1, vorhanden)
                self.ui.admin_lager_fehlendes_material.setItem(row, 2, mindest)
                self.ui.admin_lager_fehlendes_material.setItem(row, 3, max)
                self.ui.admin_lager_fehlendes_material.setItem(row, 4, artikelnr)
                self.ui.admin_lager_fehlendes_material.setItem(row, 5, status)
                self.ui.admin_lager_fehlendes_material.horizontalHeader().setSectionResizeMode(1)
        Uebersicht(self.ui).lager_uebersicht()
        self.update.update_from_fehlendes_material()