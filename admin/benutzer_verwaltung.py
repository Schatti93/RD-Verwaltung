from admin.benutzer_data import Benutzer_Data
import hashlib

class Benutzer_Verwaltung():
    def __init__(self, ui):
        self.ui = ui
        self.data = Benutzer_Data()

    def benuter_passwort_aendern(self):
        benutzer = ""
        passwort = ""
        passwort_hash = hashlib.sha1(passwort.encode('utf-8')).hexdigest()
        benutzer_daten = self.data.benutzerdaten_abfragen()
        neues_passwort = ""
        neues_passwort_vergleich = ""

        if passwort_hash == benutzer_daten[0][2]:
            if neues_passwort == neues_passwort_vergleich:
                self.data.passwort_update(benutzer, passwort)


    def neuer_benutzer(self):
        benutzer = ""
        passwort = ""
        passwort_vergleich = ""
        count = 0
        alle_benutzer = self.data.alle_benutzer_abfragen()
        for i in alle_benutzer[0]:
            if i[1] == benutzer:
                count += 1

        if count == 0:
            if passwort == passwort_vergleich:
                passwort_hash = hashlib.sha1(passwort.encode('utf-8')).hexdigest()
                self.data.neuer_benutzer(benutzer, passwort_hash)
        else:
            print("hier muss das error label benutzer schon vorhanden anzeigen")

    def benutzer_loeschen(self):
        benutzer = ""
        