import sqlite3

class Barcode_Data():
    def __init__(self):
        self.conn = sqlite3.connect("Database.db")
        self.c = self.conn.cursor()

    def get_barcodes(self):
        sql = "SELECT barcode from lager"
        self.c.execute(sql)
        return self.c.fetchall()

    def get_barcode_location(self):
        sql = "select * from settings_barcode"
        self.c.execute(sql)
        return self.c.fetchall()
