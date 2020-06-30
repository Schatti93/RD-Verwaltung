from datetime import date
from clothes.clothes_data import Clothes_Data

class Clothes():
    def __init__(self, ui, fill_table):
        self.ui = ui
        self.data = Clothes_Data()
        self.fill_table = fill_table
        self.ui.clothes_button.clicked.connect(self.go_through_table_entrys)
        self.ui.clothes_textfield.returnPressed.connect(self.content_to_save)
        self.read_from_database("Klamotten", "kleidung_zurueck")

    def content_to_save(self):
        content = [self.ui.clothes_textfield.text()]
        mode = (1, )
        self.fill_table.fill_table(content, self.ui.cloth_to_save, mode)
        self.ui.clothes_textfield.setText("")

    def go_through_table_entrys(self):
        row = self.ui.cloth_to_save.rowCount()
        for i in range(0, row):
            item = self.ui.cloth_to_save.item(0, 0).text()
            self.in_out(item)
            self.ui.cloth_to_save.removeRow(0)

    def read_from_database(self, first_database, second_database):
        list = self.data.get_liste(first_database)
        mode = (1, 1)
        self.ui.clothes_away.setRowCount(0)
        for i in range(0, len(list)):
            self.fill_table.fill_table(list[i], self.ui.clothes_away, mode)

        list = self.data.get_liste(second_database)
        self.ui.clothes_back.setRowCount(0)
        for i in range(0, len(list)):
            self.fill_table.fill_table(list[i], self.ui.clothes_back, mode)

    def in_out(self, content):
        mode = (1, 1)
        row = self.ui.clothes_away.rowCount()
        today = date.today()
        today_format = str(today.day) + '.' + str(today.month) + '.' + str(today.year)
        self.data.check_barcode(content)
        for i in range(0, row):
            item = self.ui.clothes_away.item(i, 0).text()
            if item == content:
                self.ui.clothes_away.removeRow(i)
                list = [content, today_format]
                self.fill_table.fill_table(list, self.ui.clothes_back, mode)
                break
            else:
                if i == row - 1:
                    list = [content, today_format]
                    self.fill_table.fill_table(list,  self.ui.clothes_away, mode)
