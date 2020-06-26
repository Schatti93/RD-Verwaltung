import sqlite3
import urllib.request
import shutil
import os
import platform
import sys
from PyQt5 import QtWidgets
from mainwindow import Ui_MainWindow
from datetime import date
from zipfile import ZipFile
import time
import subprocess

app = QtWidgets.QApplication(sys.argv)

class Update_Software(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.update_finish_btn.setVisible(False)
        self.ui.progressBar.setProperty("value", 0)
        self.old_version_directory = ""
        self.update_path = ""
        self.backup_path = ""
        self.system = ""
        self.safe_list = ["venv", "Database.db", "employees.db",
                          "mpg.db", "sets.db", "version.db"]
        self.ui.update_btn.clicked.connect(self.updater)
        self.ui.update_finish_btn.clicked.connect(self.start_rdv)

    def database_copy(self):
        for database in range(0, len(self.safe_list)): # loop to go through all databases
            if ".db" in self.safe_list[database]:
                con_update = sqlite3.connect("../update/rdv/" + self.safe_list[database])
                c_update = con_update.cursor()
                con_old = sqlite3.connect(self.safe_list[database])
                c_old = con_old.cursor()
                c_update.execute("SELECT `name` FROM `sqlite_master` WHERE `type` = 'table'")
                list_new = []
                for tables in c_update: # loop to get all tables of the database
                    list_new.append(tables[0])
                list_old = []
                c_old.execute("SELECT `name` FROM `sqlite_master` WHERE `type` = 'table'")
                for tables in c_old:  # loop to get all tables of the the old database
                    list_old.append(tables[0])

                for i in range(0, len(list_new)): # loop to insert not existing tables
                    if list_new[i] in list_old:
                        pass
                    else:
                        tables = list_new[i]

                        sql = "SELECT sql FROM sqlite_master WHERE name='" + list_new[i] + "'"
                        c_update.execute(sql)
                        table = c_update.fetchall()
                        con_old.execute(str(table[0][0]))

                        sql = "SELECT * FROM " + list_new[i]
                        c_update.execute(sql)
                        datas = c_update.fetchall()

                        for p in range(0, len(datas)): # loop to go through the datas of new table
                            insert_questionmark = ""
                            for j in range(0, len(datas[i])): # loop to create the questionmarks for sql
                                if j == 0:
                                    if datas[p][0] == "NULL":
                                        insert_questionmark = "NULL,"
                                    else:
                                        insert_questionmark = "?,"
                                elif j == len(datas[i]) - 1:
                                    insert_questionmark = insert_questionmark + "?"
                                else:
                                    insert_questionmark = insert_questionmark + " ?,"
                            sql = "INSERT INTO " + tables + " VALUES (" + insert_questionmark + ")"
                            c_old.execute(sql, datas[i])
                            con_old.commit()

    def get_installation_path(self):
        path = os.getcwd()
        directory = ""
        today = date.today()
        today_format = str(today.day) + '.' + str(today.month) + '.' + str(today.year)
        if self.system == "Linux" or self.system == "Darwin":
            working = path.split("/")
        if self.system == "Windows":
            working = path.split("\\")
        for i in range(0, len(working)):
            if i == len(working) -2:
                self.update_path = directory + "/" + working[i] + "/" + "update"
                check_update_path_exists = True
                count = 1
                while check_update_path_exists == True:
                    path = directory + "/" + working[i] + "/" + working[i + 1] + "_backup_" + str(today_format)
                    check = os.path.isdir(path)
                    if check == True:
                        path = directory + "/" + working[i] + "/" + working[i + 1] + "_backup_" + str(today_format) + "_" + str(count)
                        check = os.path.isdir(path)
                        if check == True:
                            count += 1
                        else:
                            self.backup_path = directory + "/" + working[i] + "/" + working[i + 1] + "_backup_" + str(
                                today_format) + "_" + str(count)
                            check_update_path_exists = False
                    else:
                        self.backup_path = directory + "/" + working[i] + "/" + working[i + 1] + "_backup_" + str(today_format)
                        check_update_path_exists = False
            if i == 0:
                directory = working[0]
            else:
                directory = directory + "/" + working[i]
        self.old_version_directory = directory
        os.listdir(self.old_version_directory)

    def delete_folders_and_files(self):
        pathes = os.listdir(self.old_version_directory)
        list = []
        for i in range(0, len(pathes)):
            if pathes[i] in self.safe_list:
                pass
            else:
                list.append(pathes[i])
        for i in range(0, len(list)):
            directory = self.old_version_directory + "/" + list[i]
            check = os.path.isdir(directory)
            if check == True:
                shutil.rmtree(directory)
            else:
                os.remove(directory)

    def download_new_version(self):
        url = 'http://rd-v.site/rdv/rdv.zip'
        urllib.request.urlretrieve(url, self.update_path + "/rdv.zip")
        with ZipFile(self.update_path + '/rdv.zip', 'r') as zipObj:
            zipObj.extractall(self.update_path)

    def copy_update_files(self):
        copy_list = []
        pathes = os.listdir(self.update_path + "/rdv/")
        for i in range(0, len(pathes)):
            if pathes[i] in self.safe_list:
                pass
            else:
                copy_list.append(pathes[i])
        for i in range(0, len(copy_list)):
            path_from = self.update_path + "/rdv/" + copy_list[i]
            path_to = self.old_version_directory + "/" + copy_list[i]
            check = os.path.isdir(path_from)
            if check == True:
                shutil.copytree(path_from, path_to)
            else:
                shutil.copyfile(path_from, path_to)

    def delete_update_path(self):
        shutil.rmtree(self.update_path)

    def update_version_in_database(self):
        conn = sqlite3.connect(self.old_version_directory + "/version.db")
        c = conn.cursor()
        sql = "SELECT * FROM version"
        c.execute(sql)
        old_version = c.fetchall()[0][0]
        url = 'http://rd-v.site/version.txt'
        urllib.request.urlretrieve(url, 'update/version.txt')
        path = str("update/version.txt")
        with open(path, "r") as f:
            for line in f:
                new_version = line
        sql = "UPDATE version SET version = ? Where version = ?"
        params = (new_version, old_version)
        c.execute(sql, params)
        conn.commit()

    def make_backup(self):
        shutil.copytree(self.old_version_directory, self.backup_path)

    def updater(self):
        self.ui.show_status_label.setText("Und Los!")
        self.system = platform.system()
        self.get_installation_path()
        time.sleep(0.5)
        self.ui.progressBar.setProperty("value", 2)
        self.ui.show_status_label.setText("Erstelle Backup")
        self.make_backup()
        self.ui.progressBar.setProperty("value", 15)
        time.sleep(2)
        self.ui.show_status_label.setText("Lade das Update runter")
        self.download_new_version()
        self.ui.progressBar.setProperty("value", 20)
        time.sleep(2)
        self.ui.show_status_label.setText("Lösche alte Dateien")
        self.delete_folders_and_files()
        self.ui.progressBar.setProperty("value", 50)
        time.sleep(2)
        self.ui.show_status_label.setText("Update wird eingefügt")
        self.copy_update_files()
        self.ui.progressBar.setProperty("value", 80)
        time.sleep(2)
        self.ui.show_status_label.setText("Überprüfe die Datenbanken")
        self.database_copy()
        self.ui.progressBar.setProperty("value", 90)
        time.sleep(2)
        self.ui.show_status_label.setText("Lösche den Download")
        self.delete_update_path()
        time.sleep(2)
        self.ui.progressBar.setProperty("value", 100)
        self.ui.show_status_label.setText("Fertig!")
        self.ui.update_finish_btn.setVisible(True)
        self.ui.update_btn.setVisible(False)

    def start_rdv(self):
        subprocess.Popen([sys.executable, self.old_version_directory + "/main.py"])
        sys.exit(0)

window = Update_Software()
window.show()
sys.exit(app.exec_())




