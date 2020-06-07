import sqlite3
from datetime import date

class Admin_Lager_Data():
    def __init__(self):
        self.conn = sqlite3.connect("Database.db")
        self.c = self.conn.cursor()
        self.conn_sets = sqlite3.connect("sets.db")
        self.c_sets = self.conn_sets.cursor()
        self.today = today = date.today()
        self.datum = str(today.day) + '.' + str(today.month) + '.' + str(today.year)

    def new_produkt(self, produkt, bestand, mindest, maximal, barcode, inhalt, artikel_nr, status):
        params = (produkt, bestand, mindest, maximal, barcode, inhalt, artikel_nr, status)
        sql = "INSERT INTO lager VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)"
        self.c.execute(sql, params)
        self.conn.commit()

    def barcode_abfrage(self, produkt):
        params = (produkt,)
        sql = "SELECT barcode FROM lager WHERE Produkt = ?"
        self.c.execute(sql, params)
        return self.c.fetchall()

    def produkt_abfrage(self, barcode):
        params = (barcode, )
        sql = "SELECT Produkt FROM lager WHERE Barcode = ?"
        self.c.execute(sql, params)
        return self.c.fetchall()

    def del_produkt(self, produkt):
        params = (produkt, )
        sql = "DELETE FROM lager WHERE Produkt = ?"
        self.c.execute(sql, params)
        self.conn.commit()

    def update_alle_produkte(self, id, produkt, bestand, mindest, maximun, barcode, inhalt, artnr):
        params = (produkt, bestand, mindest, maximun, barcode, inhalt, artnr, id)
        sql = "UPDATE lager SET Produkt = ?, Bestand = ?, 'Mindest bestand' = ?, 'Maximal Bestand' = ?," \
              " Barcode = ?, inhalt_menge = ?, artikel_nr = ? WHERE id = ?"
        self.c.execute(sql, params)
        self.conn.commit()

    def get_liste(self):
        sql = "SELECT * FROM lager"
        self.c.execute(sql)
        return self.c.fetchall()

    def auffuellen(self, produkt, menge):
        params = (produkt, )
        liste = []
        sql = "SELECT Bestand FROM lager WHERE Produkt = ?"
        self.c.execute(sql, params)
        for row in self.c.fetchall():
            liste.append(int(row[0]))
        neue_menge = liste[0] + menge

        params = (neue_menge, produkt)
        sql = "UPDATE lager SET Bestand = ? WHERE Produkt = ?"
        self.c.execute(sql, params)
        self.conn.commit()

    def update_status(self, name, status):
        params = (status, name)
        sql = "UPDATE lager SET status = ? WHERE produkt = ?"
        self.c.execute(sql, params)
        self.conn.commit()
