import sqlite3

class Mpg_User_Data():
    def __init__(self):
        self.conn = sqlite3.connect("mpg.db")
        self.c = self.conn.cursor()
        self.conn_data = sqlite3.connect("Database.db")
        self.c_data = self.conn_data.cursor()

    def standorte_abfragen(self):
        sql = "SELECT standort from mpg_geraete"
        self.c.execute(sql)
        return self.c.fetchall()

    def geraete_auf_standort_abfragen(self, standort):
        params = (standort, )
        sql = "SELECT geraet, geraetenummer, inventarnummer FROM mpg_geraete WHERE standort = ?"
        self.c.execute(sql, params)
        return self.c.fetchall()

    def fahrzeuge_abfragen(self):
        sql = "SELECT kennzeichen FROM fahrzeug_aktiv"
        self.c_data.execute(sql)
        return self.c_data.fetchall()

    def standort_von_geraet_abfragen(self, inventarnummer):
        params = (inventarnummer, )
        sql = "SELECT standort FROM mpg_geraete WHERE inventarnummer = ?"
        self.c.execute(sql, params)
        return self.c.fetchall()

    def update_standort_von_geraet(self, standort, inventarnummer, neue_bemerkung):
        params = (standort, neue_bemerkung, inventarnummer)
        sql = "UPDATE mpg_geraete SET standort = ?, bemerkung = ? WHERE inventarnummer = ?"
        self.c.execute(sql, params)
        self.conn.commit()

    def wachen_abfragen(self):
        sql = "SELECT standort FROM standorte"
        self.c.execute(sql)
        return self.c.fetchall()

    def bemerkung_abfragen(self, inventarnummer):
        params = (inventarnummer, )
        sql = "SELECT bemerkung FROM mpg_geraete WHERE inventarnummer = ?"
        self.c.execute(sql, params)
        return self.c.fetchall()