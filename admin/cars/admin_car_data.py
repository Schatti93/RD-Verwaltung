import sqlite3

class Admin_Car_Data():
    def __init__(self):
        self.conn = sqlite3.connect("Database.db")
        self.c = self.conn.cursor()

    def save_car(self, radio_identification, license_plate, town, status, tuev, comment):
        params = (radio_identification, license_plate, town, status, tuev, comment )
        sql = "INSERT INTO fahrzeug_aktiv VALUES (NULL, ?, ?, ?, ?, ?, ?)"
        self.c.execute(sql, params)
        self.conn.commit()

    def get_active_cars(self):
        sql = "SELECT * FROM fahrzeug_aktiv"
        self.c.execute(sql)
        return self.c.fetchall()