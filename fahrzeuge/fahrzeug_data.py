import sqlite3
from uebersicht.uebersicht_fahrzeuge_anzeige import Fahrzeug_Anzeige

class Data_Fahrzeug():
    def __init__(self):
        self.conn = sqlite3.connect("Database.db")
        self.c = self.conn.cursor()
        self.fahrzeuge = Fahrzeug_Anzeige

    def __del__(self):
        self.conn.close()  # zum freigeben der Datenbank

    def daten_combo_fahrzeug_mitarbeiter(self):
        sql = "SELECT kennzeichen from fahrzeug_aktiv"
        self.c.execute(sql)
        return self.c.fetchall()

    def fahrzeug_zustand_aendern_sql(self, fahrzeug, zustand, bemerkung):
        params = (zustand, bemerkung, fahrzeug)
        sql = "UPDATE fahrzeug_aktiv SET zustand = ?, bemerkung = ?  WHERE kennzeichen = ?"
        self.c.execute(sql, params)
        self.conn.commit()

    def daten_combo_status_rtw(self, kennzeichen):
        params = (kennzeichen, )
        sql = ("SELECT zustand FROM fahrzeug_aktiv WHERE kennzeichen = ?")
        self.c.execute(sql, params)
        return self.c.fetchall()

    def fahrzeug_daten_holen(self):
        sql = "SELECT * FROM fahrzeug_aktiv"
        self.c.execute(sql)
        return self.c.fetchall()
