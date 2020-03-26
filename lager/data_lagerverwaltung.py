from datetime import date
import sqlite3


# Warnung wenn mindest bestand unterschritten




class Database_Lagerverwaltung():
    def __init__(self):
        self.conn = sqlite3.connect("Database.db")
        self.c = self.conn.cursor()
        self.today = today = date.today()
        self.datum = str(today.day) + '.' + str(today.month) + '.' + str(today.year)


    def __del__(self):
        self.conn.close()  # zum freigeben der Datenbank

    #verpackungsgröße mit einbeziehen

    def new_produkt(self, produkt, bestand, mindest, maximal, barcode, inhalt, artikel_nr):
        params = (produkt, bestand, mindest, maximal, barcode, inhalt, artikel_nr)
        sql = "INSERT INTO lager VALUES (NULL, ?, ?, ?, ?, ?, ?, ?)"
        self.c.execute(sql, params)
        self.conn.commit()

    def del_produkt(self, produkt):
        params = (produkt, )
        sql = "DELETE FROM lager WHERE Produkt = ?"
        self.c.execute(sql, params)
        self.conn.commit()

    #Einsazunummer einfügen
    def entnahme(self, produkt, menge):
        params = (produkt, )
        liste = []
        sql = "SELECT Bestand FROM lager WHERE Produkt = ?"
        self.c.execute(sql, params)
        for row in self.c.fetchall():
            liste.append(int(row[0]))
        neue_menge = liste[0] - menge
        params = (neue_menge, produkt)
        sql = "UPDATE lager SET Bestand = ? WHERE Produkt = ?"
        self.c.execute(sql, params)
        self.conn.commit()

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

    def produkt_abfrage(self, barcode):
        params = (barcode, )
        sql = "SELECT Produkt FROM lager WHERE Barcode = ?"
        self.c.execute(sql, params)
        return self.c.fetchall()

    def barcode_abfrage(self, produkt):
        params = (produkt,)
        sql = "SELECT barcode FROM lager WHERE Produkt = ?"
        self.c.execute(sql, params)
        return self.c.fetchall()

    def get_liste(self):
        sql = "SELECT * FROM lager"
        self.c.execute(sql)
        return self.c.fetchall()

    def einsatz_nachweis(self, nummer, item, menge):
        params = (item, nummer, menge)
        sql = "INSERT INTO lager_nachweis VALUES (NULL, ?, ?, ?)"
        self.c.execute(sql, params)
        self.conn.commit()

