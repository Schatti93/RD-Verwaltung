from PyQt5.QtWidgets import QLineEdit
import hashlib
from PyQt5 import QtCore
from admin.login.admin_login_data import Admin_Login_Data
from admin.mpg.update_mpg import Update_Mpg

class Login_Admin():
    def __init__(self, ui):
        self.ui = ui
        self.data = Admin_Login_Data()
        self.ui.login_btn.clicked.connect(self.check)
        self.ui.admin_bereich.setVisible(False)
        self.ui.admin_logout_btn.clicked.connect(self.logout)
        self.ui.admin_text_pw.returnPressed.connect(self.check)
        self.ui.admin_text_pw.setEchoMode(QLineEdit.Password)
        self.bei_start_alte_admin_logins_loeschen()
        self.ui.admin_logout_btn.setVisible(False)

    def bei_start_alte_admin_logins_loeschen(self):
        alte_nutzer = self.data.alle_benutzer_abfragen()
        for element in range(0, len(alte_nutzer)):
            self.data.benutzer_ausloggen(alte_nutzer[element][0])

    def check(self):
        benutzer = self.ui.admin_text_ben.text()
        passwort = self.ui.admin_text_pw.text()
        passwort_hash = hashlib.sha1(passwort.encode('utf-8')).hexdigest()
        liste = self.data.passwort_check(benutzer, passwort_hash)

        if len(liste) == 1:
            self.data.eingeloggter_benutzer_speichern(benutzer)
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
            Update_Mpg(self.ui).update_tabellen_und_combos()
            self.ui.admin_bereich.setVisible(True)
            self.ui.admin_logout_btn.setVisible(True)
            self.ui.login_error_label.setText("")
            self.ui.admin_logout_btn.setVisible(True)



        else:
            self.ui.login_error_label.setText("<html><head/><body><p><span style=\" color:#cc3300 ;\">Passwort / Benutzer falsch</span></p></body></html>")

    def logout(self):
        eingeloggter_user = self.data.alle_benutzer_abfragen()
        self.data.benutzer_ausloggen(eingeloggter_user[0][0])
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
        self.ui.admin_logout_btn.setVisible(False)

