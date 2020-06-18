from admin.stock.admin_lager_data import Admin_Lager_Data
from PyQt5.QtWidgets import QMessageBox
from admin.stock.update_lager import Update_Stock
from fill_table import Fill_Table
from admin.barcodes.barcodes import Generate_Barcodes

class New_Delete():
    def __init__(self, ui):
        self.ui = ui
        self.data = Admin_Lager_Data()
        self.barcode = Generate_Barcodes()
        self.update = Update_Stock(self.ui)
        self.fill_table = Fill_Table(self.ui)
        #return actions
        self.ui.admin_new_prod_item.returnPressed.connect(self.show_new_product_in_table)
        self.ui.admin_del_prod_prod.returnPressed.connect(self.fill_delete_table)
        self.ui.admin_del_prod_bar.returnPressed.connect(self.fill_delete_table)
        # button actions
        self.ui.admin_del_prod_btn.clicked.connect(self.del_message_box)
        self.ui.admin_new_prod_btn.clicked.connect(self.sammeln)
        self.ui.admin_new_prod_create_barcode.clicked.connect(self.set_barcode)


    def show_new_product_in_table(self):
        mode = (0, 2, 2, 2, 0, 2, 0)
        list = [self.ui.admin_new_prod_prod.text(), self.ui.admin_new_prod_in_stock.text(),
                self.ui.admin_new_prod_min.text(), self.ui.admin_new_prod_max.text(),
                self.ui.admin_new_prod_bar.text(), self.ui.admin_new_prod_content.text(),
                self.ui.admin_new_prod_item.text()]
        self.fill_table.fill_table(list, self.ui.admin_new_prod_table, mode)

    def sammeln(self):
        rows = self.ui.admin_new_prod_table.rowCount()
        for i in range(0, rows):
            list = []
            for J in range(0, 7):
                list.append(self.ui.admin_new_prod_table.item(0, J).text())
            self.ui.admin_new_prod_table.removeRow(0)
            self.data.new_produkt(list[0], list[1], list[2], list[3], list[4], list[5], list[6], "NULL")
        self.update.update()

    def fill_delete_table(self):
        product = self.ui.admin_del_prod_prod.text()
        barcode = self.ui.admin_del_prod_bar.text()
        self.ui.admin_del_prod_label.setText("")
        if product == "" and barcode == "":
            pass

        elif barcode == "":
            item = self.data.get_barcode(product)
            try:
                if item[0][0] == "":
                    self.ui.admin_del_prod_prod.setText("")
                else:
                    mode = (1, 1)
                    list = [str(product), str(item[0][0])]
                    self.fill_table.fill_table(list, self.ui.admin_del_prod_table, mode)
            except IndexError:
                self.ui.admin_stock_delete_error.setText("<html><head/><body><p><span style=\" color:#ff0000;\">"
                                                           "Produkt nicht vorhanden.</span></p></body></html>")
        elif product == "":
            item = self.data.get_product(barcode)
            try:
                if item[0][0] == "":
                    self.ui.admin_del_prod_bar.setText("")
                else:
                    mode = (1, 1)
                    list = [str(product), str(item[0][0])]
                    self.fill_table.fill_table(list, self.ui.admin_del_prod_table, mode)
            except IndexError:
                self.ui.admin_stock_delete_error.setText("<html><head/><body><p><span style=\" color:#ff0000;\">"
                                                           "Produkt nicht vorhanden.</span></p></body></html>")

    def produkt_loeschen(self):
        rows = self.ui.admin_del_prod_table.rowCount()
        for i in range(0, rows):
            item = self.ui.admin_del_prod_table.item(0, 0).text()
            self.data.del_product(item)
            self.ui.admin_del_prod_table.removeRow(0)
        self.ui.admin_del_prod_label.setText("<html><head/><body><p><span style=\" color:#00FF00;\">"
                                          "Eingabe Gespeichert</span></p></body></html>")
        self.update.update()

    def set_barcode(self):
        barcode = self.barcode.generate_barcode()
        self.ui.admin_new_prod_bar.setText(barcode)

    def del_message_box(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Möchten Sie die Produkte wirklich löschen? \nDie Produkte werden unwiderruflich aus der Datenbank gelöscht.")
        msgBox.setWindowTitle("Wirklich löschen?")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            self.produkt_loeschen()