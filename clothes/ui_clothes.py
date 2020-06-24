from ui.ui_manager import UI_Manager
from clothes.clothes import Clothes
from datetime import date

class UI_Clothes(UI_Manager):
    def __init__(self, ui):
        super().__init__(ui)
        self.ui = ui
        self.clothes = Clothes(self.ui)
        self.read_from_database()
        self.ui.clothes_button.clicked.connect(self.go_through_table_entrys)
        self.ui.clothes_textfield.returnPressed.connect(self.content_to_save)

    def content_to_save(self):
        content = [self.ui.clothes_textfield.text()]
        mode = (1,)
        self.fill_table(content, self.ui.cloth_to_save, mode)

    def read_from_database(self):
        self.ui.clothes_away.setRowCount(0)
        datas = self.clothes.read_from_database("Klamotten")
        for i in range(0, len(datas)):
            self.fill_table(datas[i][0], self.ui.clothes_away, datas[i][1])

        self.ui.clothes_back.setRowCount(0)
        datas = self.clothes.read_from_database("kleidung_zurueck")
        for i in range(0, len(datas)):
            self.fill_table(datas[i][0], self.ui.clothes_back, datas[i][1])

    def go_through_table_entrys(self):
        mode = (1, 1)
        rows = self.ui.cloth_to_save.rowCount()
        for i in range(0, rows):
            content = self.ui.cloth_to_save.item(rows, 0).text()
            check = self.clothes.in_out(content)
            if check == True:
                self.fill_table([content], self.ui.clothes_away, mode)
            if check == False:
                self.fill_table([content], self.ui.clothes_back, mode)
