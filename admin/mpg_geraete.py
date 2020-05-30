from admin.mpg_data import Mpg_Data
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import datetime
from dateutil.relativedelta import relativedelta
from mpg.mpg_user import Mpg_User

class Mpg_Geraete():
    def __init__(self, ui):
        self.ui = ui
        self.data = Mpg_Data()
        self.standort_combo_fuellen()
        self.geraete_tabelle_fuellen()
        self.geraete_inventarnummer_combos_fuellen()
        self.verwertet_tabelle_fuellen()
        self.einweisung_geraete_combos_fuellen()
        self.einweisung_tabelle_fuellen()
        self.combos_ma_fuellen()
        self.tabellen_filter_ma_combo_fuellen()
        self.ui.einweisung_tabelle_filtern_ma_combo.currentTextChanged.connect \
            (self.tabelle_nach_ma_filtern)
        self.ui.geraete_verwalten_aenderung_speichern_btn.clicked.connect(self.geraet_update)
        self.ui.verwertet_speichern_button.clicked.connect(self.geraet_verwerten)
        self.ui.geraete_verwalten_speichern_button.clicked.connect(self.neues_geraet_anlegen)
        self.ui.einweisung_speichern_btn.clicked.connect(self.geraete_einweisung)
        self.ui.einweisung_standardwerte_loeschen_btn.clicked.connect(self.standard_werte_loeschen)
        self.ui.einweisung_tabelle_filtern_geraet_combo.currentTextChanged.connect(
            self.einweisung_tabelle_filtern_geraet_auswahl)
        self.ui.einweisung_tabelle_filtern_software_combo.currentTextChanged.connect(
            self.einweisung_tabelle_filtern_nach_software)
        self.ui.mpg_standort_speichern_btn.clicked.connect(self.mpg_standort_hinzufuegen)
        self.standorte_tabelle_fuellen()
        self.standort_loeschen_combo_fuellen()
        self.ui.mpg_standorte_loeschen_btn.clicked.connect(self.standort_loeschen)

    # combos und tabellen fuellen

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

    def standort_combo_fuellen(self):
        self.ui.geraete_verwalten_standort_combo.clear()
        alle_fahrzeuge = self.data.fahrzeuge_abfragen()
        liste_der_eintraege = ["---"]
        for element in range(0, len(alle_fahrzeuge)):
            liste_der_eintraege.append(alle_fahrzeuge[element][2])

        standorte = self.data.standorte_abfragen()
        for element in range(0, len(standorte)):
            liste_der_eintraege.append(standorte[element][0])
        self.ui.geraete_verwalten_standort_combo.addItems(liste_der_eintraege)

    def geraete_tabelle_fuellen(self):
        self.ui.mpg_geraete_tabelle.setRowCount(0)
        geraete = self.data.geraete_abfragen()

        for element in range(0, len(geraete)):
            count = 0
            feld = 0
            rows = self.ui.mpg_geraete_tabelle.rowCount()
            self.ui.mpg_geraete_tabelle.insertRow(rows)
            for eigenschaft in range(0, len(geraete[element])):
                if count == 8:
                    einzusetzen = QtWidgets.QTableWidgetItem(str(geraete[element][eigenschaft]))
                    einzusetzen.setTextAlignment(Qt.AlignCenter)
                    self.ui.mpg_geraete_tabelle.setItem(rows, feld, QtWidgets.QTableWidgetItem(
                        einzusetzen))

                    feld += 1
                    pruefdatum_splitted = geraete[element][7].split(".")
                    datum = datetime.date(int(pruefdatum_splitted[2]), int(pruefdatum_splitted[1]),
                                          int(pruefdatum_splitted[0]))
                    naechste_pruefung = datum + relativedelta(months=int(geraete[element][eigenschaft]))
                    naechste_pruefung = str(naechste_pruefung.strftime("%d.%m.%Y"))
                    einzusetzen = QtWidgets.QTableWidgetItem(naechste_pruefung)
                    einzusetzen.setTextAlignment(Qt.AlignCenter)
                    self.ui.mpg_geraete_tabelle.setItem(rows, feld, QtWidgets.QTableWidgetItem(
                        einzusetzen))
                    count += 1
                    feld += 1
                else:
                    einzusetzen = QtWidgets.QTableWidgetItem(str(geraete[element][eigenschaft]))
                    einzusetzen.setTextAlignment(Qt.AlignCenter)
                    self.ui.mpg_geraete_tabelle.setItem(rows, feld, QtWidgets.QTableWidgetItem(
                        einzusetzen))
                    feld += 1
                    count += 1
        self.ui.mpg_geraete_tabelle.horizontalHeader().setSectionResizeMode(1)

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

    def geraete_inventarnummer_combos_fuellen(self):
        self.ui.verwertet_geraete_combo.clear()
        geraete = self.data.geraete_abfragen()
        liste_der_eintraege = ["---"]
        for element in range(0, len(geraete)):
            liste_der_eintraege.append(geraete[element][1] + " / " + geraete[element][2])
        self.ui.verwertet_geraete_combo.addItems(liste_der_eintraege)


    def einweisung_tabelle_fuellen(self):
        self.ui.einweisung_tabelle.setRowCount(0)
        einweisungen = self.data.einweisungen_abfragen()
        for element in range(0, len(einweisungen)):
            count = 0
            rows = self.ui.einweisung_tabelle.rowCount()
            self.ui.einweisung_tabelle.insertRow(rows)
            for eigenschaft in range(1, len(einweisungen[element])):
                einzusetzen = QtWidgets.QTableWidgetItem(einweisungen[element][eigenschaft])
                einzusetzen.setTextAlignment(Qt.AlignCenter)
                self.ui.einweisung_tabelle.setItem(rows, count, QtWidgets.QTableWidgetItem(einzusetzen))
                count += 1
        self.ui.einweisung_tabelle.horizontalHeader().setSectionResizeMode(1)

    def verwertet_tabelle_fuellen(self):
        self.ui.verwertet_tabelle.setRowCount(0)
        verwertete_geraete = self.data.verwertete_geraete_abfragen()
        for element in range(0, len(verwertete_geraete)):
            count = 0
            rows = self.ui.verwertet_tabelle.rowCount()
            self.ui.verwertet_tabelle.insertRow(rows)
            for eigenschaft in range(1, len(verwertete_geraete[element])):
                einzusetzen = QtWidgets.QTableWidgetItem(verwertete_geraete[element][eigenschaft])
                einzusetzen.setTextAlignment(Qt.AlignCenter)
                self.ui.verwertet_tabelle.setItem(rows, count, QtWidgets.QTableWidgetItem(einzusetzen))
                count += 1
        self.ui.verwertet_tabelle.horizontalHeader().setSectionResizeMode(1)

    def update_tabellen_und_combos(self):
        self.einweisung_geraete_combos_fuellen()
        self.geraete_inventarnummer_combos_fuellen()
        self.verwertet_tabelle_fuellen()
        self.geraete_tabelle_fuellen()

    # combos und tabellen fuellen ende

    def tabelle_nach_ma_filtern(self):
        
        self.ui.einweisung_tabelle.setRowCount(0)
        ma = self.ui.einweisung_tabelle_filtern_ma_combo.currentText()
        daten = self.data.einweisungs_daten_gefiltert_ma(ma)
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

        if ma == "---":
           self.einweisung_tabelle_fuellen()

    def geraet_update(self):
        rows = self.ui.mpg_geraete_tabelle.rowCount()

        for reihe in range(0, rows):
            id = self.ui.mpg_geraete_tabelle.item(reihe, 0).text()
            geraet = self.ui.mpg_geraete_tabelle.item(reihe, 1).text()
            seriennummer = self.ui.mpg_geraete_tabelle.item(reihe, 2).text()
            inventarnummer = self.ui.mpg_geraete_tabelle.item(reihe, 3).text()
            ce = self.ui.mpg_geraete_tabelle.item(reihe, 4).text()
            bemerkung = self.ui.mpg_geraete_tabelle.item(reihe, 5).text()
            anschaffung = self.ui.mpg_geraete_tabelle.item(reihe, 6).text()
            pruefdatum = self.ui.mpg_geraete_tabelle.item(reihe, 7).text()
            pruefung = self.datum_pruefen(pruefdatum)
            if pruefung == 1:
                naechste_pruefung = self.ui.mpg_geraete_tabelle.item(reihe, 8).text()
                standort = self.ui.mpg_geraete_tabelle.item(reihe, 10).text()
                artikelnr = self.ui.mpg_geraete_tabelle.item(reihe, 11).text()
                self.data.geraet_updaten(geraet, seriennummer, inventarnummer, ce, bemerkung, anschaffung, pruefdatum
                                         , naechste_pruefung, standort, artikelnr, id)
            else:
                pass
        self.update_tabellen_und_combos()
        Mpg_User(self.ui).update()

    def neues_geraet_anlegen(self):
        geraet = self.ui.geraete_verwalten_geraet.text()
        geraetenummer = self.ui.geraete_verwalten_geraetenummer.text()
        inventarnummer = self.ui.geraete_verwalten_inventarnummer.text()
        ce = self.ui.geraete_verwalten_ce.text()
        bemerkung = self.ui.geraete_verwalten_bemerkung.text()
        anschaffung = self.ui.geraete_verwalten_anschaffung.text()
        pruefdatum = self.ui.geraete_verwalten_pruefdatum.text()
        pruefung = self.datum_pruefen(pruefdatum)
        artikelnr = self.ui.geraete_verwalten_artikelnr.text()
        if pruefung == 1:
            prueffrist = self.ui.geraete_verwalten_prueffrist.text()
            try:
                int(prueffrist)
                standort = self.ui.geraete_verwalten_standort_combo.currentText()

                self.data.neues_geraet_speichern(geraet, geraetenummer, inventarnummer, ce,
                                                 bemerkung, anschaffung, pruefdatum, prueffrist, standort, artikelnr)
                self.update_tabellen_und_combos()
                self.geraete_verwalten_felder_leeren()
                Mpg_User(self.ui).update()
            except ValueError:
                pass # error label einfügen das anzeigt das monate nicht korrekt angegeben ist.
        else:
            pass # error label einfügen was falsches datum auswirft

    def geraete_verwalten_felder_leeren(self):
        self.ui.geraete_verwalten_geraet.setText("")
        self.ui.geraete_verwalten_geraetenummer.setText("")
        self.ui.geraete_verwalten_inventarnummer.setText("")
        self.ui.geraete_verwalten_ce.setText("")
        self.ui.geraete_verwalten_bemerkung.setText("")
        self.ui.geraete_verwalten_pruefdatum.setText("")
        self.ui.geraete_verwalten_prueffrist.setText("")
        self.ui.geraete_verwalten_pruefdatum.setText("")
        self.ui.geraete_verwalten_anschaffung.setText("")
        self.ui.geraete_verwalten_standort_combo.setCurrentIndex(0)

    def geraet_verwerten(self):
        geraet = self.ui.verwertet_geraete_combo.currentText()
        datum = self.ui.verwertet_datum.text()
        geraetenummer = str(geraet).split("/ ")[1]
        bemerkung = self.ui.verwertet_bemerkung.text()
        self.data.geraet_verwerten(geraet, datum, geraetenummer, bemerkung)
        rows = self.ui.verwertet_tabelle.rowCount()
        self.ui.verwertet_tabelle.insertRow(rows)
        self.update_tabellen_und_combos()
        Mpg_User(self.ui).update()
        self.ui.verwertet_geraete_combo.setCurrentIndex(0)
        self.ui.verwertet_datum.setText("")
        self.ui.verwertet_bemerkung.setText("")

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

        self.data.einweisung_speichern(geraet, softwareversion, datum, eingewiesener, einweisender,
                                       original)
        rows = self.ui.einweisung_tabelle.rowCount()
        self.ui.einweisung_tabelle.insertRow(rows)
        liste_der_eintraege = [geraet, softwareversion, datum, eingewiesener, einweisender, original]
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

    def standard_werte_loeschen(self):
        self.ui.einweisung_geraete_combo_standard.setCurrentIndex(0)
        self.ui.einweisung_softwareversion_standard.setText("")
        self.ui.einweisung_datum_standard.setText("")
        self.ui.einweisung_ma_standard_combo.setCurrentIndex(0)
        self.ui.einweisung_einweisender_standard.setText("")
        self.ui.einweisung_original_standard.setText("")

    def einweisung_tabelle_filtern_geraet_auswahl(self):
        auswahl = self.ui.einweisung_tabelle_filtern_geraet_combo.currentText()
        if auswahl == "---":
            self.tabelle_filtern_software_combo_fuellen()
            self.einweisung_tabelle_fuellen()
        else:
            self.ui.einweisung_tabelle_filtern_ma_combo.setCurrentIndex(0)
            self.tabelle_filtern_software_combo_fuellen()
            self.einweisung_tabelle_filtern_geraet_anzeigen()

    def einweisung_tabelle_filtern_geraet_anzeigen(self):
        self.ui.einweisung_tabelle.setRowCount(0)
        geraet = self.ui.einweisung_tabelle_filtern_geraet_combo.currentText()
        daten = self.data.einweisungs_daten_gefiltert_geraet(geraet)
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
        self.ui.einweisung_tabelle_filtern_anzahl.setText("<html><head/><body><p><span style=\" "
                                                          "color:#ffffff;\">"+ str(eintraege) +
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


    def datum_pruefen(self, datum):
        liste_der_daten = datum.split(".")
        wert = 1
        try:
            datetime.date(year=int(liste_der_daten[2]), month=int(liste_der_daten[1]),
                              day=int(liste_der_daten[0]))
        except ValueError:
            wert = 0
        return wert

    def standorte_tabelle_fuellen(self):
        self.ui.mpg_standorte_tabelle.setRowCount(0)
        standorte = self.data.standorte_abfragen()
        for element in range(0, len(standorte)):
            rows = self.ui.mpg_standorte_tabelle.rowCount()
            self.ui.mpg_standorte_tabelle.insertRow(rows)
            einzusetzen = QtWidgets.QTableWidgetItem(standorte[element][0])
            einzusetzen.setTextAlignment(Qt.AlignCenter)
            self.ui.mpg_standorte_tabelle.setItem(rows, 0, QtWidgets.QTableWidgetItem(einzusetzen))

        self.ui.mpg_standorte_tabelle.horizontalHeader().setSectionResizeMode(1)

    def mpg_standort_hinzufuegen(self):
        name = self.ui.mpg_standort_text.text()
        self.data.neuen_standort_anlegen(name)
        self.standorte_tabelle_fuellen()
        self.standort_loeschen_combo_fuellen()
        self.standort_combo_fuellen()
        self.ui.mpg_standort_text.setText("")
        Mpg_User(self.ui).update()

    def standort_loeschen_combo_fuellen(self):
        self.ui.mpg_standorte_combo.clear()
        standorte = self.data.standorte_abfragen()
        liste_der_eintraege = ["---"]
        for element in range(0, len(standorte)):
            liste_der_eintraege.append(standorte[element][0])
        self.ui.mpg_standorte_combo.addItems(liste_der_eintraege)

    def standort_loeschen(self):
        name = self.ui.mpg_standorte_combo.currentText()
        self.data.standort_loeschen(name)
        self.standorte_tabelle_fuellen()
        self.standort_loeschen_combo_fuellen()
        self.standort_combo_fuellen()
        Mpg_User(self.ui).update()



