
from uebersicht.uebersicht_fahrzeuge_anzeige import Fahrzeug_Anzeige
import sqlite3

class Fahrzeuge_Uebersicht():
    def __init__(self, ui):
        self.ui = ui
        self.conn = sqlite3.connect("Database.db")
        self.c = self.conn.cursor()


    def __del__(self):
        self.conn.close()  # zum freigeben der Datenbank


    def anzeige(self):
        liste = self.daten_holen()
        fahrzeug_objekte = {}
        counter = 0
        for i in range(0, len(liste)):

            kennung = liste[i][1]
            kennzeichen = liste[i][2]
            ort = liste[i][3]
            status = liste[i][4]
            bemerkung = liste[i][6]
            fahrzeug_objekte[kennzeichen] = Fahrzeug_Anzeige(self.ui).anzeige(kennung, kennzeichen, ort, status, bemerkung, counter)
            counter += 1

        return fahrzeug_objekte
        liste = []

    def daten_holen(self):
        sql = "SELECT * FROM fahrzeug_aktiv"
        self.c.execute(sql)
        return self.c.fetchall()


