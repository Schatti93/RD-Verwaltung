from admin.stock.admin_lager_data import Admin_Lager_Data
from admin.stock.update_stock import Update_Stock
from fill_table import Fill_Table

class Edit_Stock_Content():
    def __init__(self, ui):
        self.ui = ui
        self.data = Admin_Lager_Data()
        self.update = Update_Stock(self.ui)
        self.fill_table = Fill_Table(self.ui)
        self.ui.admin_produkte_update.clicked.connect(self.change_product)

    def change_product(self):
        rows = self.ui.admin_lager_alle_produkte.rowCount()
        for element in range(0, rows):
            id = self.ui.admin_lager_alle_produkte.item(element, 0).text()
            product = self.ui.admin_lager_alle_produkte.item(element, 1).text()
            in_stock = self.ui.admin_lager_alle_produkte.item(element, 2).text()
            minimal = self.ui.admin_lager_alle_produkte.item(element, 3).text()
            maximum= self.ui.admin_lager_alle_produkte.item(element, 4).text()
            barcode = self.ui.admin_lager_alle_produkte.item(element, 5).text()
            content = self.ui.admin_lager_alle_produkte.item(element, 6).text()
            item_number = self.ui.admin_lager_alle_produkte.item(element, 7).text()
            self.data.update_all_products(id, product, in_stock, minimal, maximum, barcode, content, item_number)
        self.update.update()


    def show_all_products_in_table(self):
        self.ui.admin_lager_alle_produkte.setRowCount(0)
        all_products = self.data.get_liste()
        mode = (1, 0, 2, 2, 2, 0, 2, 0)
        for element in range(0, len(all_products)):
            list = []
            for list_element in range(0, len(all_products[element]) - 1):
                list.append(all_products[element][list_element])
            self.fill_table.fill_table(list, self.ui.admin_lager_alle_produkte, mode)

