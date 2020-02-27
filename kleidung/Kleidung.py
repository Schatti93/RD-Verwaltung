from datetime import date
from PyQt5 import QtWidgets
from kleidung.data_kleidung import Database_kleidung
from PyQt5.QtCore import Qt


class Kleidung():
    def __init__(self, ui):

        self.ui = ui
        self.ui.klamotten_button.clicked.connect(self.durchgehen)
        self.ui.klamotten_textfeld.returnPressed.connect(self.zwischenspeicher)
        self.einlesen("Klamotten", "kleidung_zurueck") # liest die daten ein


    def zwischenspeicher(self):
        inhalt = self.ui.klamotten_textfeld.text()  # suchbegriff entgegen genommen
        row = self.ui.aufnahme.rowCount()
        name =  QtWidgets.QTableWidgetItem(inhalt)
        name.setTextAlignment(Qt.AlignHCenter)
        self.ui.aufnahme.insertRow(row)
        self.ui.aufnahme.setItem(row, 0, name)
        self.ui.klamotten_textfeld.setText("")


    def durchgehen(self):
        row = self.ui.aufnahme.rowCount()
        for i in range(0, row):
            item = self.ui.aufnahme.item(0, 0).text()
            self.ein_aus(item)
            self.ui.aufnahme.removeRow(0)

    def einlesen(self, name_databank, name_zweite_datenbank):
        liste = Database_kleidung().get_liste(name_databank)
        for i in range(0, len(liste)):
            barcode = QtWidgets.QTableWidgetItem(liste[i][1])
            barcode.setTextAlignment(Qt.AlignCenter)
            datum = QtWidgets.QTableWidgetItem(liste[i][2])
            datum.setTextAlignment(Qt.AlignCenter)
            row = self.ui.klamotten_tabelle.rowCount()
            self.ui.klamotten_tabelle.insertRow(row)
            self.ui.klamotten_tabelle.setItem(row, 0, barcode)
            self.ui.klamotten_tabelle.setItem(row, 1, datum)
            self.ui.klamotten_tabelle.horizontalHeader().setSectionResizeMode(1)
        liste = Database_kleidung().get_liste(name_zweite_datenbank)

        for i in range(0, len(liste)):
            barcode2 = QtWidgets.QTableWidgetItem(liste[i][1])
            barcode2.setTextAlignment(Qt.AlignCenter)
            datum = QtWidgets.QTableWidgetItem(liste[i][2])
            datum.setTextAlignment(Qt.AlignCenter)
            row = self.ui.kleidung_zurueck_tabelle.rowCount()
            self.ui.kleidung_zurueck_tabelle.insertRow(row)
            self.ui.kleidung_zurueck_tabelle.setItem(row, 0, barcode2)
            self.ui.kleidung_zurueck_tabelle.setItem(row, 1, datum)
            self.ui.kleidung_zurueck_tabelle.horizontalHeader().setSectionResizeMode(1)


    def ein_aus(self, item):
        row = self.ui.klamotten_tabelle.rowCount()
        today = date.today()
        heute = str(today.day) + '.' + str(today.month) + '.' + str(today.year)
        inhalt = item  # suchbegriff entgegen genommen
        Database_kleidung().check_barcode(item) # Datenbank aktualisieren
        group = []
        remove = 0 # zeile die gelöscht wird falls inhalt im textfeld schon besteht
        for i in range(0, row):
            item = self.ui.klamotten_tabelle.item(i, 0).text()
            if item == inhalt: # Wenn der eintrag im textfeld schon vorhanden ist, wird remove auf den inhalt der Tabelle gesetzt und dieser dann spaeter aus der Tabelle entfernt
                remove = i
            group.append(item)
        if inhalt in group:
            self.zurueck(remove, inhalt, heute)
            group = [] # muss wieder leer werden damit die suche nach doppelten eintraegen von vorne beginnen kann
        else:
            self.neuer_eintrag(inhalt, heute)

    def zurueck(self, remove, inhalt, heute):
        barcode = QtWidgets.QTableWidgetItem(inhalt)
        barcode.setTextAlignment(Qt.AlignCenter)
        datum = QtWidgets.QTableWidgetItem(heute)
        datum.setTextAlignment(Qt.AlignCenter)
        row = self.ui.kleidung_zurueck_tabelle.rowCount()
        self.ui.kleidung_zurueck_tabelle.insertRow(row)
        self.ui.kleidung_zurueck_tabelle.setItem(row, 0, barcode)
        self.ui.kleidung_zurueck_tabelle.setItem(row, 1, datum)
        self.ui.kleidung_zurueck_tabelle.horizontalHeader().setSectionResizeMode(1)
        self.ui.klamotten_tabelle.removeRow(remove) #eintrag der doppelt waere wird gelöscht aus der Tabelle
        rows = self.ui.klamotten_tabelle.rowCount()


    def neuer_eintrag(self, inhalt, heute):
        row = self.ui.klamotten_tabelle.rowCount()
        self.ui.klamotten_tabelle.insertRow(row)
        barcode = QtWidgets.QTableWidgetItem(inhalt)
        barcode.setTextAlignment(Qt.AlignCenter)
        datum = QtWidgets.QTableWidgetItem(heute)
        datum.setTextAlignment(Qt.AlignCenter)
        self.ui.klamotten_tabelle.setItem(row, 0, barcode)
        self.ui.klamotten_tabelle.setItem(row, 1, datum)
        self.ui.klamotten_tabelle.horizontalHeader().setSectionResizeMode(1)


