from PyQt5 import QtWidgets
from lager.data_lagerverwaltung import Database_Lagerverwaltung
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from uebersicht.uebersicht import Uebersicht

class Admin_Lager():
    def __init__(self, ui):
        self.ui = ui
        self.lager = Database_Lagerverwaltung()

        ### aufruf bei start des programms
        self.fehlendes_material()
        self.combobox_bestellung_einpflegen()
        self.alle_produkte_anzeigen_table()

        ### verbindungen mit Enter
        self.ui.admin_new_prod_artikel.returnPressed.connect(self.neues_produkt_table_insert)
        self.ui.admin_material_speichern_barcode.returnPressed.connect(self.bestellung_einpflegen_barcode_enter)
        self.ui.admin_material_speichern_anzahl.returnPressed.connect(self.bestellung_einpflegen_tabelle)
        self.ui.admin_del_prod_prod.returnPressed.connect(self.produkt_loeschen_tabelle_fuellen)
        self.ui.admin_del_prod_bar.returnPressed.connect(self.produkt_loeschen_tabelle_fuellen)


        ### verbindungen mit buttons
        self.ui.admin_new_prod_btn.clicked.connect(self.sammeln)
        self.ui.admin_del_prod_btn.clicked.connect(self.del_message_box)
        self.ui.admin_material_speichern_button.clicked.connect(self.bestellung_einpflegen)
        self.ui.admin_produkte_update.clicked.connect(self.produkte_aendern)

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
            self.lager.new_produkt(liste[0], liste[1], liste[2], liste[3], liste[4], liste[5], liste[6], "NULL")
            liste = []


    def fehlendes_material(self):
        liste = Database_Lagerverwaltung().get_liste()
        count = 0
        self.ui.admin_lager_fehlendes_material.setRowCount(0)

        for i in range(0, len(liste)):
            if liste[i][2] >= liste[i][3]:
                if liste[i][8] == "Ausreichend":
                    pass
                else:
                    Database_Lagerverwaltung().update_status(liste[i][1], "Ausreichend")
            else:
                if liste[i][8] == "NULL":
                    Database_Lagerverwaltung().update_status(liste[i][1], "Bestand zu gering")
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


    def produkt_loeschen_tabelle_fuellen(self):
        produkt = self.ui.admin_del_prod_prod.text()
        barcode = self.ui.admin_del_prod_bar.text()
        self.ui.admin_del_prod_label.setText("")
        if produkt == "" and barcode == "":
            pass

        elif barcode == "":
            item = self.lager.barcode_abfrage(produkt)
            rows = self.ui.admin_del_prod_table.rowCount()
            try:
                if item[0][0] == "":
                    self.ui.admin_del_prod_prod.setText("")
                else:
                    name =  QtWidgets.QTableWidgetItem(str(produkt))
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
            item = self.lager.produkt_abfrage(barcode)
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
            self.lager.del_produkt(item)
            self.ui.admin_del_prod_table.removeRow(0)
            self.ui.admin_del_prod_label.setText("<html><head/><body><p><span style=\" color:#00FF00;\">"
                                          "Eingabe Gespeichert</span></p></body></html>")
        self.update()


    def del_message_box(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Möchten Sie die Produkte wirklich löschen? \nDie Produkte werden unwiderruflich aus der Datenbank gelöscht.")
        msgBox.setWindowTitle("Wirklich löschen?")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.produkt_loeschen()

    def status_speichern(self):
        rows = self.ui.table_bestellt.rowCount()
        for i in reversed(range(0, rows)):
            name = self.ui.table_bestellt.item(i, 0).text()
            status = self.ui.table_bestellt.item(i, 1).text()
            self.lager.update_status(name, status)
            self.ui.table_bestellt.removeRow(i)
        self.update()

    def combobox_bestellung_einpflegen(self):
        liste_der_daten = self.lager.get_liste()
        liste_der_eintraege = ["----"]
        for eintrag in liste_der_daten:
            liste_der_eintraege.append(eintrag[1])
        self.ui.admin_material_speichern_combo.addItems(liste_der_eintraege)

    def bestellung_einpflegen_barcode_enter(self):
        barcode = self.ui.admin_material_speichern_barcode.text()
        produkt = self.lager.produkt_abfrage(barcode)
        index = self.ui.admin_material_speichern_combo.findText(produkt[0][0])
        self.ui.admin_material_speichern_combo.setCurrentIndex(index)
        self.ui.admin_material_speichern_anzahl.setFocus()

    def bestellung_einpflegen_tabelle(self):
        produkt = self.ui.admin_material_speichern_combo.currentText()
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
            self.lager.auffuellen(produkt, anzahl)
            self.ui.admin_material_speichern_table.removeRow(0)
        self.update()

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
            self.lager.update_alle_produkte(id, produkt, bestand, minimal, maximal, barcode, inhalt, artikelnr)
        self.update()

    def alle_produkte_anzeigen_table(self):
        self.ui.admin_lager_alle_produkte.setRowCount(0)
        alle_produkte = self.lager.get_liste()
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

    def update(self):
        Uebersicht(self.ui).lager_uebersicht()
        self.fehlendes_material()
        self.combobox_bestellung_einpflegen()
        self.alle_produkte_anzeigen_table()