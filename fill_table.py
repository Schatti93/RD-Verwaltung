from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5 import QtCore

class Fill_Table():
    def __init__(self, ui):
        self.ui = ui


    def fill_table(self, content, table, mode):
        rows = table.rowCount()
        table.insertRow(rows)
        if table == self.ui.admin_lager_alle_produkte:
            print(content)
        for i in range(0, len(content)):
            if mode[i] == 0:
                entry = self.create_widget(str(content[i]))
            if mode[i] == 1:
                entry = self.create_widget(str(content[i]))
                entry.setFlags(QtCore.Qt.ItemIsEnabled)
            if mode[i] == 2:
                entry = QtWidgets.QTableWidgetItem()
                entry.setData(QtCore.Qt.EditRole, content[i])
                entry.setTextAlignment(Qt.AlignCenter)
            table.setItem(rows, i, entry)

        table.horizontalHeader().setSectionResizeMode(1)

    def create_widget(self, item):
        content = QtWidgets.QTableWidgetItem(item)
        content.setTextAlignment(Qt.AlignCenter)
        return content


