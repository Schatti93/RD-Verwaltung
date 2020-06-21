from admin.stock.admin_lager_data import Admin_Lager_Data
from admin.pdf_bestellung.pdf_bestellung import Pdf_Bestellung
from admin.stock.update_stock import Update_Stock
from admin.stock.online_order import Online_Bestellung
from fill_table import Fill_Table

class Missing_Material():
    def __init__(self, ui):
        self.ui = ui
        self.fill_table = Fill_Table(self.ui)
        self.data = Admin_Lager_Data()
        self.pdf = Pdf_Bestellung(self.ui)
        self.ui.pdf_erstellen.clicked.connect(self.pdf_erstellen)
        self.update = Update_Stock(self.ui)
        self.bestellen = Online_Bestellung()
        #self.ui.lager_bestellung.clicked.connect(self.bestellen.nachbestellen)

    def pdf_erstellen(self):
        self.pdf.pdf_erstellen()
        self.update.update()

    def show_missing_material(self):
        list_of_data = self.data.get_liste()

        self.ui.admin_lager_fehlendes_material.setRowCount(0)

        for i in range(0, len(list_of_data)):
            if list_of_data[i][2] >= list_of_data[i][3]:
                if list_of_data[i][8] == "Ausreichend":
                    pass
                else:
                    self.data.update_status(list_of_data[i][1], "Ausreichend")
            else:
                if list_of_data[i][8] == "Bestellt":
                    status = "Bestellt"
                else:
                    self.data.update_status(list_of_data[i][1], "Bestand zu gering")
                    status = "Bestand zu gering"
                list = [list_of_data[i][1], list_of_data[i][2], list_of_data[i][3], list_of_data[i][4], str(list_of_data[i][7]), status]
                mode = (0, 2, 2, 2, 0, 1)
                self.fill_table.fill_table(list, self.ui.admin_lager_fehlendes_material, mode)