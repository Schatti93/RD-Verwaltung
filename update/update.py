import os
import sys
import shutil
import subprocess
from PyQt5.QtWidgets import QMessageBox
class Updater():
    def __init__(self, ui):
        self.ui = ui

    def update_or_not(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Möchten Sie wirklich Updaten? \nAlles was nicht gespeichert ist, geht verloren.")
        msgBox.setWindowTitle("Wirklich löschen?")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.start_update()

    def start_update(self):
        link = "../update"
        os.makedirs(link)
        shutil.copyfile("update/updater.py", "../update/updater.py")
        filename = os.path.abspath("../update/updater.py")
        subprocess.Popen([sys.executable, filename])
        sys.exit(0)
