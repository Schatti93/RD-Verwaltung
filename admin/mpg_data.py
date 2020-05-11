import sqlite3

class Mpg_Data():
    def __init__(self):
        self.conn = sqlite3.connect("Database.db")
        self.c = self.conn.cursor()

    def neues_geraet_speichern(self, geraet, geraetenummer, inventarnummmer, ce, bemerkung, pruefdatum, prueffrist, standort):
        params = (geraet, geraetenummer, inventarnummmer, ce, bemerkung, pruefdatum, prueffrist, standort)
        sql = "INSERT INTO mpg_geraete VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)"
        self.c.execute(sql, params)
        self.conn.commit()

