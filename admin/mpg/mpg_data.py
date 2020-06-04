import sqlite3

class Mpg_Data():
    def __init__(self):
        self.conn = sqlite3.connect("mpg.db")
        self.c = self.conn.cursor()
        self.conn_data = sqlite3.connect("Database.db")
        self.c_data = self.conn_data.cursor()
        self.conn_ma = sqlite3.connect("mitarbeiter.db")
        self.c_ma = self.conn_ma.cursor()

    def neues_geraet_speichern(self, geraet, geraetenummer, inventarnummmer, ce,
                               bemerkung, anschaffung, pruefdatum, prueffrist, standort, artikelnr):
        params = (geraet, geraetenummer, inventarnummmer, ce, bemerkung, anschaffung, pruefdatum,
                  prueffrist, standort, artikelnr)
        sql = "INSERT INTO mpg_geraete VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        self.c.execute(sql, params)
        self.conn.commit()

    def mitarbeiter_abfragen(self):
        sql = "SELECT * FROM mitarbeiter"
        self.c_ma.execute(sql)
        return self.c_ma.fetchall()

    def mitarbeiter_status_abfragen(self, nachname, vorname):
        params = (nachname, vorname)
        sql = "SELECT status from mitarbeiter WHERE nachname = ? AND vorname = ?"
        self.c_ma.execute(sql, params)
        return self.c_ma.fetchall()

    def fahrzeuge_abfragen(self):
        sql = "SELECT * FROM fahrzeug_aktiv"
        self.c_data.execute(sql)
        return self.c_data.fetchall()

    def geraete_abfragen(self):
        sql = "SELECT * FROM mpg_geraete"
        self.c.execute(sql)
        return self.c.fetchall()

    def geraet_verwerten(self, geraet, datum, geraetenummer, bemerkung):
        params = (geraet, datum, bemerkung)
        sql = "INSERT INTO mpg_verwertet VALUES (NULL, ?, ?, ?)"
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
                               bemerkung, anschaffung, pruefdatum, prueffrist, standort, artikelnr, id):
        params = (geraet, inventarnummmer, ce, bemerkung, pruefdatum,
                  prueffrist, standort, geraetenummer, artikelnr, id)
        sql = "UPDATE mpg_geraete SET geraet = ?, inventarnummer = ?, ce = ?, bemerkung = ?, pruefdatum = ?, prueffrist = ?" \
              ", standort = ?, geraetenummer = ?, artikelnr = ? WHERE id = ?"
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

    def einweisung_checken(self, ma, geraet):
        params = (ma, geraet)
        sql = "SELECT softwareversion from mpg_einweisungen WHERE eingewiesener = ? and geraet = ?"
        self.c.execute(sql, params)
        return self.c.fetchall()

    def einweisungs_daten_gefiltert_ma(self, ma):
        params = (ma, )
        sql = "SELECT * FROM mpg_einweisungen WHERE eingewiesener = ?"
        self.c.execute(sql, params)
        return self.c.fetchall()

    def einweisungs_daten_gefiltert_software(self, geraet, software):
        params = (geraet, software)
        sql = "SELECT * FROM mpg_einweisungen WHERE geraet = ? AND softwareversion = ?"
        self.c.execute(sql, params)
        return self.c.fetchall()

    def neuen_standort_anlegen(self, name):
        params = (name, )
        sql = "INSERT INTO standorte VALUES (NULL, ?)"
        self.c.execute(sql, params)
        self.conn.commit()

    def standorte_abfragen(self):
        sql = "SELECT standort FROM standorte"
        self.c.execute(sql)
        return self.c.fetchall()

    def standort_loeschen(self, name):
        params = (name, )
        sql = "DELETE FROM standorte WHERE standort = ?"
        self.c.execute(sql, params)
        self.conn.commit()

    def einweisung_updaten(self, geraet, softwareversion, datum, eingewiesener, einweisender, original):
        params = (softwareversion, datum, einweisender, original, geraet, eingewiesener)
        sql = "UPDATE mpg_einweisungen SET softwareversion = ?, datum = ?, einweisender = ?," \
        "original = ? WHERE geraet = ? and eingewiesener = ?"
        self.c.execute(sql, params)
        self.conn.commit()

    def softwareversion_check(self, geraet):
        params = (geraet, )
        sql = "SELECT softwareversion, datum FROM mpg_einweisungen WHERE geraet = ?"
        self.c.execute(sql, params)
        return self.c.fetchall()



