
class UI_Clothes():
    def __init__(self, ui):
        self.ui = ui
        self.ui.clothes_button.clicked.connect(self.go_through_table_entrys)
        self.ui.clothes_textfield.returnPressed.connect(self.content_to_save)
        