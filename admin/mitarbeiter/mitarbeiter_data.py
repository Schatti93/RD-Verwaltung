import sqlite3

class Mitarbeiter_Data():
    def __init__(self):
        self.conn = sqlite3.connect("mitarbeiter.db")
        self.c = self.conn.cursor()

    def neuer_mitarbeiter_speichern(self, vorname, nachname):
        params = (vorname, nachname)
        sql = "INSERT INTO mitarbeiter VALUES (NULL, ?, ?)"
        self.c.execute(sql, params)
        self.conn.commit()

    def alle_ma_abfragen(self):
        sql = "SELECT * FROM mitarbeiter"
        self.c.execute(sql)
        return self.c.fetchall()

    def ma_loeschen(self, ma_id):
        params = (ma_id, )
        sql = "DELETE FROM mitarbeiter WHERE id = ?"
        self.c.execute(sql, params)
        self.conn.commit()