import sqlite3
from datetime import date

class Clothes_Data():
    def __init__(self):
        self.conn = sqlite3.connect("Database.db")
        self.c = self.conn.cursor()
        self.today = date.today()
        self.datum = str(self.today.day) + '.' + str(self.today.month) + '.' + str(self.today.year)

    def __del__(self):
        self.conn.close()  # zum freigeben der Datenbank

    def add_barcode(self, barcode):
        params = (barcode, self.datum)
        sql = "INSERT INTO Klamotten VALUES (NULL, ?, ?)"
        self.c.execute(sql, params)
        self.conn.commit()

    def check_barcode(self, barcode):
        params = (barcode, )
        list = []
        sql = "SELECT barcode FROM Klamotten WHERE barcode = ?"
        self.c.execute(sql, params)
        for row in self.c.fetchall():
            list.append(str(row[0]))

        if len(list) > 0:
            self.switch_barcode(barcode)
        else:
            self.add_barcode(barcode)

    def switch_barcode(self, list):
        params = (str(list), str(self.datum))
        sql = "INSERT INTO kleidung_zurueck VALUES(NULL,?,?)"
        self.c.execute(sql, params)
        self.conn.commit()
        sql = "DELETE FROM Klamotten WHERE barcode = ?"
        params = (list, )
        self.c.execute(sql, params)
        self.conn.commit()

    def get_liste(self, name_database):
        sql = "SELECT barcode, datum FROM " + str(name_database)
        self.c.execute(sql)
        return self.c.fetchall()
