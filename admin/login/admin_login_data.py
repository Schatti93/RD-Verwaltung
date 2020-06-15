import sqlite3

class Admin_Login_Data():
    def __init__(self):
        self.conn = sqlite3.connect("Database.db")
        self.c = self.conn.cursor()

    def save_login(self, user):
        params = (user, )
        sql = "INSERT INTO eingeloggt VALUES (NULL, ?)"
        self.c.execute(sql, params)
        self.conn.commit()

    def logout_user(self, id):
        params = (id, )
        sql = "DELETE FROM eingeloggt Where id = ?"
        self.c.execute(sql, params)
        self.conn.commit()

    def password_check(self, user, password):
        params = (user, password)
        sql = "SELECT benutzer FROM admin WHERE benutzer = ? AND passwort = ?"
        self.c.execute(sql, params)
        return self.c.fetchall()

    def old_logins(self):
        sql = "SELECT * FROM eingeloggt"
        self.c.execute(sql)
        return self.c.fetchall()
