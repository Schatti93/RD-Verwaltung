from PyQt5.QtWidgets import QLineEdit
import hashlib
from PyQt5 import QtCore
from admin.login.admin_login_data import Admin_Login_Data
from admin.mpg.update_mpg import Update_Mpg
from admin.stock.edit_stock_content import Edit_Stock_Content

class Login_Admin():
    def __init__(self, ui):
        self.ui = ui
        self.data = Admin_Login_Data()
        self.ui.login_btn.clicked.connect(self.check)
        self.ui.admin_bereich.setVisible(False)
        self.ui.admin_logout_btn.clicked.connect(self.logout)
        self.ui.admin_text_pw.returnPressed.connect(self.check)
        self.ui.admin_text_pw.setEchoMode(QLineEdit.Password)
        self.delete_old_admins_in_database()
        self.ui.admin_logout_btn.setVisible(False)

    def delete_old_admins_in_database(self):
        old_admins = self.data.old_logins()
        for element in range(0, len(old_admins)):
            self.data.logout_user(old_admins[element][0])

    def check(self):
        user = self.ui.admin_text_user.text()
        password = self.ui.admin_text_pw.text()
        password_hash = hashlib.sha512(password.encode('utf-8')).hexdigest()
        list = self.data.password_check(user, password_hash)

        if len(list) == 1:
            self.data.save_login(user)
            self.ui.admin_text_user.setText("")
            self.ui.admin_text_pw.setText("")
            self.ui.admin_text_user.setVisible(False)
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
            self.ui.admin_text_user.setMaximumSize(QtCore.QSize(0, 0))
            self.ui.benutzer_label.setMaximumSize(QtCore.QSize(0, 0))
            self.ui.passwort_label.setMaximumSize(QtCore.QSize(0, 0))
            Update_Mpg(self.ui).update_tabellen_und_combos()
            # TODO delete Edit Stock entry when Edit_Stock_content.show_all_products_in_table shows all products
            Edit_Stock_Content(self.ui).change_product()
            self.ui.admin_bereich.setVisible(True)
            self.ui.admin_logout_btn.setVisible(True)
            self.ui.login_error_label.setText("")
            self.ui.admin_logout_btn.setVisible(True)

        else:
            self.ui.login_error_label.setText("<html><head/><body><p><span style=\" color:#cc3300 ;\">Passwort / Benutzer falsch</span></p></body></html>")

    def logout(self):
        user_logged_in = self.data.old_logins()
        self.data.logout_user(user_logged_in[0][0])
        self.ui.admin_text_user.setVisible(True)
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
        self.ui.admin_text_user.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ui.benutzer_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ui.passwort_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ui.admin_logout_btn.setVisible(False)

