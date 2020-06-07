from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from admin.lager.admin_lager_data import Admin_Lager_Data
from PyQt5.QtWidgets import QMessageBox
from admin.lager.update_lager import Update_Lager

class Neu_Loeschen():
    def __init__(self, ui):
        self.ui = ui
        self.data = Admin_Lager_Data()
        self.update = Update_Lager(self.ui)

        #return actions
        self.ui.admin_new_prod_artikel.returnPressed.connect(self.neues_produkt_table_insert)
        self.ui.admin_del_prod_prod.returnPressed.connect(self.produkt_loeschen_tabelle_fuellen)
        self.ui.admin_del_prod_bar.returnPressed.connect(self.produkt_loeschen_tabelle_fuellen)
        # button actions
        self.ui.admin_del_prod_btn.clicked.connect(self.del_message_box)
        self.ui.admin_new_prod_btn.clicked.connect(self.sammeln)

    def neues_produkt_table_insert(self):
        produkt = QtWidgets.QTableWidgetItem(self.ui.admin_new_prod_prod.text())
        produkt.setTextAlignment(Qt.AlignCenter)
        bestand = QtWidgets.QTableWidgetItem(self.ui.admin_new_prod_bes.text())
        bestand.setTextAlignment(Qt.AlignCenter)
        min = QtWidgets.QTableWidgetItem(self.ui.admin_new_prod_min.text())
        min.setTextAlignment(Qt.AlignCenter)
        max = QtWidgets.QTableWidgetItem(self.ui.admin_new_prod_max.text())
        max.setTextAlignment(Qt.AlignCenter)
        barcode = QtWidgets.QTableWidgetItem(self.ui.admin_new_prod_bar.text())
        barcode.setTextAlignment(Qt.AlignCenter)
        inhalt = QtWidgets.QTableWidgetItem(self.ui.admin_new_prod_inhalt_menge.text())
        inhalt.setTextAlignment(Qt.AlignCenter)
        artikel_nr = QtWidgets.QTableWidgetItem(self.ui.admin_new_prod_artikel.text())
        artikel_nr.setTextAlignment(Qt.AlignCenter)
        row = self.ui.admin_new_prod_table.rowCount()
        self.ui.admin_new_prod_table.insertRow(row)
        self.ui.admin_new_prod_table.setItem(row, 0, QtWidgets.QTableWidgetItem(produkt))
        self.ui.admin_new_prod_table.setItem(row, 1, QtWidgets.QTableWidgetItem(bestand))
        self.ui.admin_new_prod_table.setItem(row, 2, QtWidgets.QTableWidgetItem(min))
        self.ui.admin_new_prod_table.setItem(row, 3, QtWidgets.QTableWidgetItem(max))
        self.ui.admin_new_prod_table.setItem(row, 4, QtWidgets.QTableWidgetItem(barcode))
        self.ui.admin_new_prod_table.setItem(row, 5, QtWidgets.QTableWidgetItem(inhalt))
        self.ui.admin_new_prod_table.setItem(row, 6, QtWidgets.QTableWidgetItem(artikel_nr))
        self.ui.admin_new_prod_table.resizeColumnsToContents()
        self.ui.admin_new_prod_table.horizontalHeader().setSectionResizeMode(1)

    def sammeln(self):
        liste = []
        rows = self.ui.admin_new_prod_table.rowCount()
        for i in range(0, rows):
            for J in range(0, 7):
                liste.append(self.ui.admin_new_prod_table.item(0, J).text())
            self.ui.admin_new_prod_table.removeRow(0)
            self.data.new_produkt(liste[0], liste[1], liste[2], liste[3], liste[4], liste[5], liste[6], "NULL")
            liste = []
        self.update.update()

    def produkt_loeschen_tabelle_fuellen(self):
        produkt = self.ui.admin_del_prod_prod.text()
        barcode = self.ui.admin_del_prod_bar.text()
        self.ui.admin_del_prod_label.setText("")
        if produkt == "" and barcode == "":
            pass

        elif barcode == "":
            item = self.data.barcode_abfrage(produkt)
            rows = self.ui.admin_del_prod_table.rowCount()
            try:
                if item[0][0] == "":
                    self.ui.admin_del_prod_prod.setText("")
                else:
                    name = QtWidgets.QTableWidgetItem(str(produkt))
                    name.setTextAlignment(Qt.AlignCenter)
                    barcode = QtWidgets.QTableWidgetItem(str(item[0][0]))
                    barcode.setTextAlignment(Qt.AlignCenter)
                    self.ui.admin_del_prod_table.insertRow(rows)
                    self.ui.admin_del_prod_table.setItem(rows, 0, name)
                    self.ui.admin_del_prod_table.setItem(rows, 1, barcode)
                    self.ui.admin_del_prod_prod.setText("")
                    self.ui.admin_lager_loeschen_error.setText("")
                    self.ui.admin_del_prod_table.horizontalHeader().setSectionResizeMode(1)
            except IndexError:
                self.ui.admin_lager_loeschen_error.setText("<html><head/><body><p><span style=\" color:#ff0000;\">"
                                                           "Produkt nicht vorhanden.</span></p></body></html>")

        elif produkt == "":
            item = self.data.produkt_abfrage(barcode)
            rows = self.ui.admin_del_prod_table.rowCount()
            try:
                if item[0][0] == "":
                    self.ui.admin_del_prod_bar.setText("")
                else:
                    name = QtWidgets.QTableWidgetItem(str(item[0][0]))
                    name.setTextAlignment(Qt.AlignCenter)
                    barcode = QtWidgets.QTableWidgetItem(str(barcode))
                    barcode.setTextAlignment(Qt.AlignCenter)
                    self.ui.admin_del_prod_table.insertRow(rows)
                    self.ui.admin_del_prod_table.setItem(rows, 0, name)
                    self.ui.admin_del_prod_table.setItem(rows, 1, barcode)
                    self.ui.admin_del_prod_table.horizontalHeader().setSectionResizeMode(1)
                    self.ui.admin_del_prod_bar.setText("")
                    self.ui.admin_lager_loeschen_error.setText("")
            except IndexError:
                self.ui.admin_lager_loeschen_error.setText("<html><head/><body><p><span style=\" color:#ff0000;\">"
                                                           "Produkt nicht vorhanden.</span></p></body></html>")

    def produkt_loeschen(self):
        rows = self.ui.admin_del_prod_table.rowCount()
        for i in range(0, rows):
            item = self.ui.admin_del_prod_table.item(0, 0).text()
            self.data.del_produkt(item)
            self.ui.admin_del_prod_table.removeRow(0)
            self.ui.admin_del_prod_label.setText("<html><head/><body><p><span style=\" color:#00FF00;\">"
                                          "Eingabe Gespeichert</span></p></body></html>")
        self.update.update()

    def del_message_box(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Möchten Sie die Produkte wirklich löschen? \nDie Produkte werden unwiderruflich aus der Datenbank gelöscht.")
        msgBox.setWindowTitle("Wirklich löschen?")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.produkt_loeschen()