import sqlite3
import urllib.request
import shutil
import os
import platform

class Update_Software():
    def __init__(self):
        self.old_version_directory = ""
        self.update_path = ""
        self.system = ""

    def database_copy(self):
        con = sqlite3.connect("Database.db")
        dbcursor = con.cursor()
        dahin = sqlite3.connect("test.db")
        dahin_cursor = dahin.cursor()
        dbcursor.execute("SELECT `name` FROM `sqlite_master` WHERE `type` = 'table'")
        list_new = []
        for tables in dbcursor:
            list_new.append(tables[0])
        list_old = []
        dahin_cursor.execute("SELECT `name` FROM `sqlite_master` WHERE `type` = 'table'")
        for tables in dahin_cursor:
            list_old.append(tables[0])

        for i in range(0, len(list_new)):
            if list_new[i] in list_old:
                pass
            else:
                sql = "SELECT sql FROM sqlite_master WHERE name='" + list_new[i] + "'"
                dbcursor.execute(sql)
                table = dbcursor.fetchall()
                dahin.execute(str(table[0][0]))

    def get_installation_path(self):
        path = os.getcwd()

        directory = ""
        if self.system == "Linux" or self.system == "Darwin":
            working = path.split("/")
        if self.system == "Windows":
            working = path.split("\\")
        for i in range(0, len(working) - 1):
            if i == len(working) -2:
                self.update_path = directory + working[i] + "/" + "update"
            if i == 0:
                directory = working[0]
            else:
                directory = directory + "/" + working[i]
        self.old_version_directory = directory
        os.listdir(self.old_version_directory)

    def delete_folders_and_files(self):
        pathes = os.listdir(self.old_version_directory)
        for i in range(0, len(pathes)):

            if pathes[i] == "Database.db":
                pass
            elif pathes[i] == "mitarbeiter.db":
                pass
            elif pathes[i] == "mpg.db":
                pass
            elif pathes[i] == "sets.db":
                pass
            else:
                dir = self.old_version_directory + "/" + pathes[i]
                check = os.path.isdir(dir)
                if check == True:
                    shutil.rmtree(dir)
                else:
                    os.remove(dir)
        #os.remove("../main.py")
        #shutil.rmtree("download")
        #shutil.copytree("test", "download")
        pass

    def download_new_version(self):
        # url = 'adresse'
        # urllib.request.urlretrieve(url, self.update_path + "/rdv")
        pass

    def version_check(self):
        #url = 'adresse'
        #urllib.request.urlretrieve(url, 'version.py')
        actual_version = "1.1.0" # datenbank!
        version = ""

        path = str(self.old_version_directory + "/update/version.py")
        with open(path, "r") as f:
           for line in f:
               version = line
        actual_version = actual_version.split(".")
        version = version.split(".")
        if version[0] > actual_version[0]:
            return True
        elif version[0] == actual_version[0]:
            if version[1] > actual_version[1]:
                return True
            if version[1] == actual_version[1] and version[2] > actual_version[2]:
                return True

    def updater(self):
        self.system = platform.system()
        self.get_installation_path()
        check = self.version_check()
        if check == True:
            self.download_new_version()
            self.delete_folders_and_files()





a = Update_Software()
a.updater()