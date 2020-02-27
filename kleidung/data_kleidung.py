import sqlite3
from datetime import date

class Database_kleidung():
    def __init__(self):
        self.conn = sqlite3.connect("Database.db")
        self.c = self.conn.cursor()
        self.today = today = date.today()
        self.datum = str(today.day) + '.' + str(today.month) + '.' + str(today.year)

    def __del__(self):
        self.conn.close()  # zum freigeben der Datenbank

    def add_barcode(self, barcode):
        params = (barcode, self.datum)
        sql = "INSERT INTO Klamotten VALUES (NULL, ?, ?)"
        self.c.execute(sql, params)
        self.conn.commit()

    def check_barcode(self, barcode):
        params = (barcode, )
        liste = []
        sql = "SELECT barcode FROM Klamotten WHERE barcode = ?"
        self.c.execute(sql, params)
        for row in self.c.fetchall():
            liste.append(str(row[0]))

        if len(liste) > 0:
            self.switch_barcode(barcode)
        else:
            self.add_barcode(barcode)

    def switch_barcode(self, liste):
        params = (str(liste), str(self.datum))
        sql = "INSERT INTO kleidung_zurueck VALUES(NULL,?,?)"
        self.c.execute(sql, params)
        self.conn.commit()
        sql = "DELETE FROM Klamotten WHERE barcode = ?"
        params = (liste, )
        self.c.execute(sql, params)
        self.conn.commit()

    def get_liste(self, name_databank):
        sql = "SELECT * FROM " + str(name_databank)
        self.c.execute(sql)
        return self.c.fetchall()
