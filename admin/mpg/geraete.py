from admin.mpg.mpg_data import Mpg_Data
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from dateutil.relativedelta import relativedelta
import datetime
from datetime import date
from mpg.mpg_user import Mpg_User
from admin.mpg.update_mpg import Update_Mpg
from PyQt5 import QtCore
from PyQt5 import QtGui

class Geraete():
    def __init__(self, ui):
        self.ui = ui
        self.data = Mpg_Data()
        self.ui.geraete_verwalten_aenderung_speichern_btn.clicked.connect \
            (self.geraet_update)
        self.ui.geraete_verwalten_speichern_button.clicked.connect \
            (self.neues_geraet_anlegen)

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
                    einzusetzen = QtWidgets.QTableWidgetItem()
                    einzusetzen.setTextAlignment(Qt.AlignCenter)
                    einzusetzen.setData(QtCore.Qt.EditRole, geraete[element][eigenschaft])
                    self.ui.mpg_geraete_tabelle.setItem(rows, feld, einzusetzen)

                    feld += 1
                    pruefdatum_splitted = geraete[element][7].split(".")
                    datum = datetime.date(int(pruefdatum_splitted[2]), int(pruefdatum_splitted[1]),
                                          int(pruefdatum_splitted[0]))
                    naechste_pruefung = datum + relativedelta(months=int(geraete[element]
                                                                         [eigenschaft]))
                    today = date.today()
                    kritisch = naechste_pruefung - today

                    naechste_pruefung = str(naechste_pruefung.strftime("%d.%m.%Y"))

                    entry = QtWidgets.QTableWidgetItem(naechste_pruefung)
                    # TODO That fucking table does not show the foreground color!
                    if int(kritisch.days) <= 60:
                        print("geht rein")
                        entry.setForeground(QtGui.QColor(255, 0, 0))
                    entry.setTextAlignment(Qt.AlignCenter)

                    self.ui.mpg_geraete_tabelle.setItem(rows, feld, entry)
                    count += 1
                    feld += 1
                else:
                    einzusetzen = QtWidgets.QTableWidgetItem(str(geraete[element][eigenschaft]))
                    einzusetzen.setTextAlignment(Qt.AlignCenter)
                    if eigenschaft == 0:
                        einzusetzen.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.ui.mpg_geraete_tabelle.setItem(rows, feld, einzusetzen)
                    feld += 1
                    count += 1
        self.ui.mpg_geraete_tabelle.horizontalHeader().setSectionResizeMode(1)

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
        Update_Mpg(self.ui).update_tabellen_und_combos()
        Mpg_User(self.ui).update()

    def datum_pruefen(self, datum):
        liste_der_daten = datum.split(".")
        wert = 1
        try:
            datetime.date(year=int(liste_der_daten[2]), month=int(liste_der_daten[1]),
                              day=int(liste_der_daten[0]))
        except ValueError:
            wert = 0
        return wert

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
                Update_Mpg(self.ui).update_tabellen_und_combos()
                self.geraete_verwalten_felder_leeren()
                Mpg_User(self.ui).update()
            except ValueError:
                # TODO was da unten steht -.- todo funktion zuspät entdeckt
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

