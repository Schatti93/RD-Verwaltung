import sqlite3

class Sets_Data():
    def __init__(self):
        self.conn = sqlite3.connect("sets.db")
        self.c = self.conn.cursor()
        self.conn_lager = sqlite3.connect("Database.db")
        self.c_lager = self.conn_lager.cursor()

    def save_set(self, name, barcode, product_barcodes):
        params = (name, str(product_barcodes), barcode)
        sql = "INSERT INTO sets VALUES (NULL, ?, ?, ?)"
        self.c.execute(sql, params)
        self.conn.commit()

    def all_set_names(self):
        sql = "SELECT name FROM sets"
        self.c.execute(sql)
        return self.c.fetchall()

    def ask_product_name(self, barcode):
        params = (barcode, )
        sql = "SELECT Produkt from stock WHERE Barcode = ?"
        self.c_lager.execute(sql, params)
        return self.c_lager.fetchall()

    def get_set_products(self, set):
        params = (set, )
        sql = "SELECT produkte from sets WHERE name = ?"
        self.c.execute(sql, params)
        return self.c.fetchall()

    def get_set_barcode(self, name):
        params = (name, )
        sql = "SELECT barcode from sets WHERE name = ?"
        self.c.execute(sql, params)
        return self.c.fetchall()

    def update_set(self, name, barcode, products):
        params = (products, name, barcode)
        sql = "UPDATE sets SET produkte = ? WHERE name = ? and barcode = ?"
        self.c.execute(sql, params)
        self.conn.commit()

    def delete_set(self, barcode):
        params = (barcode, )
        sql = "DELETE FROM sets WHERE barcode = ?"
        self.c.execute(sql, params)
        self.conn.commit()