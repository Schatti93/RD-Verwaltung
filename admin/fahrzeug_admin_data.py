import sqlite3

class Fahrzeug_Admin_Data():
    def __init__(self):
        self.conn = sqlite3.connect("Database.db")
        self.c = self.conn.cursor()

    def fahrzeug_hinzufuegen(self, funk, kennzeichen, ort, zustand, tuev, bemerkung):
        params = (funk, kennzeichen, ort, zustand, tuev, bemerkung )
        sql = "INSERT INTO fahrzeug_zustaende VALUES (NULL, ?, ?, ?, ?, ?, ?)"
        self.c.execute(sql, params)
        self.conn.commit()

    def aktives_fahrzeug(self,funk, kennzeichen, ort, zustand, tuev, bemerkung):
        params = (funk, kennzeichen, ort, zustand, tuev, bemerkung)
        sql = "INSERT INTO fahrzeug_aktiv VALUES (NULL, ?, ?, ?, ?, ?, ?)"
        self.c.execute(sql, params)
        self.conn.commit()

    def aktive_fahrzeuge_abfragen(self):
        sql = "SELECT * FROM fahrzeug_aktiv"
        self.c.execute(sql)
        return self.c.fetchall()