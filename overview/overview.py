from stock.stock_management_data import Stock_Management_Data
from fill_table import Fill_Table

class Overview():
    def __init__(self, ui):
        self.ui = ui
        self.fill_table = Fill_Table(self.ui)
        self.data = Stock_Management_Data()
        self.stock_overview()

    def stock_overview(self):
        list = self.data.get_liste()
        count = 0
        status = ""
        self.ui.overview_stock_table.setRowCount(0)
        for i in range(0, len(list)):

            if list[i][2] < list[i][3]:
                if list[i][8] == "Bestellt":
                    status = "Bestellt"
                else:
                    self.data.update_status(list[i][1], "Bestand zu gering")
                    status = "Bestand zu gering"
                list_to_set = [list[i][1], str(list[i][2]), str(list[i][3]), status]
                mode = (1, 1, 1, 1)
                self.fill_table.fill_table(list_to_set, self.ui.overview_stock_table, mode)
                count += 1
            else:
                continue
        if count == 0:
            self.ui.label_overview_stock.setText("Lager ist Voll")
            self.ui.label_overview_stock.setStyleSheet(
                "color:#ffffff; font-size:13pt; border: 1px solid #00FF00; border-radius: 5px")
            self.ui.uebersicht_lager_table.setVisible(False)
        elif status == "Bestand zu gering":
            self.ui.label_overview_stock.setText("Fehlendes Material")
            self.ui.label_overview_stock.setStyleSheet(
                "color:#ffffff; font-size:13pt; border: 1px solid red; border-radius: 5px")
        else:
            self.ui.label_overview_stock.setText("Bestellt")
            self.ui.label_overview_stock.setStyleSheet(
                "color:#ffffff; font-size:13pt; border: 1px solid orange; border-radius: 5px")



