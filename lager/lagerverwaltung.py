from PyQt5 import QtWidgets
from lager.data_lagerverwaltung import Database_Lagerverwaltung
from lager.online_bestellung import Online_Bestellung

class Lagerverwaltung():
    def __init__(self, ui):
        self.ui = ui
        self.lagerverwaltung = Database_Lagerverwaltung()
        self.bestellen = Online_Bestellung()
        self.ui.lager_btn.clicked.connect(self.durchgehen)
        self.ui.lager_bestellung.clicked.connect(self.bestellen.nachbestellen)
        self.ui.combobox_lager.currentTextChanged.connect(self.pruefung_auf_textfeld)
        self.ui.lager_textfeld_produkt.returnPressed.connect(self.zwischenspeicher)
        self.ui.lager_uebernehmen_btn.clicked.connect(self.zwischenspeicher)

    def test_der_felder(self): # testet auf den text der combobox ob die daten direkt in die Tabelle gelegt werden oder ob noch eine einsatznummer eingegeben werden muss
        text = self.ui.combobox_lager.currentText()
        if text == "Falsch Entnahme - wieder zurück geben" or text == "Auffüllen wegen Fehlbestand":
            pass
        else:
            self.ui.lager_textfeld_einsatz.setFocus() # setzt den fokus auf die einsatznummer

    def pruefung_eintrag_vorhanden_tabelle(self, produkt):
        rows = self.ui.lager_table.rowCount()
        count = 0
        for i in range(0, rows):
            produkt_tabelle = self.ui.lager_table.item(i, 0).text()
            if produkt_tabelle == produkt:
                anzahl = int(self.ui.lager_table.item(i, 1).text())
                anzahl += 1
                self.ui.lager_table.setItem(i, 1, QtWidgets.QTableWidgetItem(str(anzahl)))
                self.ui.lager_textfeld_produkt.setText("")
                self.ui.lager_table.resizeColumnsToContents()
                count = 1
        return count

    def zwischenspeicher(self): # speichert die daten zunaechst in der tabelle zur ansicht
        modus = self.ui.combobox_lager.currentText()
        einsatznummer = self.ui.lager_textfeld_einsatz.text()
        durchfuehren = 1
        if modus == "Auffüllen nach Einsatz":
            if einsatznummer == "":
                self.ui.lager_textfeld_einsatz.setFocus()
                self.ui.lager_error_label.setText("Einsatznummer eingeben!")
                self.ui.lager_error_label.setStyleSheet("color:#ffffff; border: 1px solid red; border-radius: 5px")
                durchfuehren = 0
        if durchfuehren == 1:
            self.ui.lager_error_label.setText(" ")
            self.ui.lager_error_label.setStyleSheet("")
            barcode = self.ui.lager_textfeld_produkt.text()
            produkt = Database_Lagerverwaltung().produkt_abfrage(barcode)
            text = self.ui.combobox_lager.currentText()
            rows = self.ui.lager_table.rowCount()
            if len(produkt) == 0:
                self.ui.lager_error_label.setText("Produkt mit dem Barcode nicht vorhanden!")
                self.ui.lager_error_label.setStyleSheet("color:#ffffff; border: 1px solid red; border-radius: 5px")

            else:
                pruefung = self.pruefung_eintrag_vorhanden_tabelle(produkt[0][0])
                if pruefung == 0:
                    row = self.ui.lager_table.rowCount()
                    self.ui.lager_table.insertRow(row)
                    self.ui.lager_table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(produkt[0][0])))
                    self.ui.lager_table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(1)))
                    if text == "Auffüllen nach Einsatz":
                        self.ui.lager_table.setItem(row, 2, QtWidgets.QTableWidgetItem(self.ui.lager_textfeld_einsatz.text()))
                    if text == "Auffüllen wegen Fehlbestand":
                        self.ui.lager_table.setItem(row, 2, QtWidgets.QTableWidgetItem("Auffüllen"))
                    if text == "Falsch Entnahme - wieder zurück geben":
                        self.ui.lager_table.setItem(row, 2, QtWidgets.QTableWidgetItem("Zurück"))

                    self.ui.lager_textfeld_produkt.setText("")
                    self.ui.lager_table.resizeColumnsToContents()



    def durchgehen(self): #holt die daten aus der Tabelle und übergibt sie an die passende funktion zum entnehmen etc.
        row = self.ui.lager_table.rowCount()
        for i in range(0, row):
            text = self.ui.lager_table.item(0, 2).text()
            if text == "Zurück":
                item = self.ui.lager_table.item(0, 0).text()
                menge = self.ui.lager_table.item(0, 1).text()
                Database_Lagerverwaltung().auffuellen(item, int(menge))
                self.ui.lager_table.removeRow(0)

            else:
                item = self.ui.lager_table.item(0, 0).text()
                menge = self.ui.lager_table.item(0, 1).text()
                Database_Lagerverwaltung().entnahme(item, int(menge))

                try:
                    nummer = int(text)
                    if nummer >= 0:
                        nummer = self.ui.lager_table.item(0, 2).text()
                        self.lagerverwaltung.einsatz_nachweis(nummer, item, menge)
                except (TypeError, ValueError):
                    pass
            self.ui.lager_table.removeRow(0)
        self.ui.lager_error_label.setText("Eingabe Gespeichert")
        self.ui.lager_error_label.setStyleSheet("color:#ffffff; font-size:13pt; border: 1px solid #00FF00; border-radius: 5px")
        self.ui.lager_textfeld_einsatz.setText("")
    def pruefung_auf_textfeld(self): # prueft auf welchem text gerade dei Combobox steht um das Einsatznummer feld anzuzeigen oder nicht.
        text = self.ui.combobox_lager.currentText()
        if text == "Falsch Entnahme - wieder zurück geben" or text == "Auffüllen wegen Fehlbestand":
            self.ui.lager_textfeld_einsatz.setVisible(False)
            self.ui.label_einsatznummer.setVisible(False)
            self.ui.label_einsatznummer_enter.setVisible(False)
        else:
            self.ui.lager_textfeld_einsatz.setVisible(True)
            self.ui.label_einsatznummer.setVisible(True)
            self.ui.label_einsatznummer_enter.setVisible(True)
