import sqlite3

class Mpg_Data():
    def __init__(self):
        self.conn = sqlite3.connect("Database.db")
        self.c = self.conn.cursor()

    def neues_geraet_speichern(self, geraet, geraetenummer, inventarnummmer, ce,
                               bemerkung, pruefdatum, prueffrist, standort):
        params = (geraet, geraetenummer, inventarnummmer, ce, bemerkung, pruefdatum,
                  prueffrist, standort)
        sql = "INSERT INTO mpg_geraete VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)"
        self.c.execute(sql, params)
        self.conn.commit()

    def standorte_abfragen(self):
        sql = "SELECT * FROM fahrzeug_aktiv"
        self.c.execute(sql)
        return self.c.fetchall()

    def geraete_abfragen(self):
        sql = "SELECT * FROM mpg_geraete"
        self.c.execute(sql)
        return self.c.fetchall()

    def geraet_verwerten(self, geraet, datum, geraetenummer):
        params = (geraet, datum)
        sql = "INSERT INTO mpg_verwertet VALUES (NULL, ?, ?)"
        self.c.execute(sql, params)
        params = (geraetenummer, )
        sql = "DELETE FROM mpg_geraete WHERE geraetenummer = ?"
        self.c.execute(sql, params)
        self.conn.commit()

    def verwertete_geraete_abfragen(self):
        sql = "SELECT * FROM mpg_verwertet"
        self.c.execute(sql)
        return self.c.fetchall()

    def einweisung_speichern(self, geraet, softwareversion, datum, eingewiesener, einweisender, original):
        params = (geraet, softwareversion, datum, eingewiesener, einweisender, original)
        sql = "INSERT INTO mpg_einweisungen VALUES (NULL, ?, ?, ?, ?, ?, ?)"
        self.c.execute(sql, params)
        self.conn.commit()

    def einweisungen_abfragen(self):
        sql = "SELECT * FROM mpg_einweisungen"
        self.c.execute(sql)
        return self.c.fetchall()

    def ein_geraet_abfragen(self, geraetenummer):
        params = (geraetenummer, )
        sql = "SELECT * FROM mpg_geraete WHERE geraetenummer = ?"
        self.c.execute(sql, params)
        return self.c.fetchall()

    def geraet_updaten(self, geraet, geraetenummer, inventarnummmer, ce,
                               bemerkung, pruefdatum, prueffrist, standort, id):
        params = (geraet, inventarnummmer, ce, bemerkung, pruefdatum,
                  prueffrist, standort, geraetenummer, id)
        sql = "UPDATE mpg_geraete SET geraet = ?, inventarnummer = ?, ce = ?, bemerkung = ?, pruefdatum = ?, prueffrist = ?" \
              ", standort = ?, geraetenummer = ? WHERE id = ?"
        self.c.execute(sql, params)
        self.conn.commit()

    def geraete_id_abfragen(self, geraetenummer):
        params = (geraetenummer, )
        sql = "SELECT id FROM mpg_geraete WHERE geraetenummer = ?"
        self.c.execute(sql, params)
        return self.c.fetchall()

    def softwareversion_abfragen(self, geraet):
        params = (geraet, )
        sql = "SELECT softwareversion FROM mpg_einweisungen WHERE geraet = ?"
        self.c.execute(sql, params)
        return self.c.fetchall()

    def einweisungs_daten_gefiltert_geraet(self, geraet):
        params = (geraet, )
        sql = "SELECT * FROM mpg_einweisungen WHERE geraet = ?"
        self.c.execute(sql, params)
        return self.c.fetchall()

    def einweisungs_daten_gefiltert_software(self, geraet, software):
        params = (geraet, software)
        sql = "SELECT * FROM mpg_einweisungen WHERE geraet = ? AND softwareversion = ?"
        self.c.execute(sql, params)
        return self.c.fetchall()
