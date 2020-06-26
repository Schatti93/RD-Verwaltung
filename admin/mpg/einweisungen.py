from admin.mpg.mpg_data import Mpg_Data
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import datetime
from PyQt5 import QtCore
from error_message_boxes import Error_Message_Boxes

class Einweisungen():
    def __init__(self, ui):
        self.ui = ui
        self.error = Error_Message_Boxes()
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

    def check_neueste_software(self, geraet):
        daten = self.data.softwareversion_check(geraet)
        neuste_version = ""
        aktuellstes_datum = ""
        for element in range(0, len(daten)):
            if element == 0:
                neuste_version = daten[element][0]
                aktuellstes_datum = daten[element][1]
            else:
                datum_aktuell = aktuellstes_datum.split(".")
                datum_aktuell = datetime.date(year=int(datum_aktuell[2]), month=int(datum_aktuell[1]),
                              day=int(datum_aktuell[0]))
                pruef_datum = daten[element][1].split(".")
                pruef_datum = datetime.date(year=int(pruef_datum[2]), month=int(pruef_datum[1]),
                              day=int(pruef_datum[0]))
                check = datum_aktuell - pruef_datum
                if check.days < 0:
                    aktuellstes_datum = daten[element][1]
                    neuste_version = daten[element][0]
        return_liste = [geraet, neuste_version]
        return return_liste

    def fehlende_einweisung_fuellen(self):
        self.ui.fehlende_einweisungen_table.setRowCount(0)
        geraete = self.data.geraete_abfragen()
        liste_der_geraete = []
        for element in range(0, len(geraete)):
            if geraete[element][1] in liste_der_geraete:
                pass
            else:
                liste_der_geraete.append(geraete[element][1])
        for element in liste_der_geraete:
            checkliste = self.check_neueste_software(element)
            eintraege = self.data.einweisungs_daten_gefiltert_geraet(element)
            for eintrag in range(0, len(eintraege)):
                if eintraege[eintrag][2] == checkliste[1]:
                    pass
                else:
                    status = self.ma_status_ermitteln(eintraege[eintrag][4])
                    if status != 0:
                        rows = self.ui.fehlende_einweisungen_table.rowCount()
                        self.ui.fehlende_einweisungen_table.insertRow(rows)

                        einzusetzen = QtWidgets.QTableWidgetItem(eintraege[eintrag][4])
                        einzusetzen.setTextAlignment(Qt.AlignCenter)
                        self.ui.fehlende_einweisungen_table.setItem(rows, 0, QtWidgets.QTableWidgetItem(einzusetzen))

                        einzusetzen = QtWidgets.QTableWidgetItem(eintraege[eintrag][1])
                        einzusetzen.setTextAlignment(Qt.AlignCenter)
                        self.ui.fehlende_einweisungen_table.setItem(rows, 1, QtWidgets.QTableWidgetItem(einzusetzen))

                        einzusetzen = QtWidgets.QTableWidgetItem(eintraege[eintrag][2])
                        einzusetzen.setTextAlignment(Qt.AlignCenter)
                        self.ui.fehlende_einweisungen_table.setItem(rows, 2, QtWidgets.QTableWidgetItem(einzusetzen))
        self.ui.fehlende_einweisungen_table.horizontalHeader().setSectionResizeMode(1)

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
            status = self.ma_status_ermitteln(eintrag)
            if eintrag in combo_eintraege:
                pass
            else:
                if status == 0:
                    pass
                else:
                    combo_eintraege.append(eintrag)
        self.ui.einweisung_tabelle_filtern_ma_combo.addItems(sorted(combo_eintraege))

    def einweisung_tabelle_fuellen(self):
        self.ui.einweisung_tabelle.setRowCount(0)
        einweisungen = self.data.einweisungen_abfragen()
        self.tabelle_gefiltert_fuellen(einweisungen)
        self.ui.einweisung_tabelle_filtern_anzahl.setText(str(0))
        self.ui.einweisung_tabelle_filtern_anzahl.setStyleSheet("color:#ffffff;")

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

        if self.ui.einweisung_einweisender_standard.text() == "":
            einweisender = self.ui.einweisung_einweisender.text()
        else:
            einweisender = self.ui.einweisung_einweisender_standard.text()

        if self.ui.einweisung_original_standard.text() == "":
            original = self.ui.einweisung_original.text()
        else:
            original = self.ui.einweisung_original_standard.text()

        check = self.data.einweisung_checken(eingewiesener, geraet)
        datum_check = self.datum_pruefen(datum)
        if datum_check == 1:
            if len(check) > 0:
                self.data.einweisung_updaten(geraet, softwareversion, datum, eingewiesener \
                                             ,einweisender, original)
            else:
                self.data.einweisung_speichern(geraet, softwareversion, datum, eingewiesener, einweisender,
                                               original)

            self.ui.einweisung_geraete_combo.setCurrentIndex(0)
            self.ui.einweisung_softwareversion.setText("")
            self.ui.einweisung_datum.setText("")
            self.ui.einweisung_ma_combo.setCurrentIndex(0)
            self.ui.einweisung_einweisender.setText("")
            self.ui.einweisung_original.setText("")
            self.ui.einweisung_tabelle_filtern_anzahl.setText(str(0))
            self.ui.einweisung_tabelle_filtern_anzahl.setStyleSheet("color:#ffffff;")
            self.tabellen_filter_ma_combo_fuellen()
            self.einweisung_tabelle_fuellen()
            self.fehlende_einweisung_fuellen()
        else:
            self.error.message_box_only_ok("Das Datum wurde nicht korrekt angegeben", "Fehlerhaftes Datum")

    def standard_werte_loeschen(self):
        self.ui.einweisung_geraete_combo_standard.setCurrentIndex(0)
        self.ui.einweisung_softwareversion_standard.setText("")
        self.ui.einweisung_datum_standard.setText("")
        self.ui.einweisung_ma_standard_combo.setCurrentIndex(0)
        self.ui.einweisung_einweisender_standard.setText("")
        self.ui.einweisung_original_standard.setText("")

    def tabelle_gefiltert_fuellen(self, daten):
        for element in range(0, len(daten)):
            count = 0
            rows = self.ui.einweisung_tabelle.rowCount()
            status = self.ma_status_ermitteln(daten[element][4])
            if status != 0:
                self.ui.einweisung_tabelle.insertRow(rows)
                for eigenschaft in range(1, len(daten[element])):
                    einzusetzen = QtWidgets.QTableWidgetItem(daten[element][eigenschaft])
                    einzusetzen.setTextAlignment(Qt.AlignCenter)
                    self.ui.einweisung_tabelle.setItem(rows, count, einzusetzen)
                    count += 1
                    if eigenschaft == 4:
                        einzusetzen = QtWidgets.QTableWidgetItem(status)
                        einzusetzen.setTextAlignment(Qt.AlignCenter)
                        einzusetzen.setFlags(QtCore.Qt.ItemIsEnabled)
                        self.ui.einweisung_tabelle.setItem(rows, count, einzusetzen)
                        count += 1
        self.ui.einweisung_tabelle.horizontalHeader().setSectionResizeMode(1)

    def tabelle_nach_ma_filtern(self):
        ma = self.ui.einweisung_tabelle_filtern_ma_combo.currentText()
        if ma == "---":
            if int(self.ui.einweisung_tabelle_filtern_anzahl.text()) > 0:
                if self.ui.einweisung_tabelle_filtern_geraet_combo.currentText() == "---":
                    self.einweisung_tabelle_fuellen()
        elif ma == "":
            pass
        else:
            self.ui.einweisung_tabelle_filtern_geraet_combo.setCurrentIndex(0)
            self.ui.einweisung_tabelle_filtern_software_combo.setCurrentIndex(0)
            self.ui.einweisung_tabelle.setRowCount(0)
            daten = self.data.einweisungs_daten_gefiltert_ma(ma)
            self.tabelle_gefiltert_fuellen(daten)
            eintraege = self.ui.einweisung_tabelle.rowCount()
            self.ui.einweisung_tabelle_filtern_anzahl.setText(str(eintraege))
            self.ui.einweisung_tabelle_filtern_anzahl.setStyleSheet("color:#ffffff;")

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
        software = self.ui.einweisung_tabelle_filtern_software_combo.currentText()
        if software == "---":
            pass
        elif software == "":
            pass
        else:
            self.ui.einweisung_tabelle.setRowCount(0)
            geraet = self.ui.einweisung_tabelle_filtern_geraet_combo.currentText()
            daten = self.data.einweisungs_daten_gefiltert_software(geraet, software)
            self.tabelle_gefiltert_fuellen(daten)
            eintraege = self.ui.einweisung_tabelle.rowCount()
            self.ui.einweisung_tabelle_filtern_anzahl.setText(str(eintraege))
            self.ui.einweisung_tabelle_filtern_anzahl.setStyleSheet("color:#ffffff;")

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
        geraet = self.ui.einweisung_tabelle_filtern_geraet_combo.currentText()
        if geraet == "---":
            if int(self.ui.einweisung_tabelle_filtern_anzahl.text()) > 0:
                if self.ui.einweisung_tabelle_filtern_ma_combo.currentText() == "---":
                    self.einweisung_tabelle_fuellen()
        elif geraet == "":
            pass
        else:
            self.ui.einweisung_tabelle.setRowCount(0)
            daten = self.data.einweisungs_daten_gefiltert_geraet(geraet)
            self.tabelle_gefiltert_fuellen(daten)
            eintraege = self.ui.einweisung_tabelle.rowCount()
            self.ui.einweisung_tabelle_filtern_anzahl.setText(str(eintraege))
            self.ui.einweisung_tabelle_filtern_anzahl.setStyleSheet("color:#ffffff;")

    def ma_status_ermitteln(self, name):
        if "," in name:
            nachname = name.split(", ")[0]
            vorname = name.split(", ")[1]
            status = self.data.mitarbeiter_status_abfragen(nachname, vorname)
            if len(status) > 0:
                return status[0][0]
            else:
                return 0
        else:
            return 0

    def datum_pruefen(self, datum):
        liste_der_daten = datum.split(".")
        wert = 1
        try:
            datetime.date(year=int(liste_der_daten[2]), month=int(liste_der_daten[1]),
                              day=int(liste_der_daten[0]))
        except ValueError:
            wert = 0
        return wert