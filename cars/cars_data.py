import sqlite3
from overview.uebersicht_fahrzeuge_anzeige import Fahrzeug_Anzeige

class Cars_Data():
    def __init__(self):
        self.conn = sqlite3.connect("Database.db")
        self.c = self.conn.cursor()
        self.fahrzeuge = Fahrzeug_Anzeige

    def __del__(self):
        self.conn.close()  # zum freigeben der Datenbank

    def datas_for_combobox_cars(self):
        sql = "SELECT kennzeichen from fahrzeug_aktiv"
        self.c.execute(sql)
        return self.c.fetchall()

    def change_car_status(self, fahrzeug, zustand, bemerkung):
        params = (zustand, bemerkung, fahrzeug)
        sql = "UPDATE fahrzeug_aktiv SET zustand = ?, bemerkung = ?  WHERE kennzeichen = ?"
        self.c.execute(sql, params)
        self.conn.commit()

    def data_combobox_status(self, kennzeichen):
        params = (kennzeichen, )
        sql = ("SELECT zustand FROM fahrzeug_aktiv WHERE kennzeichen = ?")
        self.c.execute(sql, params)
        return self.c.fetchall()

    def get_cars(self):
        sql = "SELECT * FROM fahrzeug_aktiv"
        self.c.execute(sql)
        return self.c.fetchall()
