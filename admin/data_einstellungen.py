import sqlite3

class Data_Einstellungen():
    def __init__(self):
        self.conn = sqlite3.connect("Database.db")
        self.c = self.conn.cursor()

    def standard_url_speichern(self):
