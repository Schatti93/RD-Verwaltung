from PyQt5.QtGui import QIntValidator
from stock.stock_management_data import Stock_Management_Data
from admin.stock.missing_material import Missing_Material
from admin.stock.maintain_material import Maintain_Material
from admin.stock.edit_stock_content import Edit_Stock_Content
from admin.stock.new_delete import New_Delete
from admin.stock.sets import Sets

class Admin_Stock():
    def __init__(self, ui):
        self.ui = ui
        self.lager = Stock_Management_Data()

        ### aufruf bei start des programms
        self.input_boxes_int()

        self.missing_Material = Missing_Material(self.ui)
        self.missing_Material.show_missing_material()

        self.maintain_material = Maintain_Material(self.ui)
        self.maintain_material.combobox_maintain_order()

        self.edit_stock_content = Edit_Stock_Content(self.ui)
        self.edit_stock_content.show_all_products_in_table()

        self.new_delete = New_Delete(self.ui)

        self.sets = Sets(self.ui)
        self.sets.edit_set_combo_fill()

    def input_boxes_int(self):
        validator = QIntValidator(0, 999999999)
        self.ui.admin_material_save_number.setValidator(validator)
        self.ui.admin_new_prod_in_stock.setValidator(validator)
        self.ui.admin_new_prod_min.setValidator(validator)
        self.ui.admin_new_prod_max.setValidator(validator)
        self.ui.admin_new_prod_content.setValidator(validator)
