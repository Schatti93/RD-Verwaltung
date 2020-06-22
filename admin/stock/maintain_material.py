from admin.stock.admin_lager_data import Admin_Lager_Data
from admin.stock.update_stock import Update_Stock
from fill_table import Fill_Table
from error_message_boxes import Error_Message_Boxes

class Maintain_Material():
    def __init__(self, ui):
        self.ui = ui
        self.error = Error_Message_Boxes()
        self.data = Admin_Lager_Data()
        self.update = Update_Stock(self.ui)
        self.fill_table = Fill_Table(self.ui)
        # return actions
        self.ui.admin_material_save_barcode.returnPressed.connect(self.maintain_order_barcode_enter)
        self.ui.admin_material_save_number.returnPressed.connect(self.maintain_order_tabelle)
        # button actions
        self.ui.admin_material_save_button.clicked.connect(self.maintain_order)

    def combobox_maintain_order(self):
        self.ui.admin_material_save_combo.clear()
        list_of_datas = self.data.get_liste()
        list_of_entries = ["---"]
        for entry in list_of_datas:
            list_of_entries.append(entry[1])
        self.ui.admin_material_save_combo.addItems(list_of_entries)

    def maintain_order_barcode_enter(self):
        barcode = self.ui.admin_material_save_barcode.text()
        product = self.data.get_product(barcode)
        try:
            index = self.ui.admin_material_save_combo.findText(product[0][0])
            self.ui.admin_material_save_combo.setCurrentIndex(index)
            self.ui.admin_material_save_number.setFocus()
        except IndexError:
            self.error.message_box_only_ok("Der Barcode ist nicht hinterlegt.", "Barcode nicht bekannt")

    def maintain_order_tabelle(self):
        product = self.ui.admin_material_save_combo.currentText()
        if product == "---":
            self.maintain_order_barcode_enter()
            product = self.ui.admin_material_save_combo.currentText()
        number = self.ui.admin_material_save_number.text()
        list = [product, int(number)]
        mode = [1, 2]
        self.fill_table.fill_table(list, self.ui.admin_material_save_table, mode)
        self.ui.admin_material_save_combo.setCurrentIndex(0)
        self.ui.admin_material_save_number.setText("")
        self.ui.admin_material_save_barcode.setText("")

    def maintain_order(self):
        rows = self.ui.admin_material_save_table.rowCount()
        for eintrag in range(0, rows):
            produkt = self.ui.admin_material_save_table.item(0, 0).text()
            anzahl = int(self.ui.admin_material_save_table.item(0, 1).text())
            vorhanden = self.data.get_barcode(produkt)
            if len(vorhanden) > 0:
                self.data.fill_up(vorhanden[0][0], anzahl)
                self.ui.admin_material_save_table.removeRow(0)
                self.data.update_status(produkt, "Ausreichend")
            else:
                self.error.message_box_only_ok("Das produkt: " + produkt + " ist nicht in der Datenbank hinterlegt",
                                              " Produkt nicht vorhanden")
        self.update.update()
