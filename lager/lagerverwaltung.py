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
        self.ui.lager_textfeld_menge.returnPressed.connect(self.test_der_felder)
        self.ui.combobox_lager.currentTextChanged.connect(self.pruefung_auf_textfeld)
        self.ui.lager_textfeld_einsatz.returnPressed.connect(self.zwischenspeicher)

    def test_der_felder(self): # testet auf den text der combobox ob die daten direkt in die Tabelle gelegt werden oder ob noch eine einsatznummer eingegeben werden muss
        text = self.ui.combobox_lager.currentText()
        if text == "Falsch Entnahme - wieder zurück geben" or text == "Auffüllen wegen Fehlbestand":
            self.zwischenspeicher()
        else:
            self.ui.lager_textfeld_einsatz.setFocus() # setzt den fokus auf die einsatznummer

    def zwischenspeicher(self): # speichert die daten zunaechst in der tabelle zur ansicht
        self.ui.lager_error_label.setText(" ")
        barcode = self.ui.lager_textfeld_produkt.text()
        inhalt_menge = self.ui.lager_textfeld_menge.text()
        produkt = Database_Lagerverwaltung().produkt_abfrage(barcode)
        text = self.ui.combobox_lager.currentText()

        try:
            row = self.ui.lager_table.rowCount()
            self.ui.lager_table.insertRow(row)
            self.ui.lager_table.setItem(row, 0, QtWidgets.QTableWidgetItem(str(produkt[0][0])))
            self.ui.lager_table.setItem(row, 1, QtWidgets.QTableWidgetItem(str(inhalt_menge)))
            if text == "Auffüllen nach Einsatz":
                self.ui.lager_table.setItem(row, 2, QtWidgets.QTableWidgetItem(self.ui.lager_textfeld_einsatz.text()))
            if text == "Auffüllen wegen Fehlbestand":
                self.ui.lager_table.setItem(row, 2, QtWidgets.QTableWidgetItem("Auffüllen"))
            if text == "Falsch Entnahme - wieder zurück geben":
                self.ui.lager_table.setItem(row, 2, QtWidgets.QTableWidgetItem("Zurück"))
            self.ui.lager_textfeld_menge.setText("")
            self.ui.lager_textfeld_produkt.setText("")
            self.ui.lager_table.resizeColumnsToContents()
        except (IndexError):
            row = self.ui.lager_table.rowCount()
            self.ui.lager_table.removeRow(row - 1)
            self.ui.lager_error_label.setText("<html><head/><body><p><span style=\" color:#ff0000;\">"
                                              "Produkt mit dem Barcode nicht vorhanden!</span></p></body></html>")

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
        self.ui.lager_error_label.setText("<html><head/><body><p><span style=\" color:#00FF00;\">"
                                          "Eingabe Gespeichert</span></p></body></html>")

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
