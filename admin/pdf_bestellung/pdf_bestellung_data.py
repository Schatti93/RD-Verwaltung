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

    def alle_produkte(self):
        sql = "SELECT * FROM lager"
        self.c.execute(sql)
        return self.c.fetchall()

    def status_aendern(self, produkt):
        params = ("Bestellt", produkt)
        sql = "UPDATE lager SET status = ? WHERE Produkt = ?"
        self.c.execute(sql, params)
        self.conn.commit()

    def speicherort_abfragen(self):
        sql = "SELECT * FROM speicherort_bestellung"
        self.c.execute(sql)
        return self.c.fetchall()
