from overview.overview import Overview
from admin.stock.admin_lager_data import Admin_Lager_Data
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from fill_table import Fill_Table

class Update_Stock():
    def __init__(self, ui):
        self.ui = ui
        self.data = Admin_Lager_Data()
        self.fill_table = Fill_Table(self.ui)


    def update(self):
        Overview(self.ui).stock_overview()
        self.fehlendes_material()
        self.combobox_bestellung_einpflegen()
        self.show_all_products_in_table()

    def update_from_fehlendes_material(self):
        self.combobox_bestellung_einpflegen()
        self.show_all_products_in_table()
        Overview(self.ui).stock_overview()

    def fehlendes_material(self):
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
                list = [list_of_data[i][1], list_of_data[i][2], list_of_data[i][3], list_of_data[i][4],
                        str(list_of_data[i][7]), status]
                mode = (0, 2, 2, 2, 0, 1)
                self.fill_table.fill_table(list, self.ui.admin_lager_fehlendes_material, mode)

    def combobox_bestellung_einpflegen(self):
        self.ui.admin_material_save_combo.clear()
        liste_der_daten = self.data.get_liste()
        liste_der_eintraege = ["---"]
        for eintrag in liste_der_daten:
            liste_der_eintraege.append(eintrag[1])
        self.ui.admin_material_save_combo.addItems(liste_der_eintraege)

    def show_all_products_in_table(self):
        self.ui.admin_lager_alle_produkte.setRowCount(0)
        all_products = self.data.get_liste()
        mode = (1, 0, 2, 2, 2, 0, 2, 0)
        for element in range(0, len(all_products)):
            list = []
            for list_element in range(0, len(all_products[element]) - 1):
                list.append(all_products[element][list_element])
            self.fill_table.fill_table(list, self.ui.admin_lager_alle_produkte, mode)