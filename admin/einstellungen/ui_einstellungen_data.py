import sqlite3

class Ui_Einstellungen_Data():
    def __init__(self):
        self.conn = sqlite3.connect("Database.db")
        self.c = self.conn.cursor()

    def __del__(self):
        self.conn.close()  # zum freigeben der Datenbank

    def einstellungen_abfragen(self):
        sql = "SELECT * FROM einstellungen"
        self.c.execute(sql)
        return self.c.fetchall()

    def einstellungen_speichern(self, bool, name):
        liste = self.einstellungen_abfragen()
        if len(liste) < 4:
            sql = "INSERT INTO einstellungen VALUES(NULL, ?, ?)"
        else:
            sql = "UPDATE einstellungen SET bool = ? WHERE name = ? "
        params = (bool, name)
        self.c.execute(sql, params)
        self.conn.commit()

    def pdf_speicherort(self, speicherort, id):
        params = (speicherort, id )
        sql = "UPDATE speicherort_bestellung SET speicherort = ? WHERE id = ?"
        self.conn.execute(sql, params)
        self.conn.commit()

    def speicherort_abfragen(self):
        sql = "SELECT * FROM speicherort_bestellung"
        self.c.execute(sql)
        return self.c.fetchall()

    def get_barcode_location(self):
        sql = "SELECT * FROM settings_barcode"
        self.c.execute(sql)
        return self.c.fetchall()

    def save_barcode_location(self, location, id):
        params = (location, id)
        sql = "UPDATE settings_barcode SET location = ? WHERE id = ?"
        self.conn.execute(sql, params)
        self.conn.commit()

    def save_barcode_minimum(self, id, minimum):
        params = (minimum, id)
        sql = "UPDATE settings_barcode SET minimum = ? WHERE id = ?"
        self.c.execute(sql, params)
        self.conn.commit()

    def save_barcode_sizes(self, id, hight, width, font_size, font_distance):
        params = (hight, width, font_size, font_distance, id)
        sql = "UPDATE settings_barcode SET hight = ?, width = ?, font_size = ?, font_distance = ? WHERE id = ?"
        print(params)
        self.c.execute(sql, params)
        self.conn.commit()