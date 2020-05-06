import sqlite3

class Admin_Login_Data():
    def __init__(self):
        self.conn = sqlite3.connect("Database.db")
        self.c = self.conn.cursor()

    def eingeloggter_benutzer_speichern(self, benutzer):
        params = (benutzer, )
        sql = "INSERT INTO eingeloggt VALUES (NULL, ?)"
        self.c.execute(sql, params)
        self.conn.commit()

    def benutzer_ausloggen(self, id):
        params = (id, )
        sql = "DELETE FROM eingeloggt Where id = ?"
        self.c.execute(sql, params)
        self.conn.commit()

    def passwort_check(self, benutzer, passwort):
        params = (benutzer, passwort)
        sql = "SELECT benutzer FROM admin WHERE benutzer = ? AND passwort = ?"
        self.c.execute(sql, params)
        return self.c.fetchall()

    def alle_benutzer_abfragen(self):
        sql = "SELECT * FROM eingeloggt"
        self.c.execute(sql)
        return self.c.fetchall()
