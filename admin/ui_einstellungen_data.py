import sqlite3

class Ui_Einstellungen_Data():
    def __init__(self):
        self.conn = sqlite3.connect("Database.db")
        self.c = self.conn.cursor()

    def __del__(self):
        self.conn.close()  # zum freigeben der Datenbank

    def einstellungen_abfragen(self):
        sql = "SELECT * FROM einstellungen"
        self.c.execute(sql)
        return self.c.fetchall()

    def einstellungen_speichern(self, bool, name):
        liste = self.einstellungen_abfragen()
        if len(liste) < 4:
            sql = "INSERT INTO einstellungen VALUES(NULL, ?, ?)"
        else:
            sql = "UPDATE einstellungen SET bool = ? WHERE name = ? "
        params = (bool, name)
        self.c.execute(sql, params)
        self.conn.commit()

