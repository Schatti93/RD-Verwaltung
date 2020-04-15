from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore
from ui.second_window import Ui_second_window
from lager.data_lagerverwaltung import Database_Lagerverwaltung
import re

class Ui_Einstellungen_Lager(QtWidgets.QMainWindow):
    def __init__(self, ui):
        self.ui = ui
        self.data = Database_Lagerverwaltung()
        self.standard_url_combobox()



    def standard_url_combobox(self):
        url_liste = set()
        zwischen_liste = self.data.get_liste()

        zweite = []

        for i in zwischen_liste:
            url_liste.add(i[7])
        for i in url_liste:
            zweite.append((i.split(".")[1] + " URL: " + i))
        self.ui.combobox_standard_url.addItems(zweite)
        ###combo box bekommt daten, standard wert muss noch gespeichert werden



    def hinzufuegen(self, url):
        text = self.ui.combobox_standard_url.currentText()
        sql = "DELETE FROM standard_url"
        self.c.execute(sql)

        params = (url, )
        sql = ""