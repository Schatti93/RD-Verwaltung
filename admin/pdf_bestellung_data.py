import sqlite3

class Pdf_Bestellung_Data():
    def __init__(self):
        self.conn = sqlite3.connect("Database.db")
        self.c = self.conn.cursor()

    def __del__(self):
        self.conn.close()  # zum freigeben der Datenbank

    def produkt_abfragen(self, produkt):
        params = (produkt, )
        sql = "SELECT * FROM lager WHERE produkt = ?"
        self.c.execute(sql, params)
        return self.c.fetchall()

