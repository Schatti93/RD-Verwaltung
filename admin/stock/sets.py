from admin.stock.sets_data import Sets_Data
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

class Sets():
    def __init__(self, ui):
        self.ui = ui
        self.data = Sets_Data()

        self.ui.new_set_inhalt_text.returnPressed.connect(self.write_entry_in_new_set_table)
        self.ui.edit_set_combo.currentTextChanged.connect(self.edit_set_table_fill)
        self.ui.new_set_save_btn.clicked.connect(self.new_set)
        self.ui.edit_set_save_btn.clicked.connect(self.update_set)
        self.ui.edit_set_delete_entry_btn.clicked.connect(self.delete_entry)
        self.ui.edit_set_add_barcode.returnPressed.connect(self.new_entry_edit_set)
        self.ui.edit_set_delete_btn.clicked.connect(self.delete_set)

    # actions from buttons

    def delete_set(self):
        barcode = self.ui.edit_set_barcode.text()
        self.data.delete_set(barcode)
        self.edit_set_combo_fill()

    def new_set(self):
        name = self.ui.new_set_name.text()
        barcode = self.ui.new_set_barcode.text()
        barcodes = ""
        rows = self.ui.new_set_table.rowCount()
        for element in range(0, rows):
            if element == 0:
                barcodes = str((self.ui.new_set_table.item(element, 1).text()))
            else:
                barcodes = barcodes + ", " + str((self.ui.new_set_table.item(element, 1).text()))
        self.data.save_set(name, barcode, barcodes)
        self.edit_set_combo_fill()
        self.ui.new_set_table.setRowCount(0)
        self.ui.new_set_name.setText("")
        self.ui.new_set_barcode.setText("")

    def update_set(self):
        set_name = self.ui.edit_set_combo.currentText()
        barcode = self.ui.edit_set_barcode.text()
        rows = self.ui.edit_set_table.rowCount()
        barcodes = ""
        for element in range(0, rows):
            if element == 0:
                barcodes = str((self.ui.edit_set_table.item(element, 1).text()))
            else:
                barcodes = barcodes + ", " + str((self.ui.edit_set_table.item(element, 1).text()))
        self.data.update_set(set_name, barcode, barcodes)
        self.ui.edit_set_combo.setCurrentIndex(0)

    def delete_entry(self):
        row = self.ui.edit_set_table.currentRow()
        self.ui.edit_set_table.removeRow(row)

    # actions from pressed enter

    def write_entry_in_new_set_table(self):
        barcode = self.ui.new_set_inhalt_text.text()
        produkt = self.data.ask_product_name(barcode)
        entry_list = []
        if len(produkt) > 0:
            entry_list.append(produkt[0][0])
            entry_list.append(barcode)
            rows = self.ui.new_set_table.rowCount()
            self.ui.new_set_table.insertRow(rows)
            for i in range(0, 2):
                entry = QtWidgets.QTableWidgetItem(entry_list[i])
                entry.setTextAlignment(Qt.AlignCenter)
                self.ui.new_set_table.setItem(rows, i, entry)
        self.ui.new_set_table.horizontalHeader().setSectionResizeMode(1)
        self.ui.new_set_inhalt_text.setText("")

    def new_entry_edit_set(self):
        barcode = self.ui.edit_set_add_barcode.text()
        name = self.data.ask_product_name(barcode)
        if len(name) > 0:
            rows = self.ui.edit_set_table.rowCount()
            self.ui.edit_set_table.insertRow(rows)
            name = name[0][0]
            entry = QtWidgets.QTableWidgetItem(name)
            entry.setTextAlignment(Qt.AlignCenter)
            self.ui.edit_set_table.setItem(rows, 0, entry)
            entry = QtWidgets.QTableWidgetItem(barcode)
            entry.setTextAlignment(Qt.AlignCenter)
            self.ui.edit_set_table.setItem(rows, 1, entry)
        self.ui.edit_set_add_barcode.setText("")

    # just loading, not doing anything with user

    def edit_set_combo_fill(self):
        self.ui.edit_set_combo.clear()
        entrys = self.data.all_set_names()
        entry_list = ["---"]
        for element in range(0, len(entrys)):
            entry_list.append(entrys[element][0])
        self.ui.edit_set_combo.addItems(entry_list)

   # actions from combobox

    def edit_set_table_fill(self):
        self.ui.edit_set_table.setRowCount(0)
        set_text = self.ui.edit_set_combo.currentText()
        if set_text == "---":
            self.ui.edit_set_barcode.setText("")
            self.ui.edit_set_add_barcode.setText("")
            self.ui.edit_set_table.setRowCount(0)
        else:

            set = self.data.get_set_products(set_text)
            if len(set) == 0:
                pass
            else:
                set = set[0][0]
                if "," in set:
                    set = set.split(", ")
                for element in range(0, len(set)):
                    rows = self.ui.edit_set_table.rowCount()
                    self.ui.edit_set_table.insertRow(rows)
                    product_name = self.data.ask_product_name(set[element])[0][0]
                    entry = QtWidgets.QTableWidgetItem(product_name)
                    entry.setTextAlignment(Qt.AlignCenter)
                    self.ui.edit_set_table.setItem(rows, 0, entry)
                    entry = QtWidgets.QTableWidgetItem(set[element])
                    entry.setTextAlignment(Qt.AlignCenter)
                    self.ui.edit_set_table.setItem(rows, 1, entry)
                self.ui.edit_set_table.horizontalHeader().setSectionResizeMode(1)
                barcode = self.data.get_set_barcode(set_text)[0][0]
                self.ui.edit_set_barcode.setText(barcode)

