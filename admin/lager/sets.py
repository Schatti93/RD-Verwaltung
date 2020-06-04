from admin.lager.sets_data import Sets_Data
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

class Sets():
    def __init__(self, ui):
        self.ui = ui
        self.data = Sets_Data()
        self.ui.new_set_inhalt_text.returnPressed.connect(self.write_entry_in_new_set_table)

    def new_set(self):
        name = self.ui.new_set_name.text()
        barcode = self.ui.new_set_barcode.text()
        barcodes = []
        rows = self.ui.new_set_table.rowCount()
        for element in range(0, rows):
            barcodes.append(self.ui.new_set_table.item(element, 1).text())
        self.data.save_set(name, barcode, barcodes)
        self.edit_set_combo_fill()
        self.ui.edit_set_table.setRowCount(0)
        self.ui.new_set_name.setText("")
        self.ui.new_set_barcode.setText("")

    def write_entry_in_new_set_table(self):
        barcode = self.ui.new_set_inhalt_text.text()
        produkt = self.data.ask_produkt_name(barcode)
        entry_list = []
        if len(produkt) > 0:
            entry_list.append(produkt[0][0])
            entry_list.append(barcode)
            rows = self.ui.edit_set_table.rowCount()
            for i in range(0, 1):
                entry = QtWidgets.QTableWidgetItem(entry_list[i])
                entry.setTextAlignment(Qt.AlignCenter)
                self.ui.edit_set_table.setItem(rows, i, QtWidgets.QTableWidgetItem(entry))
        self.ui.edit_set_table.horizontalHeader().setSectionResizeMode(1)
        self.ui.new_set_inhalt_text.setText("")


    ### just loading, not doing anything with user
    def edit_set_combo_fill(self):
        self.ui.edit_set_combo.clear()
        entrys = self.data.ask_set_names()
        entry_list = ["---"]
        for element in range(0, len(entrys)):
            entry_list.append(entrys[element][0])
        self.ui.edit_set_combo.addItems(entry_list)
