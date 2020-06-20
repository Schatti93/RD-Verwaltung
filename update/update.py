import os
import sys
import shutil
import subprocess
from PyQt5.QtWidgets import QMessageBox
import urllib.request
import sqlite3

class Updater():
    def __init__(self, ui):
        self.ui = ui

    def delete_update_path(self):
        directory = "../update"
        check = os.path.isdir(directory)
        if check == True:
            shutil.rmtree(directory)

    def update_or_not(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Möchten Sie wirklich Updaten? \nAlles was nicht gespeichert ist, geht verloren.")
        msgBox.setWindowTitle("Wirklich Updaten?")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.start_update()

    def update_available(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Ein Update ist verfügbar. Soll das Update durchgeführt werden?")
        msgBox.setWindowTitle("Update Manager")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.update_or_not()

    def clear_messagebox(self, text, window_tile):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(text)
        msgBox.setWindowTitle(window_tile)
        msgBox.setStandardButtons(QMessageBox.Ok)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            pass

    def start_update(self):
        link = "../update"
        os.makedirs(link)
        shutil.copyfile("update/updater.py", "../update/updater.py")
        shutil.copyfile("update/ui/mainwindow.py", "../update/mainwindow.py")
        filename = os.path.abspath("../update/updater.py")
        subprocess.Popen([sys.executable, filename])
        sys.exit(0)

    def version_check(self):
        try:
            url = 'http://rd-v.site/version.txt'
            urllib.request.urlretrieve(url, 'update/version.txt')

            actual_version = self.get_current_version()[0][0]
            version = ""

            path = str("update/version.txt")
            with open(path, "r") as f:
                for line in f:
                    version = line
            actual_version = actual_version.split(".")
            version = version.split(".")
            check = False
            if version[0] > actual_version[0]:
                check = True
            elif version[0] == actual_version[0]:
                if version[1] > actual_version[1]:
                    check = True
                if version[1] == actual_version[1] and version[2] > actual_version[2]:
                    check = True
            if check == False:
                self.clear_messagebox("Kein neues Update_verfügbar",
                                      "Update Manager")
            else:
                self.update_available()
        except urllib.error.URLError:
            self.clear_messagebox("Es besteht keine Verbindung zum Internet", "Update Manager")

    def get_current_version(self):
        conn = sqlite3.connect("version.db")
        c = conn.cursor()
        sql = "SELECT * FROM version"
        c.execute(sql)
        return c.fetchall()