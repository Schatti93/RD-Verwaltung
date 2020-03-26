import sqlite3
from lager.data_lagerverwaltung import Database_Lagerverwaltung
from selenium import webdriver
import platform

class Online_Bestellung():
    def __init__(self):
        self.conn = sqlite3.connect("Database.db")
        self.c = self.conn.cursor()
        self.lager = Database_Lagerverwaltung()


    def nachbestellen(self):
        liste = self.lager.get_liste()
        nachbestellen = []
        menge = []
        for i in range(0, len(liste)):
            if int(liste[i][2]) < int(liste[i][3]):
                nachbestellen.append(str(liste[i][7]))
                count = 0
                counter = 0
                bestand = liste[i][2]
                inh_meng = liste[i][6]
                while count == 0:
                    if bestand + inh_meng < liste[i][4]:
                        bestand = bestand + liste[i][6]
                        counter += 1
                    else:
                        counter += 1
                        menge.append(counter)
                        count += 1
        if len(nachbestellen) == 0:
            pass
        else:
            system = platform.system()
            architektur = platform.architecture()[0]
            if system == "Darwin":
                driver = webdriver.Firefox(executable_path=r"lager/geckodriver_macos")
            if system == "Linux":
                driver = webdriver.Firefox(executable_path=r"lager/geckodriver_linux64")
            if system == "Windows" and architektur == "64bit":
                driver = webdriver.Firefox(executable_path=r"lager/geckodriver_win64.exe")
            if system == "Windows" and architektur == "32bit":
                driver = webdriver.Firefox(executable_path=r"lager/geckodriver_win32.exe")

            for i in range(0, len(nachbestellen)):
                url = "https://www.meetb.de/search?sSearch=" + nachbestellen[i]
                driver.get(url)
                driver.find_element_by_xpath("//*[@id='sQuantity']/option[text()=" + str(menge[i]) + "]").click()

                driver.find_element_by_class_name("buy-btn--cart-text").click()
                driver.implicitly_wait(10)