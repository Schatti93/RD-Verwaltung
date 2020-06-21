from admin.mpg.mpg_data import Mpg_Data
import datetime
from mpg.mpg_user import Mpg_User
from admin.mpg.update_mpg import Update_Mpg
from error_message_boxes import Error_Message_Boxes


class Geraete():
    def __init__(self, ui):
        self.ui = ui
        self.error = Error_Message_Boxes()
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
                self.error.message_box_only_ok("In der Reihe mit der id: " + id + " ist das Prüfdatum falsch angegeben.",
                                               "Falsches Datum")
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

            int(prueffrist)
            standort = self.ui.geraete_verwalten_standort_combo.currentText()

            self.data.neues_geraet_speichern(geraet, geraetenummer, inventarnummer, ce,
                                             bemerkung, anschaffung, pruefdatum, prueffrist, standort, artikelnr)
            Update_Mpg(self.ui).update_tabellen_und_combos()
            self.geraete_verwalten_felder_leeren()
            Mpg_User(self.ui).update()
        else:
            self.error.message_box_only_ok("Das Datum wurde Falsch angegeben. TT.MM.JJJJ",
                                           "Falsches Datum")

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

