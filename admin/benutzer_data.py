import sqlite3

class Benutzer_Data():
    def __init__(self):
        self.conn = sqlite3.connect("Database.db")
        self.c = self.conn.cursor()

    def benutzerdaten_abfragen(self, benutzer):
        params = (benutzer, )
        sql = "SELECT * FROM admin WHERE benutzer = ?"
        self.c.execute(sql, params)
        return self.c.fetchall()

    def passwort_update(self, benutzer, passwort):
        params = (passwort, benutzer)
        sql = "UPDATE admin SET passwort = ? WHERE benutzer = ?"
        self.c.execute(sql, params)
        self.conn.commit()

    def neuer_benutzer(self, benutzer, passwort):
        params = (benutzer, passwort)
        sql = "INSERT INTO admin VALUES (NULL, ?, ?)"
        self.c.execute(sql, params)
        self.conn.commit()

    def alle_benutzer_abfragen(self):
        sql = "SELECT * FROM admin"
        self.c.execute(sql)
        return self.c.fetchall()
