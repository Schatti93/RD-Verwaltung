from admin.stock.admin_lager_data import Admin_Lager_Data
from admin.pdf_bestellung.pdf_bestellung import Pdf_Bestellung
from admin.stock.update_lager import Update_Stock
from admin.stock.online_bestellung import Online_Bestellung
from fill_table import Fill_Table

class Missing_Material():
    def __init__(self, ui):
        self.ui = ui
        self.fill_table = Fill_Table(self.ui)
        self.data = Admin_Lager_Data()
        self.ui.pdf_erstellen.clicked.connect(Pdf_Bestellung(self.ui).pdf_erstellen)
        self.update = Update_Stock(self.ui)
        self.bestellen = Online_Bestellung()
        #self.ui.lager_bestellung.clicked.connect(self.bestellen.nachbestellen)

    def show_missing_material(self):
        liste = self.data.get_liste()

        self.ui.admin_lager_fehlendes_material.setRowCount(0)

        for i in range(0, len(liste)):
            if liste[i][2] >= liste[i][3]:
                if liste[i][8] == "Ausreichend":
                    pass
                else:
                    self.data.update_status(liste[i][1], "Ausreichend")
            else:
                if liste[i][8] == "NULL":
                    self.data.update_status(liste[i][1], "Bestand zu gering")
                    status = "Bestand zu gering"
                else:
                    status = "Bestand zu gering"
                list = [liste[i][1], liste[i][2], liste[i][3], liste[i][4], str(liste[i][7]), status]
                mode = (0, 2, 2, 2, 0, 1)
                self.fill_table.fill_table(list, self.ui.admin_lager_fehlendes_material, mode)