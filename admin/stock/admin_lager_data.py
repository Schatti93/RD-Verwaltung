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

    def new_produkt(self, product, in_stock, min, max, barcode, content, item_number, status):
        params = (product, in_stock, min, max, barcode, content, item_number, status)
        sql = "INSERT INTO lager VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)"
        self.c.execute(sql, params)
        self.conn.commit()

    def get_barcode(self, product):
        params = (product,)
        sql = "SELECT barcode FROM lager WHERE Produkt = ?"
        self.c.execute(sql, params)
        return self.c.fetchall()

    def get_product(self, barcode):
        params = (barcode, )
        sql = "SELECT Produkt FROM lager WHERE Barcode = ?"
        self.c.execute(sql, params)
        return self.c.fetchall()

    def del_product(self, product):
        params = (product, )
        sql = "DELETE FROM lager WHERE Produkt = ?"
        self.c.execute(sql, params)
        self.conn.commit()

    def update_all_products(self, id, product, in_stock, min, max, barcode, content, item_number):
        params = (product, in_stock, min, max, barcode, content, item_number, id)
        sql = "UPDATE lager SET Produkt = ?, Bestand = ?, 'Mindest bestand' = ?, 'Maximal Bestand' = ?," \
              " Barcode = ?, inhalt_menge = ?, artikel_nr = ? WHERE id = ?"
        self.c.execute(sql, params)
        self.conn.commit()

    def get_liste(self):
        sql = "SELECT * FROM lager"
        self.c.execute(sql)
        return self.c.fetchall()

    def fill_up(self, barcode, amount):
        params = (barcode, )
        sql = "SELECT Bestand FROM lager WHERE barcode = ?"
        self.c.execute(sql, params)
        new_amount = self.c.fetchall()[0][0] + amount
        params = (new_amount, barcode)
        sql = "UPDATE lager SET Bestand = ? WHERE barcode = ?"
        self.c.execute(sql, params)
        self.conn.commit()

    def update_status(self, name, status):
        params = (status, name)
        sql = "UPDATE lager SET status = ? WHERE produkt = ?"
        self.c.execute(sql, params)
        self.conn.commit()
