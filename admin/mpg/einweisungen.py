from admin.mpg.mpg_data import Mpg_Data
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

class Einweisungen():
    def __init__(self, ui):
        self.ui = ui
        self.data = Mpg_Data()

        self.ui.einweisung_speichern_btn.clicked.connect(self.geraete_einweisung)
        self.ui.einweisung_standardwerte_loeschen_btn.clicked.connect \
            (self.standard_werte_loeschen)
        self.ui.einweisung_tabelle_filtern_ma_combo.currentTextChanged.connect \
            (self.tabelle_nach_ma_filtern)
        self.ui.einweisung_tabelle_filtern_geraet_combo.currentTextChanged.connect(
            self.einweisung_tabelle_filtern_geraet_auswahl)
        self.ui.einweisung_tabelle_filtern_software_combo.currentTextChanged.connect(
            self.einweisung_tabelle_filtern_nach_software)

    def combos_ma_fuellen(self):
        self.ui.einweisung_ma_combo.clear()
        self.ui.einweisung_ma_standard_combo.clear()
        liste_der_eintraege = self.data.mitarbeiter_abfragen()
        combo_eintraege = ["---"]
        for element in range(0, len(liste_der_eintraege)):
            eintrag = str(liste_der_eintraege[element][2]) + ", " + \
                      str(liste_der_eintraege[element][1])
            combo_eintraege.append(eintrag)
        self.ui.einweisung_ma_combo.addItems(sorted(combo_eintraege))
        self.ui.einweisung_ma_standard_combo.addItems(sorted(combo_eintraege))

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

    def tabellen_filter_ma_combo_fuellen(self):
        self.ui.einweisung_tabelle_filtern_ma_combo.clear()
        liste_der_daten = self.data.einweisungen_abfragen()
        combo_eintraege = ["---"]
        for element in range(0, len(liste_der_daten)):
            eintrag = liste_der_daten[element][4]
            if eintrag in combo_eintraege:
                pass
            else:
                combo_eintraege.append(eintrag)
        self.ui.einweisung_tabelle_filtern_ma_combo.addItems(sorted(combo_eintraege))

    def einweisung_tabelle_fuellen(self):
        self.ui.einweisung_tabelle.setRowCount(0)
        einweisungen = self.data.einweisungen_abfragen()
        for element in range(0, len(einweisungen)):
            count = 0
            status = self.ma_status_ermitteln(einweisungen[element][4])
            rows = self.ui.einweisung_tabelle.rowCount()
            self.ui.einweisung_tabelle.insertRow(rows)
            for eigenschaft in range(1, len(einweisungen[element])):
                einzusetzen = QtWidgets.QTableWidgetItem(einweisungen[element][eigenschaft])
                einzusetzen.setTextAlignment(Qt.AlignCenter)
                self.ui.einweisung_tabelle.setItem(rows, count, QtWidgets.QTableWidgetItem(einzusetzen))
                count += 1
                if eigenschaft == 4:
                    einzusetzen = QtWidgets.QTableWidgetItem(status)
                    einzusetzen.setTextAlignment(Qt.AlignCenter)
                    self.ui.einweisung_tabelle.setItem(rows, count, QtWidgets.QTableWidgetItem(einzusetzen))
                    count += 1
        self.ui.einweisung_tabelle.horizontalHeader().setSectionResizeMode(1)

    def geraete_einweisung(self):
        if self.ui.einweisung_geraete_combo_standard.currentText() == "---":
            geraet = self.ui.einweisung_geraete_combo.currentText()
        else:
            geraet = self.ui.einweisung_geraete_combo_standard.currentText()

        if self.ui.einweisung_softwareversion_standard.text() == "":
            softwareversion = self.ui.einweisung_softwareversion.text()
        else:
            softwareversion = self.ui.einweisung_softwareversion_standard.text()

        if self.ui.einweisung_datum_standard.text() == "":
            datum = self.ui.einweisung_datum.text()
        else:
            datum = self.ui.einweisung_datum_standard.text()

        if self.ui.einweisung_ma_standard_combo.currentText() == "---":
            eingewiesener = self.ui.einweisung_ma_combo.currentText()
        else:
            eingewiesener = self.ui.einweisung_ma_standard_combo.currentText()
        status = self.ma_status_ermitteln(eingewiesener)

        if self.ui.einweisung_einweisender_standard.text() == "":
            einweisender = self.ui.einweisung_einweisender.text()
        else:
            einweisender = self.ui.einweisung_einweisender_standard.text()

        if self.ui.einweisung_original_standard.text() == "":
            original = self.ui.einweisung_original.text()
        else:
            original = self.ui.einweisung_original_standard.text()

        self.data.einweisung_speichern(geraet, softwareversion, datum, eingewiesener, einweisender,
                                       original)
        rows = self.ui.einweisung_tabelle.rowCount()
        self.ui.einweisung_tabelle.insertRow(rows)
        liste_der_eintraege = [geraet, softwareversion, datum, eingewiesener, status\
                               ,einweisender, original]
        count = 0
        for element in range(0, len(liste_der_eintraege)):
            einzusetzen = QtWidgets.QTableWidgetItem(liste_der_eintraege[element])
            einzusetzen.setTextAlignment(Qt.AlignCenter)
            self.ui.einweisung_tabelle.setItem(rows, count, QtWidgets.QTableWidgetItem(einzusetzen))
            count += 1

        self.ui.einweisung_geraete_combo.setCurrentIndex(0)
        self.ui.einweisung_softwareversion.setText("")
        self.ui.einweisung_datum.setText("")
        self.ui.einweisung_ma_combo.setCurrentIndex(0)
        self.ui.einweisung_einweisender.setText("")
        self.ui.einweisung_original.setText("")
        self.tabellen_filter_ma_combo_fuellen()

    def standard_werte_loeschen(self):
        self.ui.einweisung_geraete_combo_standard.setCurrentIndex(0)
        self.ui.einweisung_softwareversion_standard.setText("")
        self.ui.einweisung_datum_standard.setText("")
        self.ui.einweisung_ma_standard_combo.setCurrentIndex(0)
        self.ui.einweisung_einweisender_standard.setText("")
        self.ui.einweisung_original_standard.setText("")

    def tabelle_nach_ma_filtern(self):
        self.ui.einweisung_tabelle.setRowCount(0)
        ma = self.ui.einweisung_tabelle_filtern_ma_combo.currentText()
        daten = self.data.einweisungs_daten_gefiltert_ma(ma)
        for element in range(0, len(daten)):
            count = 0
            rows = self.ui.einweisung_tabelle.rowCount()
            status = self.ma_status_ermitteln(daten[element][4])
            self.ui.einweisung_tabelle.insertRow(rows)
            for eigenschaft in range(1, len(daten[element])):
                einzusetzen = QtWidgets.QTableWidgetItem(daten[element][eigenschaft])
                einzusetzen.setTextAlignment(Qt.AlignCenter)
                self.ui.einweisung_tabelle.setItem(rows, count, QtWidgets.QTableWidgetItem(einzusetzen))
                count += 1
                if eigenschaft == 4:
                    einzusetzen = QtWidgets.QTableWidgetItem(status)
                    einzusetzen.setTextAlignment(Qt.AlignCenter)
                    self.ui.einweisung_tabelle.setItem(rows, count, QtWidgets.QTableWidgetItem(einzusetzen))
                    count += 1
        self.ui.einweisung_tabelle.horizontalHeader().setSectionResizeMode(1)
        eintraege = self.ui.einweisung_tabelle.rowCount()
        self.ui.einweisung_tabelle_filtern_anzahl.setText(
            "<html><head/><body><p><span style=\" color:#ffffff;\">" + str(eintraege) +
            "</span></p></body></html>")

        if ma == "---":
           self.einweisung_tabelle_fuellen()

    def einweisung_tabelle_filtern_geraet_auswahl(self):
        auswahl = self.ui.einweisung_tabelle_filtern_geraet_combo.currentText()
        if auswahl == "---":
            self.tabelle_filtern_software_combo_fuellen()
            self.einweisung_tabelle_fuellen()
        else:
            self.ui.einweisung_tabelle_filtern_ma_combo.setCurrentIndex(0)
            self.tabelle_filtern_software_combo_fuellen()
            self.einweisung_tabelle_filtern_geraet_anzeigen()

    def einweisung_tabelle_filtern_nach_software(self):
        self.ui.einweisung_tabelle.setRowCount(0)
        geraet = self.ui.einweisung_tabelle_filtern_geraet_combo.currentText()
        software = self.ui.einweisung_tabelle_filtern_software_combo.currentText()
        daten = self.data.einweisungs_daten_gefiltert_software(geraet, software)
        for element in range(0, len(daten)):
            count = 0
            rows = self.ui.einweisung_tabelle.rowCount()
            self.ui.einweisung_tabelle.insertRow(rows)
            for eigenschaft in range(1, len(daten[element])):
                einzusetzen = QtWidgets.QTableWidgetItem(daten[element][eigenschaft])
                einzusetzen.setTextAlignment(Qt.AlignCenter)
                self.ui.einweisung_tabelle.setItem(rows, count, QtWidgets.QTableWidgetItem(einzusetzen))
                count += 1
        self.ui.einweisung_tabelle.horizontalHeader().setSectionResizeMode(1)
        eintraege = self.ui.einweisung_tabelle.rowCount()
        self.ui.einweisung_tabelle_filtern_anzahl.setText(
            "<html><head/><body><p><span style=\" color:#ffffff;\">" + str(eintraege) +
            "</span></p></body></html>")

    def tabelle_filtern_software_combo_fuellen(self):
        self.ui.einweisung_tabelle_filtern_software_combo.clear()
        geraet = self.ui.einweisung_tabelle_filtern_geraet_combo.currentText()
        liste_der_eintraege = ["---"]
        if geraet == "---":
            pass
        else:
            daten = self.data.softwareversion_abfragen(geraet)

            for element in range(0, len(daten)):
                liste_der_eintraege.append(daten[element][0])
        self.ui.einweisung_tabelle_filtern_software_combo.addItems(liste_der_eintraege)

    def einweisung_tabelle_filtern_geraet_anzeigen(self):
        self.ui.einweisung_tabelle.setRowCount(0)
        geraet = self.ui.einweisung_tabelle_filtern_geraet_combo.currentText()
        daten = self.data.einweisungs_daten_gefiltert_geraet(geraet)
        for element in range(0, len(daten)):
            count = 0
            status = self.ma_status_ermitteln(daten[element][4])
            rows = self.ui.einweisung_tabelle.rowCount()
            self.ui.einweisung_tabelle.insertRow(rows)
            for eigenschaft in range(1, len(daten[element])):
                einzusetzen = QtWidgets.QTableWidgetItem(daten[element][eigenschaft])
                einzusetzen.setTextAlignment(Qt.AlignCenter)
                self.ui.einweisung_tabelle.setItem(rows, count, QtWidgets.QTableWidgetItem(einzusetzen))
                count += 1
                if eigenschaft == 4:
                    einzusetzen = QtWidgets.QTableWidgetItem(status)
                    einzusetzen.setTextAlignment(Qt.AlignCenter)
                    self.ui.einweisung_tabelle.setItem(rows, count, QtWidgets.QTableWidgetItem(einzusetzen))
                    count += 1
        self.ui.einweisung_tabelle.horizontalHeader().setSectionResizeMode(1)
        eintraege = self.ui.einweisung_tabelle.rowCount()
        self.ui.einweisung_tabelle_filtern_anzahl.setText("<html><head/><body><p><span style=\" "
                                                          "color:#ffffff;\">"+ str(eintraege) +
                                                          "</span></p></body></html>")

    def ma_status_ermitteln(self, name):
        nachname = name.split(", ")[0]
        vorname = name.split(", ")[1]
        status = self.data.mitarbeiter_status_abfragen(nachname, vorname)
        return status[0][0]