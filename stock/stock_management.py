from stock.stock_management_data import Stock_Management_Data
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
from datetime import date
from PyQt5.QtGui import QIntValidator
from admin.stock.update_stock import Update_Stock

class Stock_Management():
    def __init__(self, ui, fill_table):
        self.ui = ui
        self.fill_table = fill_table
        self.data = Stock_Management_Data()

        self.ui.stock_save_btn.clicked.connect(self.save)
        self.ui.combobox_stock.currentTextChanged.connect(self.check_combobox_content)
        self.ui.stock_textfield_product.returnPressed.connect(self.save_in_table)
        self.ui.stock_accept_btn.clicked.connect(self.save_in_table)
        self.ui.clear_table_btn.clicked.connect(self.clear_table)
        self.ui.delete_entry_btn.clicked.connect(self.delete_entry)
        self.mission_number_only_int()

    def delete_entry(self):
        row = self.ui.stock_table.currentRow()
        self.ui.stock_table.removeRow(row)
        self.ui.stock_table.resizeColumnsToContents()
        self.ui.stock_table.horizontalHeader().setSectionResizeMode(1)

    def clear_table(self):
        self.ui.stock_table.setRowCount(0)
        self.ui.stock_table.resizeColumnsToContents()
        self.ui.stock_table.horizontalHeader().setSectionResizeMode(1)

    def mission_number_only_int(self):
        validator = QIntValidator(0, 999999999)
        self.ui.stock_textfield_mission.setValidator(validator)

    def check_content_in_table(self, product, keyword):
        rows = self.ui.stock_table.rowCount()
        count = 0
        for i in range(0, rows):
            product_tabelle = self.ui.stock_table.item(i, 0).text()
            keyword_tabelle = self.ui.stock_table.item(i, 2).text()
            if product_tabelle == product and keyword_tabelle == keyword:
                amount = int(self.ui.stock_table.item(i, 1).text())
                amount += 1
                number = QtWidgets.QTableWidgetItem()
                number.setData(QtCore.Qt.EditRole, amount)
                number.setTextAlignment(Qt.AlignCenter)
                self.ui.stock_table.setItem(i, 1, QtWidgets.QTableWidgetItem(number))
                self.ui.stock_textfield_product.setText("")
                self.ui.stock_table.resizeColumnsToContents()
                self.ui.stock_table.horizontalHeader().setSectionResizeMode(1)
                count = 1
                break
        return count

    def save_in_table(self): # speichert die daten zunaechst in der tabelle zur ansicht
        mode = self.ui.combobox_stock.currentText()
        mission = self.ui.stock_textfield_mission.text()
        transact = True
        if mode == "Auffüllen nach Einsatz":
            if mission == "":
                self.ui.stock_textfield_mission.setFocus()
                self.ui.stock_error_label.setText("Einsatznummer eingeben!")
                self.ui.stock_error_label.setStyleSheet("color:#ffffff; border: 1px solid red; border-radius: 5px")
                self.ui.stock_textfield_product.setText("")
                return False
        if transact:
            self.ui.stock_error_label.setText(" ")
            self.ui.stock_error_label.setStyleSheet("")
            barcode = self.ui.stock_textfield_product.text()
            product = self.data.produkt_abfrage(barcode)
            if len(product) == 0:
                product = self.data.get_set_products(barcode)
                if len(product) > 0:
                    self.buffer_set(product[0][0])
                else:
                    self.ui.stock_error_label.setText("Produkt mit dem Barcode nicht vorhanden!")
                    self.ui.stock_error_label.setStyleSheet(
                        "color:#ffffff; border: 1px solid red; border-radius: 5px")
                    self.ui.stock_textfield_product.setText("")
            elif len(product) > 0:
                self.buffer_product(product)
                return True
            else:
                return False

    def mode_check(self, text):
        keyword = ""
        if text == "Auffüllen nach Einsatz":
            keyword = self.ui.stock_textfield_mission.text()
        if text == "Auffüllen wegen Fehlbestand":
            keyword = "Auffüllen"
        if text == "Falsch Entnahme - wieder zurück geben":
            keyword = "Zurück"
        return keyword

    def buffer_set(self, product):
        text = self.ui.combobox_stock.currentText()
        keyword = self.mode_check(text)
        if "," in product:
            barcode = product.split(", ")
        else:
            barcode = [product, ]
        products = []
        for i in range(0, len(barcode)):
            product = self.data.produkt_abfrage(barcode[i])
            if len(product) > 0:
                products.append(product[0][0])
        for element in range(0, len(products)):
            test = self.check_content_in_table(products[element], keyword)
            if test == 0:
                mode = (1, 2, 1)
                list = [str(products[element]), 1, str(keyword)]
                self.fill_table.fill_table(list, self.ui.stock_table, mode)
                self.ui.stock_textfield_product.setText("")

    def buffer_product(self, product,):
        text = self.ui.combobox_stock.currentText()
        keyword = self.mode_check(text)
        test = self.check_content_in_table(product[0][0], keyword)
        if test == 0:
            mode = (1, 2, 1)
            list = [str(product[0][0]), 1, str(keyword)]
            self.fill_table.fill_table(list, self.ui.stock_table, mode)

            self.ui.stock_textfield_product.setText("")
        return True

    def save(self): #holt die daten aus der Tabelle und übergibt sie an die passende funktion zum entnehmen etc.
        row = self.ui.stock_table.rowCount()
        for i in range(0, row):
            text = self.ui.stock_table.item(0, 2).text()
            if text == "Zurück":
                item = self.ui.stock_table.item(0, 0).text()
                menge = self.ui.stock_table.item(0, 1).text()
                self.data.auffuellen(item, int(menge))
                self.ui.stock_table.removeRow(0)
            else:

                item = self.ui.stock_table.item(0, 0).text()
                menge = self.ui.stock_table.item(0, 1).text()
                self.data.entnahme(item, int(menge))
                try:
                    nummer = int(text)
                    if nummer >= 0:
                        nummer = self.ui.stock_table.item(0, 2).text()
                        today = date.today()
                        today_format = str(today.day) + '.' + str(today.month) + '.' + str(today.year)
                        self.data.einsatz_nachweis(nummer, item, menge, today_format)
                except (TypeError, ValueError):
                    pass
                self.ui.stock_table.removeRow(0)
        self.ui.stock_error_label.setText("Eingabe Gespeichert")
        self.ui.stock_error_label.setStyleSheet("color:#ffffff; font-size:13pt; border: 1px solid #00FF00; border-radius: 5px")
        self.ui.stock_textfield_mission.setText("")
        Update_Stock(self.ui).update()


    def check_combobox_content(self): # prueft auf welchem text gerade dei Combobox steht um das Einsatznummer feld anzuzeigen oder nicht.
        text = self.ui.combobox_stock.currentText()
        if text == "Falsch Entnahme - wieder zurück geben" or text == "Auffüllen wegen Fehlbestand":
            self.ui.stock_textfield_mission.setVisible(False)
            self.ui.label_einsatznummer.setVisible(False)
        else:
            self.ui.stock_textfield_mission.setVisible(True)
            self.ui.label_einsatznummer.setVisible(True)
        self.ui.stock_textfield_mission.setText("")



