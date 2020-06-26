import sqlite3

class Employee_Data():
    def __init__(self):
        self.conn = sqlite3.connect("mitarbeiter.db")
        self.c = self.conn.cursor()
        self.conn_mpg = sqlite3.connect("mpg.db")
        self.c_mpg = self.conn_mpg.cursor()

    def neuer_mitarbeiter_speichern(self, vorname, nachname, status):
        params = (vorname, nachname, status)
        sql = "INSERT INTO mitarbeiter VALUES (NULL, ?, ?, ?)"
        self.c.execute(sql, params)
        self.conn.commit()

    def alle_ma_abfragen(self):
        sql = "SELECT * FROM mitarbeiter"
        self.c.execute(sql)
        return self.c.fetchall()

    def ma_loeschen(self, ma_id):
        params = (ma_id, )
        sql = "DELETE FROM mitarbeiter WHERE id = ?"
        self.c.execute(sql, params)
        self.conn.commit()

    def delete_employee_data(self, employee):
        sql = "DELETE FROM mpg_einweisungen WHERE eingewiesener = ?"
        params = (employee, )
        self.conn_mpg.execute(sql, params)
        self.conn_mpg.commit()