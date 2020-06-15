from admin.stock.admin_lager_data import Admin_Lager_Data
from admin.stock.update_lager import Update_Stock
from fill_table import Fill_Table
class Bearbeiten():
    def __init__(self, ui):
        self.ui = ui
        self.fill_table = Fill_Table(self.ui)
        self.data = Admin_Lager_Data()
        self.update = Update_Stock(self.ui)
        self.ui.admin_produkte_update.clicked.connect(self.produkte_aendern)

    def produkte_aendern(self):
        rows = self.ui.admin_lager_alle_produkte.rowCount(0)
        for element in range(0, rows):
            id = self.ui.admin_lager_alle_produkte.item(element, 0).text()
            produkt = self.ui.admin_lager_alle_produkte.item(element, 1).text()
            bestand = self.ui.admin_lager_alle_produkte.item(element, 2).text()
            minimal = self.ui.admin_lager_alle_produkte.item(element, 3).text()
            maximal = self.ui.admin_lager_alle_produkte.item(element, 4).text()
            barcode = self.ui.admin_lager_alle_produkte.item(element, 5).text()
            inhalt = self.ui.admin_lager_alle_produkte.item(element, 6).text()
            artikelnr = self.ui.admin_lager_alle_produkte.item(element, 7).text()
            self.data.update_alle_produkte(id, produkt, bestand, minimal, maximal, barcode, inhalt, artikelnr)
        self.update.update()

    def alle_produkte_anzeigen_table(self):
        all_products = self.data.get_liste()
        list = []
        mode = (1, 0, 2, 2, 2, 0, 2, 0)
        for element in range(0, len(all_products)):
            for list_element in range(0, len(all_products[element]) - 1):
                list.append(all_products[element][list_element])
            self.ui.admin_lager_alle_produkte.setRowCount(0)
            self.fill_table.fill_table(list, self.ui.admin_lager_alle_produkte, mode)
            list = []