import sqlite3

class Sets_Data():
    def __init__(self):
        self.conn = sqlite3.connect("sets.db")
        self.c = self.conn.cursor()
        self.conn_lager = sqlite3.connect("Database.db")
        self.c_lager = self.conn_lager.cursor()

    def save_set(self, name, barcode, product_barcodes):
        params = (name, product_barcodes, barcode)
        sql = "INSERT INTO sets VALUES (NULL, ?, ?, ?)"
        self.c.execute(sql, params)
        self.conn.commit()

    def ask_set_names(self):
        sql = "SELECT name FROM sets"
        self.c.execute(sql)
        return self.c.fetchall()

    def ask_produkt_name(self, barcode):
        params = (barcode, )
        sql = "SELECT Produkt from lager WHERE Barcode = ?"
        self.c_lager.execute(sql, params)
        return self.c_lager.fetchall()