import sqlite3

class Missions_Data():
    def __init__(self):
        self.conn = sqlite3.connect("Database.db")
        self.c = self.conn.cursor()

    def get_material(self, miossion_numer):
        params = (miossion_numer, )
        sql = "SELECT produkt, menge, datum FROM lager_nachweis WHERE Einsatznummer = ?"
        self.c.execute(sql, params)
        return self.c.fetchall()