import sqlite3
from datetime import date
from PyQt5.QtWidgets import QLineEdit
import hashlib
from PyQt5 import QtCore

class Login_Admin():
    def __init__(self, ui):
        self.ui = ui
        self.conn = sqlite3.connect("Database.db")
        self.c = self.conn.cursor()
        self.ui.login_btn.clicked.connect(self.check)
        self.ui.admin_bereich.setVisible(False)
        self.ui.admin_logout_btn.clicked.connect(self.logout)
        self.ui.admin_text_pw.returnPressed.connect(self.check)
        self.ui.admin_text_pw.setEchoMode(QLineEdit.Password)


    def check(self):
        benutzer = self.ui.admin_text_ben.text()
        passwort = self.ui.admin_text_pw.text()
        passwort_hash = hashlib.sha1(passwort.encode('utf-8')).hexdigest()
        params = (benutzer, passwort_hash)
        sql = "SELECT benutzer FROM admin WHERE benutzer = ? AND passwort = ?"
        self.c.execute(sql, params)
        liste = self.c.fetchall()

        if len(liste) == 1:
            self.ui.admin_text_ben.setText("")
            self.ui.admin_text_pw.setText("")
            self.ui.admin_text_ben.setVisible(False)
            self.ui.admin_text_pw.setVisible(False)
            self.ui.login_btn.setVisible(False)
            self.ui.benutzer_label.setVisible(False)
            self.ui.passwort_label.setVisible(False)
            self.ui.login_label.setVisible(False)
            self.ui.login_error_label.setVisible(False)
            self.ui.login_error_label.setMaximumSize(QtCore.QSize(0, 0))
            self.ui.login_btn.setMaximumSize(QtCore.QSize(0, 0))
            self.ui.login_label.setMaximumSize(QtCore.QSize(0, 0))
            self.ui.admin_text_pw.setMaximumSize(QtCore.QSize(0, 0))
            self.ui.admin_text_ben.setMaximumSize(QtCore.QSize(0, 0))
            self.ui.benutzer_label.setMaximumSize(QtCore.QSize(0, 0))
            self.ui.passwort_label.setMaximumSize(QtCore.QSize(0, 0))

            self.ui.admin_bereich.setVisible(True)
            self.ui.admin_logout_btn.setVisible(True)
            self.ui.login_error_label.setText("")



        else:
            self.ui.login_error_label.setText("<html><head/><body><p><span style=\" color:#cc3300 ;\">Passwort / Benutzer falsch</span></p></body></html>")

    def passwort_aendern(self):
        pass

    def logout(self):
        self.ui.admin_text_ben.setVisible(True)
        self.ui.admin_text_pw.setVisible(True)
        self.ui.login_btn.setVisible(True)
        self.ui.benutzer_label.setVisible(True)
        self.ui.passwort_label.setVisible(True)
        self.ui.login_label.setVisible(True)
        self.ui.admin_bereich.setVisible(False)
        self.ui.login_error_label.setVisible(True)
        self.ui.login_error_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ui.login_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ui.login_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ui.admin_text_pw.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ui.admin_text_ben.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ui.benutzer_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ui.passwort_label.setMaximumSize(QtCore.QSize(16777215, 16777215))

