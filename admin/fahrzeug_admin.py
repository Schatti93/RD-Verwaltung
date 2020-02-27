import sqlite3
from uebersicht.uebersicht_fahrzeuge_anzeige import Fahrzeug_Anzeige


class Admin_Fahrzeug():
    def __init__(self, ui):
        self.ui = ui
        self.ui.fahrzeug_admin_save_btn.clicked.connect(self.auslesen)
        self.conn = sqlite3.connect("Database.db")
        self.c = self.conn.cursor()


    def neues_fahrzeug(self, funk, kennzeichen, ort, tuev):
        liste_status = ["Im Dienst", "Außer Dienst", "Nicht Einsatzbereit"]
        for i in range(0, len(liste_status)):
            params = (funk, kennzeichen, ort, liste_status[i], tuev, "" )
            sql = "INSERT INTO fahrzeug_zustaende VALUES (NULL, ?, ?, ?, ?, ?, ?)"
            self.c.execute(sql, params)
            self.conn.commit()
        params = (funk, kennzeichen, ort, liste_status[0], tuev, "")
        sql = "INSERT INTO fahrzeug_aktiv VALUES (NULL, ?, ?, ?, ?, ?, ?)"
        self.c.execute(sql, params)
        self.conn.commit()
        Fahrzeug_Anzeige(self.ui).anzeige(funk, kennzeichen, ort, liste_status[0], "")
        self.ui.fahrzeug_admin_error_label.setText("<html><head/><body><p><span style=\" color:#00FF00;\">Eingabe Gespeichert</span></p></body></html>")

    def auslesen(self):
        funk = self.ui.fahrzeug_admin_funkkenn.text()
        kennzeichen = self.ui.fahrzeug_admin_kennz.text()
        ort = self.ui.fahrzeug_admin_ort.text()
        tuev = self.ui.fahrzeug_admin_tuev.text()
        self.neues_fahrzeug(funk, kennzeichen, ort, tuev)

